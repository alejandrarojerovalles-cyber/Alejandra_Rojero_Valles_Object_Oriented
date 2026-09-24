class library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book registered: '{book.title}'")

    def add_user(self, user):
        self.users.append(user)
        print(f"User registered: '{user.name}'")

    def find_book(self, id_book):
        return next((b for b in self.books if b.id == id_book), None)

    def find_user(self, id_user):
        return next((u for u in self.users if u.id == id_user), None)

    def borrow_book(self, id_user, id_book):
        user_obj = self.find_user(id_user)
        book_obj = self.find_book(id_book)

        if not user_obj:
            print(f"Error: User ID '{id_user}' not found.")
            return False
        if not book_obj:
            print(f"Error: Book ID '{id_book}' not found.")
            return False

        if not book_obj.available:
            print(f"Cannot borrow: '{book_obj.title}' is already checked out!")
            return False

        book_obj.available = False
        user_obj.borrowed_books.append(book_obj)
        print(f"Success: '{user_obj.name}' borrowed '{book_obj.title}'.")
        return True

    def return_book(self, id_user, id_book):
        user_obj = self.find_user(id_user)
        book_obj = self.find_book(id_book)

        if not user_obj or not book_obj:
            print("Error: Invalid user or book ID.")
            return False

        if book_obj not in user_obj.borrowed_books:
            print(f"Error: '{user_obj.name}' does not have '{book_obj.title}' borrowed.")
            return False

        book_obj.available = True
        user_obj.borrowed_books.remove(book_obj)
        print(f"Success: '{book_obj.title}' returned by '{user_obj.name}'.")
        return True

    def show_books(self):
        for book in self.books:
            print(book.show_books_info())

    def show_users(self):
        for user in self.users:
            print(user.show_user())
