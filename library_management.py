# Library Management System using Dictionary

library = {}  # { isbn: { title, author, year, copies, available } }


def add_book(isbn, title, author, year, copies=1):
    if isbn in library:
        library[isbn]["copies"] += copies
        library[isbn]["available"] += copies
        print(f"Updated '{title}' — total copies: {library[isbn]['copies']}")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "year": year,
            "copies": copies,
            "available": copies,
        }
        print(f"Added '{title}' by {author}")


def remove_book(isbn):
    if isbn not in library:
        print("Book not found.")
        return
    print(f"Removed '{library[isbn]['title']}' from library.")
    del library[isbn]


def issue_book(isbn, borrower):
    if isbn not in library:
        print("Book not found.")
        return
    book = library[isbn]
    if book["available"] == 0:
        print(f"Sorry, '{book['title']}' is currently unavailable.")
        return
    book["available"] -= 1
    book.setdefault("borrowers", []).append(borrower)
    print(f"'{book['title']}' issued to {borrower}. Copies left: {book['available']}")


def return_book(isbn, borrower):
    if isbn not in library:
        print("Book not found.")
        return
    book = library[isbn]
    borrowers = book.get("borrowers", [])
    if borrower not in borrowers:
        print(f"{borrower} has no record of borrowing this book.")
        return
    borrowers.remove(borrower)
    book["available"] += 1
    print(f"'{book['title']}' returned by {borrower}. Copies available: {book['available']}")


def search_book(keyword):
    keyword = keyword.lower()
    results = [
        b for b in library.values()
        if keyword in b["title"].lower() or keyword in b["author"].lower()
    ]
    if not results:
        print("No books found.")
        return
    print(f"\n{'─'*55}")
    for b in results:
        print(f"  Title   : {b['title']}")
        print(f"  Author  : {b['author']}")
        print(f"  Year    : {b['year']}")
        print(f"  Available: {b['available']} / {b['copies']}")
        print(f"{'─'*55}")


def display_all():
    if not library:
        print("Library is empty.")
        return
    print(f"\n{'═'*60}")
    print(f"{'ISBN':<15} {'Title':<25} {'Author':<15} {'Avail'}")
    print(f"{'─'*60}")
    for isbn, b in library.items():
        print(f"{isbn:<15} {b['title']:<25} {b['author']:<15} {b['available']}/{b['copies']}")
    print(f"{'═'*60}")


def menu():
    options = {
        "1": "Add Book",
        "2": "Remove Book",
        "3": "Issue Book",
        "4": "Return Book",
        "5": "Search Book",
        "6": "Display All Books",
        "7": "Exit",
    }
    while True:
        print("\n===== Library Management System =====")
        for key, val in options.items():
            print(f"  {key}. {val}")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            isbn   = input("ISBN: ").strip()
            title  = input("Title: ").strip()
            author = input("Author: ").strip()
            year   = input("Year: ").strip()
            copies = int(input("Number of copies: ").strip() or 1)
            add_book(isbn, title, author, year, copies)

        elif choice == "2":
            isbn = input("ISBN to remove: ").strip()
            remove_book(isbn)

        elif choice == "3":
            isbn     = input("ISBN: ").strip()
            borrower = input("Borrower name: ").strip()
            issue_book(isbn, borrower)

        elif choice == "4":
            isbn     = input("ISBN: ").strip()
            borrower = input("Borrower name: ").strip()
            return_book(isbn, borrower)

        elif choice == "5":
            keyword = input("Search by title or author: ").strip()
            search_book(keyword)

        elif choice == "6":
            display_all()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


# ── Sample data for quick testing ──────────────────────────────
if __name__ == "__main__":
    add_book("978-0-06-112008-4", "To Kill a Mockingbird", "Harper Lee",    1960, 3)
    add_book("978-0-7432-7356-5", "1984",                  "George Orwell", 1949, 2)
    add_book("978-0-7432-7357-2", "The Great Gatsby",      "F. Scott Fitzgerald", 1925, 2)
    menu()
