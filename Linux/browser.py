import os
import sqlite3


# Build Data path

history_db = f'/home/kali/.mozilla/firefox/8paorn9b.default-esr/places.sqlite/'

# Make connection with sqlite3 database
c = sqlite3.connect(history_db)

# Create cursor object to execute query
cursor = c.cursor()
select_statement = "select moz_places.url, moz_places.visit_count from moz_places;"
cursor.execute(select_statement)

# Fetch the result and Prints the result
results = cursor.fetchall()

for url, count in results:
	print(url)
		
# Close the cursor
cursor.close()

