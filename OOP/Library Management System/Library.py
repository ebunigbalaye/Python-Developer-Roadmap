class Library:
    """Defining the library class that will contain all the books"""
    def __init__(self):
      self.books = []


    def add_book(self,title,author):
       """This method creates a book object from the book class and adds it to the library"""
       book = Book(title,author)
       self.books.append(book)


    def list_books(self):
      """This method lists out the available books in the library"""
      print("------Library Catalogue------")
      for book in self.books:
         if book.is_borrowed == True:
            print(f"{book.title} by {book.author}: Unvailable")
         else:
            print(f"{book.title} by {book.author}: Available")

    
    def check_book(self,title):
       """This method checks if a book is in the Library and returs the index in the list
       and its availability as a list"""
       for i in range(0,len(self.books)):
          if self.books[i].title == title:
             return [True,i]
       return [False]


    def borrow_book(self,title):
       """This method lets the user borrow a book depending on its availability"""
       if self.check_book(title)[0] == True:#Accessing the availability from the return list of the check_book method 
          book_index = self.check_book(title)[1]#Accessing the index from the return list of the check_book method
          if self.books[book_index].is_borrowed == False:
              #This if block checks whether a book has been borrowed or not and borrows it if not 
              self.books[book_index].is_borrowed = True
              print("Book successfully borrowed")
          else:
             print("Book has been borrowed by another person")
       else:print("We do not have that book at this library")
          

    def return_book(self,title):
        """This method resets the is_borrowed attribute for a book being returned"""
        if self.check_book(title)[0] == True:#Accessing the availability from the return list of the check_book method 
          book_index = self.check_book(title)[1]#Accessing the index from the return list of the check_book method
          if self.books[book_index].is_borrowed == True:
             #This if block sets the is_borrowed attribute of the book being returned to 
             #false if found in the list
             self.books[book_index].is_borrowed = False
          else:
             print("This book wasn't borrowed")
        else:
           print("You didn't get this book from us ")

       
        
class Book:
     """Defining the book class that all book objects will inherit from"""
     def __init__(self,title,author):
      self.title = title
      self.author = author
      self.is_borrowed = False
   
   




