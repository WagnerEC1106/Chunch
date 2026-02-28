import os
import json
import gspread
from google.oauth2.service_account import Credentials

# 1️⃣ Get the JSON key from environment variable
json_key = os.environ.get("GSHEET_KEY")
if not json_key:
    raise ValueError("GSHEET_KEY environment variable not set!")

# 2️⃣ Load credentials from the JSON string
creds_dict = json.loads(json_key)
creds = Credentials.from_service_account_info(
    creds_dict,
    scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
)

# 3️⃣ Authorize gspread client
client = gspread.authorize(creds)

# 4️⃣ Open the sheet by spreadsheet ID
SPREADSHEET_ID = "1GcAWPJzaVvwS0LzO_c2wnWVlgM7Pqw2yg8aRtaMnsT0"
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# 5️⃣ Read all rows
rows = sheet.get_all_records()

# 6️⃣ Save to JSON file (optional)
import json
with open("data/sheet_data.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=4, ensure_ascii=False)

print(f"Saved {len(rows)} rows to data/sheet_data.json")