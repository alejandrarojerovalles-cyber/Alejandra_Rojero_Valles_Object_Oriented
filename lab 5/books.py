class book:
    def __init__(self, id_book, title, author, editorial):
        self.id = id_book
        self.title = title
        self.author = author
        self.editorial = editorial
        self.available = True

    def show_books_info(self):
        return f"{self.id} - {self.title} - {self.author}"