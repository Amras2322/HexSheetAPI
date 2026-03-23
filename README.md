# HexSheet API Scripts

A collection of Python scripts for interacting with the HexSheet Supabase API. These scripts are primarily used for managing homebrew spells and retrieving character data.

## Prerequisites

- Python 3.x
- `requests` library
- `python-dotenv` library

You can activate the included virtual environment (`venv`) which likely has these dependencies installed:
```bash
source venv/bin/activate
# Or on Windows: venv\Scripts\activate
```

Alternatively, install the required packages:
```bash
pip install requests python-dotenv
```

## Setup

Create a `.env` file in the root directory of this project and add your API key:
```env
API_KEY=your_api_key_here
```

## Available Scripts

### Spells Management
- **`AddManySpellsFromCSV.py`**: Reads spell data from `Spells.csv`, formats the fields (e.g. casting times, levels, classes, duration), and uploads them in bulk to the homebrew spells endpoint.
- **`AddSingleSpell.py`**: An example script that manually constructs a payload for a single spell (Ice Knife) and POSTs it to the API. 
- **`GetSpellFromHomebrew.py`**: Fetches all homebrew spells from the API and saves the retrieved data to a local `spells.json` file.

### Characters
- **`GetCharacters.py`**: A simple script to fetch your characters from the characters API endpoint.

### Utility
- **`CheckRateLimit.py`**: Makes a lightweight HTTP request to check your current API rate limit status, remaining quota, and reset time headers.

## Usage Example

```bash
# Fetch spells and save to spells.json
python GetSpellFromHomebrew.py

# Check rate limit
python CheckRateLimit.py
```
