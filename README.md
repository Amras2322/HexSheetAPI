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
The **`AddManySpellsFromCSV.py`** script was written to be used with spells lists from [5e.tools](https://5e.tools/spells).
Use the filters to show the spells you wish to export/import to hexsheet, then click "Table View"
<img width="1173" height="566" alt="Screenshot_20260323_011543-1" src="https://github.com/user-attachments/assets/4f564deb-a67e-4b4a-9b53-3290ae0b8a5f" />
From the table view, click the button to download the spell list as a CSV. The script should be able to process this file.

