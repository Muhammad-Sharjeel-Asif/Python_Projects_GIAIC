def hello():
    print("""Welcome to your Personal Library Manager!
1. Add a book  
2. Remove a book  
3. Search for a book  
4. Display all books  
5. Display statistics  
6. Exit
""")

books = [
    {"book_title": "Python", "author_name": "John", "year": 1999, "genre": "Fiction", "read": False},
    {"book_title": "The Great Gatsby", "author_name": "F. Scott Fitzgerald", "year": 1925, "genre": "Fiction", "read": True},
    ]

while True:
    hello()
    user_input = input("Enter your choice: ")
    
        # Adding books
    if user_input == '1':
        while True:
            book_title = input("Enter the book title: ")
            author_name = input("Enter the author name: ")
            publication_year = int(input("Enter the publication year: "))
            genre = input("Enter the genre: ")
            read = input("Have you read this book? (yes/no) ").strip().lower()
            if read in ["yes", "y", "1", "true"]:
                read = True
            elif read in ["no", "n", "0", "false"]:
                read = False
            else:
                read = None
                print("Invalid input. Please enter 'yes' or 'no'.")

            book_data = {"book_title": book_title, "author_name": author_name, "publication_year": publication_year, "genre": genre, "read": read}

            books.append(book_data)
            print("Book added successfully!\n")

            more_books = input("Do you want to add more books: (yes/no) \n").strip().lower()
    
            if more_books in ["no", "n", "0", "false"]:
                print(f'"{book_data["book_title"]}" has been added to your library.\n')
                break
            

    # Removing books
    elif user_input == '2':
        remove_book = input("Enter the book title to remove: ")
        for book in books:
            if book["book_title"] == remove_book:
                books.remove(book)
                print(f'"{book["book_title"]}" removed successfully!')
                break
            else:
                print("Book not found")
    
    # Searching the book
    elif user_input == '3':
        print("""Search by:
1. Title  
2. Author
""")
        search_by = input("Enter your choice: ")

        if search_by == "1":
            book_title = input("Enter the title: ")
            for index, book in enumerate(books):
                found_book = next((book for book in books if book["book_title"] == book_title), None)
                if found_book:
                    print(f"{index-1}. {found_book["book_title"]} by {found_book["author_name"]}")
                else:
                    print("Book not found")

        elif search_by == "2":
            author_name = input("Enter the author name: ")
            for book in books:
                found_book = next((book for book in books if book["author_name"] == author_name), None)
                if found_book:
                    print(f"{found_book["book_title"]} by {found_book["author_name"]}")
                else:
                    print("Book not found")
    
        else:
            print("Invalid choice")

    # Displaying the books
    elif user_input == "4":
        print("Your Library:")
        for index, book in enumerate(books):
            print(f"{index+1}. {book["book_title"]} by {book["author_name"]} ({book["year"]}) - {book["genre"]} - {book["read"]}")

    # Displaying Statistics:
    elif user_input == "5":
        read = 0
        for book in books:
            if book["read"] == True:
                read += 1
        percentage = (read / len(books)) * 100
        print(f"""Total books: {len(books)}
Percentage read: {percentage}% """)

    elif user_input == '6':
        print("Library saved to file. Goodbye!")
        break    