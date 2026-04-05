import requests
import pandas as pd
import os
import sqlite3 # For SQL database operations (local file-based database), PostgreSQL, MySQL or MS SQL Server would require additional setup and libraries.
from bs4 import BeautifulSoup

# 1. Fetch the data
url = "https://quotes.toscrape.com/tag/love/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}

response = requests.get(url, headers=headers)
response.raise_for_status()

# 2. Parse the HTML
soup = BeautifulSoup(response.text, "lxml")

# 3. Extract quotes.
quotes = soup.select("div.quote")

scraped_data = []
for q in quotes:
    text = q.select_one("span.text").get_text(strip=True)
    author = q.select_one("small.author").get_text(strip=True)
    
    print(f"Scraping: {text[:50]}...")
    scraped_data.append({"Quote": text, "Author": author})

# 4. Save to CSV.
df = pd.DataFrame(scraped_data)
df.to_csv("quotes.csv", index=False)

print(f"\nDone! Saved {len(df)} quotes to quotes.csv in {os.getcwd()}.")

# 5. Save to SQL.
# Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect("quotes_db.sqlite")
cursor = conn.cursor()

# Create the table with Primary Key and Unique constraint
cursor.execute('''
    CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Quote TEXT NOT NULL UNIQUE, 
        Author TEXT NOT NULL
    )
''')

# Insert data while ignoring duplicates.
data_to_insert = list(df.itertuples(index=False, name=None))
cursor.executemany("INSERT OR IGNORE INTO quotes (Quote, Author) VALUES (?, ?)", data_to_insert)

conn.commit()
conn.close()

print(f"SQL Database sync complete in {os.getcwd()}.")
