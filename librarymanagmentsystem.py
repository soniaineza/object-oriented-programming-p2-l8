class library:
    def __init__(self,list_of_books,name):
        self.booklist=list_of_books
        self.name=name
        self.lenddict={}
    def displaybooks(self):
        print(f"we have the following books in our library {self.name}")
        for book in self.booklist:
            print(book)
    def lendbook(self,user,book):
        if book not in self.booklist:
            print("sorry we don't have that book")
        elif book in self.lenddict:
            print(f"the book is already being used by {self.lenddict[book]}")
        else:
            self.lenddict[book]=user
            print("lender book database has been updated you can take the book now")
    def addbook(self,book):
        self.booklist.append(book)
        print(f"{book} has been added to the booklist")
    def returnbook(self,book):
        if book in self.lenddict:
            del self.lenddict[book]
            print("The book has been returned")
        else:
            print("The book wasn't borrowed from us")
if __name__=='__main__':
    books=library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics','Algorithms by CLRS'], "Let's Upskill")
    username=input("welcome to our library,please enter your name")
    while True:
        print(f"\n hello {username},welcome to {books.name} library please choose an option")
        print("1.displaybooks\n2.lend a book\n3.add a book\n4.return a book\n5.quit")
        userchoice=input("enter your choice")
        if userchoice not in ['1','2','3','4','5']:
            print("please a valid option")
            continue
        if userchoice=='1':
            books.displaybooks()
        elif userchoice=='2':
            book=input("enter the name of the book you want to lend")
            books.lendbook(username,book)
        elif userchoice=='3':
            book=input("enter the name of the book you want to add")
            books.addbook(book)
        elif userchoice=='4':
            book=input("enter the name of the book you want to return")
            books.returnbook(book)
        elif userchoice=='5':
            print(f"Thank you for using the library!,{username}.Goodbye!")
            break


    

        