import csv

class Library:

    def add_book(self):
        book_name = input("Enter book's name: ")
        author = input("Enter book's author: ")
        publication = input("Enter book's publication: ")

        book_info = [{
            'book_name' : book_name,
            'author' : author,
            'publication' : publication
        }]

        with open('books.csv', 'a') as file:
            header = ['book_name', 'author', 'publication']
            writer = csv.DictWriter(file, fieldnames = header)
            writer.writeheader()
            writer.writerows(book_info)

    def show_book(self):
        with open('books.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter = ',')

            for book in reader:
                print(book)

book1 = Library()

print("Choose:")
print("1. Add a book")
print("2. Show books")
choice = int(input("Choice: "))

if choice == 1:
    book1.add_book()
elif choice == 2:
    book1.show_book()