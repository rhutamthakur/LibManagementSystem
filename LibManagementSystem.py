from pygame import mixer
class Library:
    def createdatabase(cls):
        n=int(input("Enter number of books you want to add:"))
        dict0= {}
        i=0
        while i<n:
            bookname=input(f"Enter book {i+1} name:")
            authorname=input("Enter respective author name:")
            dict0.update({bookname:authorname})
            i=i+1
        print("Database has been created!")
        return dict0

    def addbook(cls,dict1):
        bname=input("Enter name of book:")
        aname=input("Enter author's name:")
        dict1.update({bname:aname})

    def delbook(cls,dict1):
        bname=input("Enter name of book to be deleted:")
        if bname in dict1:
            del dict1[bname]
            print("The book has been deleted")
        else:
            print("The book you wish to delete does not exist!")

    def lendbook(cls,dict1,dict2):
        bname=input("Enter name of book to be lent:")
        if bname in dict1:
            username=input("Enter your name:")
            dict2.update({bname:username})
            del dict1[bname]
            print("Book has been lent!")
        else:
            print("The book you want to lend does not exist! Add it to collection first")

    def returnbook(cls,dict1,dict2):
        rbname=input("Enter name of book to be returned:")
        if rbname in dict2.keys():
            authname=input("Enter author's name:")
            dict1.update({rbname:authname})
            del dict2[rbname]
            print("The book has been returned!")
        else:
            print("The book you wish to return does not exist in the original database."
                  " Please check if you are at the correct library!")

    def editbook(cls,dict1):
        bname=input("Enter book name to be edited:")
        if bname in dict1:
            del dict1[bname]
            dict1.update({input("Enter new name of book:"):input("Enter new author name:")})
            print("The Book data has been updated!")
        else:
            print("The book you wush to edit does not exist in Database!")


class Thakur(Library):
    def heading(cls):
        print("***__THAKUR ONLINE LIBRARIES__***\n\n")

    def lentbklist(cls,dict2):
        if len(dict2)==0:
            print("No books have been borrowed yet!")
        else:
            print(f"The borrowed books are:\n{sorted(dict2.items())}")

    def dispbook(cls,dict1):
        if  len(dict1) == 0:
            print("No books have been added yet!")
        else:
            print(sorted(dict1.items()))


    def FirstMenu(cls):
        print("Select one option as per your requirement:\n1. Administrator\n2. Member\n3. Exit Program\n")

    def menuAdmin(cls):
        print("\n_____MAIN MENU_____\n")
        print("1. Add Book\n2. Delete Book\n3. Display Book Database\n"
              "4. Display Borrowed Book Data\n5. Edit Book Data\n6. Exit Program\n\n")

    def menuMember(cls):
        print("\n_____MAIN MENU_____\n")
        print("1. Lend Book\n2. Display Book Database\n3. Return Book\n4. Exit Program\n\n")


class Employee(Thakur):
    def personalAdminInfo(cls):
        empname=input("Enter your name:")
        empdob=int(input("Enter your date of birth(DD/MM/YYYY):"))
        empid=int(input("Enter your ID(Last three digits):"))
        pw=(str(empdob)+str(empid))
        return pw

    def personalMemberInfo(cls):
        empname=input("Enter your name:")
        empcont=int(input("Enter your contact number(First 5 digits):"))
        pw=str(str(empname)+str(empcont))
        return pw

    def Login(cls,pw):
        keycode=input("\nEnter your password:")
        if pw==keycode:
            return True
        else:
            return False

    def adminMenuMusic(cls,file):
        mixer.init()
        mixer.music.load(file)
        mixer.music.set_volume(10)
        mixer.music.play()

    def MemberMenuMusic(cls,file):
        mixer.init()
        mixer.music.load(file)
        mixer.music.set_volume(10)
        mixer.music.play()

lentbks={}
booklist=[]
Rutz=Employee()
#if __name__=='main':
Rutz.heading()
while(True):
    Rutz.FirstMenu()
    choice=int(input("Enter a choice:"))
    if choice==1:
        key=Rutz.personalAdminInfo()
        if Rutz.Login(key)== True:
            if bool(booklist)!=True:
                print("Library database:")
                booklist=Rutz.createdatabase()
            else:
                Rutz.adminMenuMusic("AdminMusic.mp3")
                while(True):
                    Rutz.menuAdmin()
                    ch=int(input("Enter a choice:"))
                    if ch==1:
                        Rutz.addbook(booklist)
                    elif ch==2:
                        Rutz.delbook(booklist)
                    elif ch==3:
                        Rutz.dispbook(booklist)
                    elif ch==4:
                        Rutz.lentbklist(lentbks)
                    elif ch==5:
                        Rutz.editbook(booklist)
                    elif ch==6:
                        break
                    else:
                        print("Enter a valid choice please!\n")
        else:
            print("Incorrect Password! Try Again!\n")
    elif choice==2:
        key = Rutz.personalMemberInfo()
        if Rutz.Login(key) == True:
            Rutz.MemberMenuMusic()
            while (True):
                Rutz.menuMember("MemberMusic.mp3")
                ch=int(input("Enter a choice="))
                if ch==1:
                    Rutz.lendbook(booklist,lentbks)
                elif ch==2:
                    Rutz.dispbook(booklist)
                elif ch==3:
                    Rutz.returnbook(booklist,lentbks)
                elif ch==4:
                    break
                else:
                    print("Enter a valid choice please!\n")
    elif choice==3:
        print("Thank you for using Thakur Online Library! Have a nice Day!\n")
        break
    else:
        print("Enter a valid choice please!\n")