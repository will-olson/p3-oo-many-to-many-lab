class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def contracts(self):
        return self._contracts

    def books(self):
        return list(set(contract.book for contract in self._contracts))

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []

    def contracts(self):
        return self._contracts

    def authors(self):
        return list(set(contract.author for contract in self._contracts))


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be of type Author")
        if not isinstance(book, Book):
            raise Exception("book must be of type Book")
        if not isinstance(date, str):
            raise Exception("date must be of type str")
        if not isinstance(royalties, int):
            raise Exception("royalties must be of type int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        author._contracts.append(self)
        book._contracts.append(self)
        Contract.all.append(self)

    @staticmethod
    def contracts_by_date(date):
        return [contract for contract in Contract.all if contract.date == date]