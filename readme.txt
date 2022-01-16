Put quotes in first column of first sheet. The first column of the second sheet shows what's been chosen already. Remove a number from there to have it added to the pool again. Once all quotes are used, it'll add them all again to the pool.

You need a data.xlsx file in the same place as the script or executable. The file needs the first sheet with your quotes named "quotes", and a second sheet named "used_numbers". The rolled quote gets output to lastquote.txt.

To run the script itself instead of the executable, install the single required by running "pip install openpyxl". 

TODO: 
Don't require explicit .xlsx sheet names.
Maybe see if I can pull from a Google Sheet too, or if Google Drive for Desktop works.