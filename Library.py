# Name: Jamar Hill
# Date: 4/19/2021
# Description: CS 162 Project 3

# import calender module. Could not get to work?????

class LibraryItem():
    checked_out_by = None
    requested_by = None
    date_checked_out =None # Should we import date?

    def __init__(self, library_item_id, title):
       self._library_item_id = library_item_id  #library_item_id_code is the library id code
       self._title = title #Cannot assume to be unique
       self._location = "ON_SHELF"
       self._checked_out_by = None
       self._requested_by = None
       self._date_checked_out = 0

    def get_library_item_id(self):
        return self._library_item_id
    def set_library_item_id(self, library_item_id):
        self._library_item_id = library_item_id
    def get_title(self):
        return self._title
    def set_title(self, title):
        self._title =title
    def get_location(self):
        return self._location
    def set_location(self,location):
        self._location = location
    def get_checked_out_by(self):
        return self._checked_out_by
    def set_checked_out_by(self,name):
        self._checked_out_by = name
    def get_requested_by(self):
        return self.requested_by
    def set_requested_by(self, name):
        self.requested_by = name
    def get_date_checked_out(self):
        return self._date_checked_out
    def set_date_checked_out(self,date):
        self._date_checked_out=date

class Book(LibraryItem):
    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id,title)
        self._author = author
    def get_author(self):
        return self._author
    def set_author(self,author):
        self.author = author
    def get_checkout_length(self):
        return 21 #Will this need a negative counter

class Album(LibraryItem):
    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = artist
    def get_artist(self):
        return self._artist
    def set_artist(self,artist):
        self._artist = artist
    def get_checkout_length(self):
        return

class Movie(LibraryItem):
    def __init__(self,library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = director
    def get_director(self):
        return self._director
    def set_director(self, direct):
        self.director = direct
    def get_check_out_length(self):
        return 7

class Patron:
    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0.00
    def add_library_item(self, library_item):
        self._checked_out_item.append(library_item)
    def remove_library_item(self, library_item):
        self._checked_out_item.remove(library_item)
    def amend_fine(self, amount):
        #self._fine_amount = set._fine_amount + amount
        self.set_fine_amount(self.get_fine_amount() + amount)

    def get_patron_id(self):
        return self._patron_id
    def set_patron_id(self, patron_id):
        self._paton_id = patron_id
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def get_fine_amount(self):
        return self._fine_amount
    def set_fine_amount(self, fine_amount):
            self._fine_amount = fine_amount

class Library:
    def __init__(self):
        self._holdings = []
        self._members = []
        self._current_date = 0

    def get_current_date(self):
        return self._current_date
    def set_current_date(self, day):
        self._current_date = day
    def add_library_item(self, library_item):
        self._holdings.append(library_item)
    def add_patron(self, patron):
        self._members.append(patron) #Consider changing the variable
    def get_library_item(self,library_item):
        for x in self._holdings: #Consider changing variable
            if library_item == self._holdings:
                return x
            else:
                return None
    def get_patron(self,patron_name): #Consider CHanging Variable
        for x in self._members:
            if patron_name == x.get_patron_id():
                return x
            else:
                return None

    def check_out_library_item(self, patron_id, library_item_id):
        library_item = self.get_library_item(library_item_id)
        patron_id = self.get_patron(patron_id)
        if library_item == None:
            print("item not found")
        elif patron_id == None:
            print("item not found")

        if library_item == "CHECKED_OUT":
            return "item already checked out"

        if library_item == "ON HOLD SHELF" and library_item.get_requested_by != patron_id:
            return("item on hold by other patron")

        library_item.set_checked_out_by(patron_id)
        library_item.set_date_checked_out(self._current_date)
        library_item.set_location("CHECKED_OUT")

        if library_item.get_requested_by() == patron_id:
            library_item.set_requested_by(None)

        patron_id.add_library_item(self, patron_id)
        print("check out successful")

        def return_library_item(self,library_item_id):
            library_item_search = self.get_library_item(library_item_id)
            patron_id_search = self.get_patron(library_item_id)
            if library_item_search == None:
                print ("item not found")
            elif patron_id_search == None:
                print("item not found")
            else:
                if (library_item_search.get_request_by != None):
                    library_item_search.set_location("ON_HOLD_SHELF")
                else:
                    library_item_search.set_location("ON_SHELF")
                    library_item_search.set_checked_out(None)
                print("return successful")


def request_library_item(self, patron_id, library_item_id):
    library_item_search = self.get_library_item(library_item_id)
    patron_id_search = self.get_patron(library_item_id)
    if library_item_search == None:
        print("item not found")
    elif patron_id_search == None:
        print("item not found")
    else:
        if (library_item_search.get_location () == "ON_HOLD_SHELF"):
            print("item already on hold")
        else:
            library_item_search.set_requested_by(patron_id)
        if (library_item_search.get_location () == "ON_SHELF"):
            library_item_search.set.location("ON_HOLD_SHELF")
    print("requested successful")

def increment_current_date(self):
    self._current_dae = self.current_date + 1 # Change to match tutors adjustment
def pay_fine(self, patron_id, fine_total):
    patron = self.get_patron(patron_id)
    if patron in None:
        print ("patron not found")
        patron.amend_fine(fine_total)
        print("payment successful")


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