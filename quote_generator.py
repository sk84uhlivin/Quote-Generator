import linecache
from random import randint

quotes_filepath = 'quotes.txt'
lastquote_filepath = 'lastquote.txt'
padding = 20

# Function for removing newline characters.
def strip_string(string):
	string = string.replace('\n','')
	string = string.rstrip()
	return string

# Calculate number of quotes (lines in quotes file).
with open(quotes_filepath, "r", encoding='utf-8') as f:
	text = f.readlines()
	size = len(text)

# Rolls for quotes until the rolled quote isn't the last quote, and then makes it the new last quote.
while True:
	# Pick a random number between 1 and number of quotes.
	random_number = randint(1, size)
	
	# Retrieve quote.
	quote = linecache.getline(quotes_filepath, random_number)
	quote = strip_string(quote)
	
	# Check to see if this was the last picked quote.
	lastquote = linecache.getline(lastquote_filepath, 1)
	lastquote = strip_string(lastquote)
		
	if quote == lastquote:
		pass
	else:
		# Write new quote with space padding for scrolling.
		with open(lastquote_filepath, "w", encoding='utf-8') as f:
			f.write(quote + (' ' * padding))
			f.close()
		break
		
print(quote)
