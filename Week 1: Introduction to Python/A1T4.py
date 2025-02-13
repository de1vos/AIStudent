# Task 4: JSON

## Story:
# You are building a program which stores information about books 
# in a library to disk. You want to use a dictionary to store the book 
# information and save it to a JSON file for persistence.

## Tasks:
# - Create a dictionary to store information about a book, including `title`,
#   `author`, `year`, and `ISBN`.
# - Save the book information to a JSON file using the `json` module.
# - Load the book information from the JSON file and display it.

## Starting Point:
import json

# Book information
book = {
    "title": "The Great Gatsby", 
    "author": "F. Scott Fitzgerald", 
    "year": 1925, 
    "ISBN": "9780743273565"
}

# Save book information to a JSON file
with open("book.json", "w") as file:
    json.dump(book, file)

# Load book information from the JSON file
with open("book.json", "r") as file:
    book_info = json.load(file)

print(f"""
    Book Information:
    Title: {book_info["title"]}
    Author: {book_info["author"]}
    Year: {book_info["year"]}
    ISBN: {book_info["ISBN"]}
    """)