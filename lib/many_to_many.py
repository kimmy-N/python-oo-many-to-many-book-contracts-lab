class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self.name = name
        Author.all.append(self)

    def __repr__(self):
        return f"Author({self.name})"

    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return [c.book for c in self.contracts()]

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)


class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise Exception("Title must be a non-empty string")
        self.title = title
        Book.all.append(self)

    def __repr__(self):
        return f"Book({self.title})"

    def contracts(self):
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        return [c.author for c in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):

        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")

        if not isinstance(book, Book):
            raise Exception("Book must be a Book instance")

        if not isinstance(date, str) or len(date) == 0:
            raise Exception("Date must be a non-empty string")

        if not isinstance(royalties, (int, float)) or royalties <= 0:
            raise Exception("Royalties must be a positive number")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    def __repr__(self):
        return f"Contract({self.author.name}, {self.book.title}, {self.date}, {self.royalties})"

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]