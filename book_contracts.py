# Step 1: Author class
class Author:
    all = []  # Keep track of all authors

    def __init__(self, name):
        self.name = name
        Author.all.append(self)  # Add this author to the class list

    def __repr__(self):
        return f"Author({self.name})"

    # ----- Many-to-Many Methods -----
    # Return all contracts for this author
    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    # Return all books this author is linked to
    def books(self):
        return [c.book for c in self.contracts()]

    # Return total royalties for this author
    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


# Step 2: Book class
class Book:
    all = []  # Keep track of all books

    def __init__(self, title):
        self.title = title
        Book.all.append(self)  # Add this book to the class list

    def __repr__(self):
        return f"Book({self.title})"

    # ----- Many-to-Many Methods -----
    # Return all contracts for this book
    def contracts(self):
        return [c for c in Contract.all if c.book == self]

    # Return all authors for this book
    def authors(self):
        return [c.author for c in self.contracts()]


# Step 3: Contract class
class Contract:
    all = []  # Keep track of all contracts

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)  # Add to list of all contracts

    def __repr__(self):
        return f"Contract({self.author.name}, {self.book.title}, {self.date}, {self.royalties})"


# ----- TEST CODE -----

# Create authors
author1 = Author("J.K. Rowling")
author2 = Author("Stephen King")

# Create books
book1 = Book("Harry Potter")
book2 = Book("The Shining")

# Create contracts
contract1 = Contract(author1, book1, "2026-02-21", 50)
contract2 = Contract(author2, book2, "2026-02-21", 30)
contract3 = Contract(author2, book1, "2026-02-22", 20)  # Many-to-many connection

# Print authors
print(author1)  # Author(J.K. Rowling)
print(author2)  # Author(Stephen King)
print(Author.all)

# Print books
print(book1)    # Book(Harry Potter)
print(book2)    # Book(The Shining)
print(Book.all)

# Print contracts
print(contract1)
print(contract2)
print(contract3)
print(Contract.all)

# Test many-to-many methods
print(author2.books())         # [Book(The Shining), Book(Harry Potter)]
print(book1.authors())         # [Author(J.K. Rowling), Author(Stephen King)]
print(author2.total_royalties())  # 50 (30 + 20)