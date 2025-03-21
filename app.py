import json
import os

LIBRARY_FILE = "library.json"

# Load library data from file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            try:
                data = file.read().strip()
                return json.loads(data) if data else []
            except json.JSONDecodeError:
                print("Error: library.json is corrupted. Resetting the file.")
                return []
    return []

# Save library data to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a new book to the library
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")
    genre = input("Enter genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower()
    
    library = load_library()
    library.append({"title": title, "author": author, "year": year, "genre": genre, "read": read_status})
    save_library(library)
    print("Book added successfully!\n")

# View all books in the library
def view_books():
    library = load_library()
    if not library:
        print("No books in the library.\n")
        return
    
    for idx, book in enumerate(library, 1):
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {book['read']}")
    print()

# Search for books by title or author
def search_book():
    query = input("Enter title or author to search: ").lower()
    library = load_library()
    results = [book for book in library if query in book['title'].lower() or query in book['author'].lower()]
    
    if not results:
        print("No books found.\n")
        return
    
    for idx, book in enumerate(results, 1):
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {book['read']}")
    print()

# Update details of an existing book
def update_book():
    view_books()
    library = load_library()
    try:
        index = int(input("Enter the number of the book to update: ")) - 1
        if index < 0 or index >= len(library):
            print("Invalid selection.\n")
            return
        
        library[index]['title'] = input(f"New title ({library[index]['title']}): ") or library[index]['title']
        library[index]['author'] = input(f"New author ({library[index]['author']}): ") or library[index]['author']
        library[index]['year'] = input(f"New year ({library[index]['year']}): ") or library[index]['year']
        library[index]['genre'] = input(f"New genre ({library[index]['genre']}): ") or library[index]['genre']
        library[index]['read'] = input(f"Read status ({library[index]['read']}): ") or library[index]['read']
        
        save_library(library)
        print("Book updated successfully!\n")
    except ValueError:
        print("Invalid input.\n")

# Delete a book from the library
def delete_book():
    view_books()
    library = load_library()
    try:
        index = int(input("Enter the number of the book to delete: ")) - 1
        if index < 0 or index >= len(library):
            print("Invalid selection.\n")
            return
        
        removed_book = library.pop(index)
        save_library(library)
        print(f"Deleted: {removed_book['title']} by {removed_book['author']}\n")
    except ValueError:
        print("Invalid input.\n")

# Count the total number of books in the library
def count_books():
    library = load_library()
    print(f"Total books in library: {len(library)}\n")

# List all books by a specific author
def list_books_by_author():
    author_name = input("Enter author name: ").lower()
    library = load_library()
    results = [book for book in library if author_name in book['author'].lower()]
    
    if not results:
        print("No books found by this author.\n")
        return
    
    for idx, book in enumerate(results, 1):
        print(f"{idx}. {book['title']} ({book['year']}) - Genre: {book['genre']} - Read: {book['read']}")
    print()

# Main function to run the menu-based system
def main():
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a Book")
        print("2. View Books")
        print("3. Search for a Book")
        print("4. Update a Book")
        print("5. Delete a Book")
        print("6. Count Books")
        print("7. List Books by Author")
        print("8. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            count_books()
        elif choice == "7":
            list_books_by_author()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()