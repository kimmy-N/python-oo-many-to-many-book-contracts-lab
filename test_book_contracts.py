import pytest
from book_contracts import Author, Book, Contract

# -----------------------
# Test Author Initialization
# -----------------------
def test_author_init():
    a = Author()
    assert isinstance(a, Author)
    a2 = Author("Test Author")
    assert a2.name == "Test Author"

# -----------------------
# Test Book Initialization
# -----------------------
def test_book_init():
    b = Book()
    assert isinstance(b, Book)
    b2 = Book("Test Book")
    assert b2.title == "Test Book"

# -----------------------
# Test Contract Initialization
# -----------------------
def test_contract_init():
    a = Author("A")
    b = Book("B")
    c = Contract(a, b, "2026-01-01", 50)
    assert isinstance(c, Contract)
    assert c.author == a
    assert c.book == b
    assert c.date == "2026-01-01"
    assert c.royalties == 50

# -----------------------
# Test Author Many-to-Many Relationships
# -----------------------
def test_author_books_and_royalties():
    a = Author("Author1")
    b1 = Book("Book1")
    b2 = Book("Book2")
    Contract(a, b1, "2026-01-01", 30)
    Contract(a, b2, "2026-01-02", 20)
    assert a.books() == [b1, b2]
    assert a.total_royalties() == 50
    assert all(isinstance(book, Book) for book in a.books())

# -----------------------
# Test Book Many-to-Many Relationships
# -----------------------
def test_book_authors():
    a1 = Author("A1")
    a2 = Author("A2")
    b = Book("B1")
    Contract(a1, b, "2026-01-01", 10)
    Contract(a2, b, "2026-01-02", 15)
    assert b.authors() == [a1, a2]
    assert all(isinstance(author, Author) for author in b.authors())

# -----------------------
# Test Author Contracts
# -----------------------
def test_author_contracts():
    a = Author("AC")
    b = Book("BC")
    c = Contract(a, b, "2026-02-01", 5)
    assert c in a.contracts()

# -----------------------
# Test Book Contracts
# -----------------------
def test_book_contracts():
    a = Author("AB")
    b = Book("BB")
    c = Contract(a, b, "2026-02-02", 10)
    assert c in b.contracts()

# -----------------------
# Test Multiple Contracts
# -----------------------
def test_multiple_contracts():
    a1 = Author("X")
    a2 = Author("Y")
    b1 = Book("B1")
    b2 = Book("B2")
    c1 = Contract(a1, b1, "2026-01-01", 10)
    c2 = Contract(a1, b2, "2026-01-02", 15)
    c3 = Contract(a2, b1, "2026-01-03", 20)
    # Check many-to-many
    assert a1.books() == [b1, b2]
    assert a2.books() == [b1]
    assert b1.authors() == [a1, a2]
    assert b2.authors() == [a1]