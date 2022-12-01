import pandas as pd

from slugify import slugify

# Create a dataFrame from csv file
data = pd.read_csv("_data/books.csv", sep=',', engine ='python', encoding="utf-8").fillna('')

# Set the titles column to a list
books = data.values.tolist()

# Loop through each name, create .md file, set contents to string
for book in books:
	author2 =str(book[18])# str is a function
	author3 =str(book[22])	
	# the next lines create the different components of the url for the main author
	author_raw = str(book[14])
	author_split = author_raw.split(" ") # split is a built-in method, we are transforming the full name of the author into a list
	author_short = (author_split[-3:])
	author = "-".join(author_short)
	# the next lines create the different components of the url for the title
	title_raw = str(book[0]) 
	title_split = title_raw.split(" ")
	title_short = (title_split[:4])
	title = "-".join(title_short)

	year = str(book[3])

	url_raw = title+"-"+author+"-"+year
	
	url = slugify(url_raw) # slugify is an imported app


	file_name = f'_books/{url}.md'	
	xcrpt = str(book[9])


	with open(file_name, 'w', encoding="utf-8") as f:
		f.write(f'---\ntitle: {title_raw}\nauthor: {author_raw}\nauthor2: {author2}\nauthor3: {author3}\n---\n{xcrpt}')
		f.close()
	print(f'{file_name} saved')