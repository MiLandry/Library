#Author, Michael Landry

class Library:
    shelf_count = 1

    def __init__(self, name):
        self.name = name
        self.shelves = []
        self.unshelved_books = []

    def _add_shelf(self, shelf):
        self.shelves.append(shelf)

    def _add_shelfless_book(self, book):
        self.unshelved_books.append(book)

    def _remove_shelfless_book(self, book):
        self.unshelved_books.remove(book)

    def count_shelves(self):
        return len(self.shelves)

    def count_unshelved_books(self):
        return len(self.unshelved_books)

    def count_books_on_shelves(self):
        books = 0
        for shelf in self.shelves:
            books += len(shelf.books)
        return books

    def count_books(self):
        return self.count_books_on_shelves() + self.count_unshelved_books()

    def library_collection_report(self):
        """Prints a report that shows how many books are being held by the library and where they are at."""
        print "%s has %s shelves holding %s books, and also has %s unshelved books, for a total of %s books. \n " \
        % (self.name, str(self.count_shelves()), str(self.count_books_on_shelves()),
        str(self.count_unshelved_books()), str(self.count_books())) 
        for shelf in self.shelves:
            shelf.shelf_collection_report()
            print "" #line break


class Shelf():

    def __init__(self, library):
        self.shelf_number = library.shelf_count
        library.shelf_count += 1
        self.books = []
        self.library = library
        library._add_shelf(self)


    def _add_to_shelf(self, book):
        self.books.append(book)

    def _take_off_shelf(self,book):
        self.books.remove(book)

    def shelf_collection_report(self):
        """Prints a report showing which books are on the shelf."""
        if len(self.books) == 0:
            print "Shelf number %s is empty." % self.shelf_number
            return
        print "Shelf number %s contains the following books:" % self.shelf_number
        for book in self.books:
            book.print_info()


class Book():
    serial_number =  10000001    

    def __init__(self, title, library):
        self.title = title
        self.shelf = None
        self.library = library
        library._add_shelfless_book(self) #update library listing
        self.serial_number = Book.serial_number
        Book.serial_number += 1

    def enshelf(self, shelf):
        """Moves the book onto a shelf.  It will also unshelf the book if it is already shelved."""
        
        #remove the book from its current shelf if it is already shelved
        if self.shelf is not None: 
            self.unshelf()
        # Or remove the book from the library list of unshelved books. 
        else:
            self.library._remove_shelfless_book(self) 
            
        shelf._add_to_shelf(self) #update shelf object
        self.shelf = shelf

    def unshelf(self):
        """Removes the book from its current shelf and adds it to its current library's shelfless inventory."""
        if self.shelf == None:
            print "%s is already unshelved."
            return
        self.shelf._take_off_shelf(self) 
        self.library._add_shelfless_book(self)
        self.shelf = None 

    def print_info(self):
        """ Prints the book title and serial number of the book."""
        print self.title + "; " + "serial number:" + " " + str(self.serial_number)





#testing
library1 = Library("library1")

shelf1 = Shelf(library1)
shelf2 = Shelf(library1)
shelf3 = Shelf(library1)
shelf4 = Shelf(library1)

book1 = Book("The Davinci Code", library1)
book2 = Book("Gone With the Wind", library1)
book3 = Book("Diary of Anne Frank", library1)
book4 = Book("Great Gatsby", library1)
book5 = Book("Gone With the Wind", library1)
book6 = Book("Of Mice and Men", library1)
book7 = Book("Treasure Island", library1)

book1.enshelf(shelf1)
book2.enshelf(shelf2)
book3.enshelf(shelf2)
book3.unshelf()
book3.enshelf(shelf3)
book4.enshelf(shelf2)
book5.enshelf(shelf1)


library1.library_collection_report()
