# Name: Jamar Hill
# Date: 4/19/2021
# Description: CS 162 Project 3

# import calender module. Could not get to work?????

class LibraryItem:
    checked_out_by = None
    requested_by = None
    date_checked_out = None  # Should we import date? Assuming "primative" means no.

    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = title  #Movie, Albums, Books may share a "title"
        self._location = "ON_SHELF" # CHECKED OUT OR ON HOLD SHELF
        self._checked_out_by = None # No default location
        self._requested_by = None #No default member request
        self._date_checked_out = 0 #Check out date will require code to count days checked out

    def get_library_item_id(self): #Retrieves library item
        return self._library_item_id
    def set_library_item_id(self, library_item_id): #Inputs library item
        self._library_item_id = library_item_id
    def get_title(self): #Retrieves Title
        return self._title
    def set_title(self, title): #Inputs Title
        self._title =title
    def get_location(self): #Retrieves Location
        return self._location
    def set_location(self,location): #Inputs Location
        self._location = location
    def get_checked_out_by(self): #Retrieves Member that checks out item
        return self._checked_out_by
    def set_checked_out_by(self,name): #Inputs member that checks out item
        self._checked_out_by = name
    def get_requested_by(self): #Retrieves Member that requests item
        return self.requested_by
    def set_requested_by(self, name): #Inputs member that requests item
        self.requested_by = name
    def get_date_checked_out(self): #Retrieves date checked out
        return self._date_checked_out
    def set_date_checked_out(self,date): #Inputs date checked out
        self._date_checked_out=date

class Book(LibraryItem):
    def __init__(self, library_item_id, title, author): #initiates attributes of the Book object
        super().__init__(library_item_id,title) #Retrieves Library_item_id and title from library object
        self._author = author #initiate author as an attribute
    def get_author(self): #Retrieves Author
        return self._author
    def set_author(self,author): #Inputs Author
        self.author = author
    def get_checkout_length(self): #Retieves the amount of time a Book object can be checked out
        return 21 #Will this need a negative counter

class Album(LibraryItem):
    def __init__(self, library_item_id, title, artist): #Initiate attributes of the Album object
        super().__init__(library_item_id, title) #Borrow attributes Library_item_id and title from Library class
        self._artist = artist #Initiate artist as an attribute
    def get_artist(self): #Retrieves Artist
        return self._artist
    def set_artist(self,artist): #Inputs Artist
        self._artist = artist
    def get_checkout_length(self): #Retieves the amount of time a Album object can be checked out
        return 14 #Will this need a negative counter

class Movie(LibraryItem):
    def __init__(self,library_item_id, title, director): #Initiate attributes of the Movie object
        super().__init__(library_item_id, title) #Borrow attributes Library_item_id and title from Library class
        self._director = director #Initiate artist as an attribute
    def get_director(self): #Retrieves Director
        return self._director
    def set_director(self, direct): #Inputs Director
        self.director = director
    def get_check_out_length(self): #Retieves the amount of time a Album object can be checked out
        return 7 #Will this need a negative counter

class Patron:
    def __init__(self, patron_id, name): #Initiates Patron_id, and name as attributes
        self._patron_id = patron_id #Establishes a call for partron_id
        self._name = name #Establishes a call for name
        self._checked_out_items = [] #Establishes a call for Checked_out_items
        self._fine_amount = "${}",(0.00) #Establishes a call fine_amount
    def add_library_item(self, library_item): #Adds item to library appending order
        self._checked_out_item.append(library_item)
    def remove_library_item(self, library_item): #Removes an item attached to a patron
        self._checked_out_item.remove(library_item)
    def amend_fine(self, amount): #Changes fine amount by adding to the existing amount
        #self._fine_amount = set._fine_amount + amount
        self.set_fine_amount(self.get_fine_amount() + amount)

    def get_patron_id(self): #Retrieves patron_id
        return self._patron_id
    def set_patron_id(self, patron_id): #Inputs Patron_id
        self._paton_id = patron_id
    def get_name(self): #Retrieves name
        return self._name
    def set_name(self, name): #Inputs name
        self._name = name
    def get_fine_amount(self): #Retrieves fine amount
        return self._fine_amount
    def set_fine_amount(self, fine_amount): #Inputs fine-amount
            self._fine_amount = fine_amount

class Library:
    def __init__(self): #Initiates library
        self._holdings = [] #Creates a list of library holdings
        self._members = [] #Creates a list of library members
        self._current_date = 0 #establishes current date with a zero value

    def get_current_date(self): #Retrieves current date
        return self._current_date
    def set_current_date(self, todays_date): #Sets current date as today's date
        self._current_date = todays_date
    def add_library_item(self, library_item): #adds library item to holdings
        self._holdings.append(library_item)
    def add_patron(self, patron): #adds additional patron to members
        self._members.append(patron) #attach patron to member list
    def lookup_library_item_from_id(self, library_item_id):
        ret = None #Variable ret determines if the item has been returned
        for library_item in self._holdings:
            if library_item.get_library_item_id() == library_item_id: #If statement: if library item is in holdings
                break #Stop runnning code
            return ret #Item has been returned

    def check_out_library_item(self, patron_id, library_item_id):
        library_item = self.lookup_library_item_from_id(library_item_id) #establish variable for lookin gup item
        patron = self.lookup_library_item_from_id(patron_id) #establish variable for looking up patron
        if library_item == None: #If statement: if no library item is found
            print("item not found")
        elif patron == None: #If statement: if no patron is found
            print("item not found")
        else:
            if library_item.get_location() == "CHECKED_OUT": #If statement: if no library item is checked out
                return "item already checked out"

            if (library_item.getlocation()== "ON HOLD SHELF" #If statement: if no library item is on hold shelf
            and library_item.get_requested_by != patron #and has not been requested by the parton
            ):
                return("item on hold by other patron")

            """Defines the checkout process by attaching checkout to parton, date to patron, and location to patron"""
            library_item.set_checked_out_by(patron)
            library_item.set_date_checked_out(self._current_date)
            library_item.set_location("CHECKED_OUT")

            if library_item.get_requested_by() == patron_id: #If statement: if patron is matched up to library_item...
                library_item.set_requested_by(None)
                patron.add_library_item(self, library_item) #Library item is attached to patron
        print("check out successful")

    def return_library_item(self,library_item_id): #Defines action to return library item
        library_item_search = self.get_library_item(library_item_id) #establishes variable to search for library item
        patron_id_search = self.get_patron(library_item_id) #establish variable to search for patron
        if library_item_search == None: #Creates response for if a library item cannot be found
            print ("item not found")
        elif patron_id_search == None: ##Creates response for if a patron cannot be found
            print("item not found")
        else:
            if (library_item_search.get_request_by != None): #If statement: if library_item has been requested by someone.
                library_item_search.set_location("ON_HOLD_SHELF")
            else:
                library_item_search.set_location("ON_SHELF") #Creates the assumption that the item is on the shelf
                library_item_search.set_checked_out(None)
                print("return successful") #prints the assumption the the item has been returned successfully


    def request_library_item(self, patron_id, library_item_id):
        library_item_search = self.check_out_library_item(library_item_id) # There is an error on this line that I cannot resolve
        patron_id_search = self.get_patron(patron_id) #established variable to define patron
        if library_item_search == None: #If statement: if library item is not founds...
            print("item not found")
        elif patron_id_search == None:
            print("item not found") #If statement: if patron_id is not founds...
        else:
            if (library_item_search.get_location () == "ON_HOLD_SHELF"): #If statement: if library item is on hold...
                #by another patron
                print("item already on hold")
            else:
                library_item_search.set_requested_by(patron_id)#Creates a default for item to be held by current patron
        if (library_item_search.get_location () == "ON_SHELF"): #If statement: if library item is on the shelf
            library_item_search.set.location("ON_HOLD_SHELF")
    print("requested successful") #Creates defult response to notify that library_item is available for request

    def increment_current_date(self):
        self._current_date = self.current_date + 1 #establishes a variable that incrementaly adds a day to checkout.
    def pay_fine(self, patron_id, fine_total): #Establishes a patron with a fine total
        patron = self.get_patron(patron_id)
        fine = self.get_fine_amount(fine_total)
        if patron is None: ##If patron cannot be found
            print ("patron not found")
        patron.amend_fine(fine_total) #If patron is found and has a fine total
        print("payment successful")
        if (patron != None
        and (fine >= 0)
        ):
            print(format.get_fine_amount(fine_total) + .1) #Print fine plus $0.10

"""Copied from assignment rubic"""
b1 = Book("345", "Phantom Tollbooth", "Juster")
a1 = Album("456", "...And His Orchestra", "The Fastbacks")
m1 = Movie("567", "Laputa", "Miyazaki")
print(b1.get_author())
print(a1.get_artist())
print(m1.get_director())

p1 = Patron("abc", "Felicity")
p2 = Patron("bcd", "Waldo")

lib = Library()
lib.add_library_item(b1)
lib.add_library_item(a1)
lib.add_patron(p1)
lib.add_patron(p2)

lib.check_out_library_item("bcd", "456")
loc = a1.get_location()
lib.request_library_item("abc", "456")
for i in range(57):
    lib.increment_current_date()  # 57 days pass
p2_fine = p2.get_fine_amount()
lib.pay_fine("bcd", p2_fine)
lib.return_library_item("456")