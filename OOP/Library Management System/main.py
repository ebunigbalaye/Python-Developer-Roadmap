from Library import Library,Book
digi_lib = Library()
run = True
print("Welcome to the Digital Library")
while run:
        
        print("""
    1. Add a Book
    2. List all Books
    3. Borrow a Book
    4. Return a Book
    5. Exit
              """)
        action = input("Enter the number that corresponds to what you'd like to do on the menu: ")
        if action == '1':
             title = input("Enter the title of the book you would like to add: ")
             author = input("Enter the author of the book: ")
             digi_lib.add_book(title,author)
             print("Book Added Successfully")

        elif action == '2':
             digi_lib.list_books()

        elif action == '3':
             title = input("Enter the title of the book you want to borrow: ")
             digi_lib.borrow_book(title)

        elif action == '4':
            title = input("Enter the title of the book you want to return: ")
            digi_lib.return_book(title)

        else: 
             run = False


       
   