import requests
import os
import csv
import re
from dotenv import load_dotenv

load_dotenv()

url = "https://nmzkkypjourlffqrzpkq.supabase.co/functions/v1/api/v1/homebrew/spells"
headers = {"x-api-key": os.getenv("API_KEY"), "Content-Type": "application/json"}


def parse_level(level_str):
    """Convert level string to integer"""
    if level_str.lower() == "cantrip":
        return 0
    # Extract number from strings like "1st", "2nd", "3rd", "4th", etc.
    match = re.search(r"(\d+)", level_str)
    if match:
        return int(match.group(1))
    return 0  # Default fallback


def parse_classes(classes_str, optional_classes_str=""):
    """Parse classes string into list of dicts"""
    combined_str = f"{classes_str},{optional_classes_str}".strip(",")
    if not combined_str or combined_str.strip() == "":
        return []

    # Split by comma and clean up
    class_list = [cls.strip() for cls in combined_str.split(",") if cls.strip()]
    result = []
    seen_indices = set()
    for cls in class_list:
        # Remove parenthetical parts
        base_name = re.sub(r"\s*\(.*?\)", "", cls).strip()
        index = base_name.lower().replace(" ", "-").replace("'", "")
        if index not in seen_indices:
            seen_indices.add(index)
            result.append({"name": base_name, "index": index})
    return result

def parse_casting_time(casting_time_str):
    """Parse casting time to API expected format"""
    time_str = casting_time_str.lower()
    if "bonus" in time_str:
        return "1 Bonus Action"
    if "reaction" in time_str:
        return "1 Reaction"
    if "action" in time_str:
        return "1 Action"
    if "min" in time_str:
        match = re.search(r"(\d+)", time_str)
        val = match.group(1) if match else "1"
        return f"{val} Minute" if val == "1" else f"{val} Minutes"
    if "hour" in time_str:
        match = re.search(r"(\d+)", time_str)
        val = match.group(1) if match else "1"
        return f"{val} Hour" if val == "1" else f"{val} Hours"
    return casting_time_str

def parse_components(components_str):
    """Strip out material component text from components"""
    if not components_str:
        return ""
    # Remove everything in parentheses
    clean_str = re.sub(r"\s*\(.*?\)", "", components_str)
    return clean_str.strip()

def extract_material(components_str):
    """Extract material component from components string"""
    if not components_str or "M" not in components_str:
        return ""
    # Find text between parentheses if present
    match = re.search(r"\(([^)]+)\)", components_str)
    if match:
        return match.group(1)
    return ""


def is_ritual(casting_time_str):
    """Determine if spell is ritual"""
    return "ritual" in casting_time_str.lower()


def is_concentration(duration_str):
    """Determine if spell requires concentration"""
    return "concentration" in duration_str.lower()


def parse_duration(duration_str):
    """Parse duration to remove concentration text and use Title Case"""
    if not duration_str:
        return ""
    # Remove "Concentration, up to "
    clean_str = re.sub(r"concentration,\s*up to\s*", "", duration_str, flags=re.IGNORECASE).strip()
    
    # Capitalize words
    words = clean_str.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)


def generate_index(name):
    """Generate URL-friendly index from spell name"""
    # Convert to lowercase, replace spaces and special characters with hyphens
    index = re.sub(r"[^a-z0-9]+", "-", name.lower())
    # Remove leading/trailing hyphens
    index = index.strip("-")
    return index


def process_spell_row(row):
    """Convert CSV row to spell payload"""
    payload = {
        "name": row["Name"],
        "index": generate_index(row["Name"]),
        "level": parse_level(row["Level"]),
        "school": row["School"],
        "casting_time": parse_casting_time(row["Casting Time"]),
        "ritual": is_ritual(row["Casting Time"]),
        "concentration": is_concentration(row["Duration"]),
        "range": row["Range"],
        "components": parse_components(row["Components"]),
        "material": extract_material(row["Components"]),
        "duration": parse_duration(row["Duration"]),
        "description": row["Text"],
        "higher_levels": row["At Higher Levels"],
        "ruleset": "2024",
        "classes": parse_classes(row["Classes"], row.get("Optional/Variant Classes", "")),
        "is_public": True,
    }
    return payload


def main():
    csv_file = "./Spells.csv"

    try:
        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for i, row in enumerate(reader, 1):
                print(f"Processing spell {i}: {row['Name']}")

                payload = process_spell_row(row)

                # Print payload for debugging (first few lines)
                if i <= 3:  # Show first 3 spells
                    print(f"  Payload: {payload}")

                try:
                    response = requests.post(url, headers=headers, json=payload)
                    data = response.json()
                    print(f"  Response: {data}")

                    # Check if successful
                    if response.status_code == 200 or response.status_code == 201:
                        print(f"  ✓ Successfully posted {row['Name']}")
                    else:
                        print(
                            f"  ✗ Failed to post {row['Name']}: {response.status_code}"
                        )

                except Exception as e:
                    print(f"  ✗ Error posting {row['Name']}: {str(e)}")

                print()  # Empty line for readability

    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_file}")
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")


if __name__ == "__main__":
    main()
