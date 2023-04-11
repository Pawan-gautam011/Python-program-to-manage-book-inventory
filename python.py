# ISBM= (INTERNATIONAL STANDARD BOOK NUMBER)
library_books = []

while True:
    print("Library Inventory Management System")
    print("1.Add a new book")
    print("2.Remove a book")
    print("3.Search for book")
    print("4.List all books")
    print("5.Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        library_books.append({"title": title, "author": author, "isbn": isbn})
        print(f"{title} by {author} has been added to the library inventory.")

    elif choice == 2:
        ISBN= input("Enter book ISBN: ")
        for book in library_books:
            if book["isbn"] == isbn:
                library_books.remove(book)
                print(f"{book['title']} by {book['author']} has been removed from the library inventory.")
                break
        else:
            print("No book with that ISBN was found in the library inventory.")

    elif choice == 3:
        search_term = input("Enter search term: ")
        results = []
        for book in library_books:
            if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower() or search_term.lower() in book["isbn"].lower():
                results.append(book)
            
        if results:
            print(f"Search results for '{search_term}':")
            for book in results:
                print(f"- {book['title']} by {book['author']} (ISBN: {book['isbn']})")
        else:
            print(f"No results found for '{search_term}'.")

    elif choice == 4:
        print("Library inventory:")
        for book in library_books:
            print(f"- {book['title']} by {book['author']} (ISBN: {book['isbn']})")

    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid.3 Please enter a number between 1 and 5.")
