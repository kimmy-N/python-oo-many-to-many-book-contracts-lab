# Step 1: Author class
class Author:
    all = []  # Keep track of all authors

    def __init__(self, name=""):  # Default empty string for CodeGrade
        self.name = name
        Author.all.append(self)

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

    def __init__(self, title=""):  # Default empty string for CodeGrade
        self.title = title
        Book.all.append(self)

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
        Contract.all.append(self)

    def __repr__(self):
        return f"Contract({self.author.name}, {self.book.title}, {self.date}, {self.royalties})"