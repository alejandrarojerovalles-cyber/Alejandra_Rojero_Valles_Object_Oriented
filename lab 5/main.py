from books import book
from users import user
from library import library

library1 = library()

# Instances matching parameter order: (id, title, author, editorial)
book1 = book("001", "Python for dummies", "Juan Garcia", "Villareal")
book2 = book("002", "Python for dummies 2", "Juan Gabriel", "Penguin")

# Instance matching parameter order: (id, name)
user1 = user("001", "Alejandra Rojero Valles")
user2 = user("002", "Juan Gabriel")

# Add books to the library
library1.add_book(book1)
library1.add_book(book2)

# Add users to the library
library1.add_user(user1)
library1.add_user(user2)

#Display books and users
print("Books in the library:")
library1.show_books()

print("\nUsers in the library:")
library1.show_users()

#Requirements
#1. the system must allow to registers books.
#2. The system must allow to register users.
#3. The system must manage the books borrow process (users).
#4. A book that has already been borrowed cannot be borrowed again.
#5. The system must allow a book to be returned.