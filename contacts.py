import sqlite3
import os

try:
    try:
        os.chdir("../")
        os.chdir("../")
        os.chdir("../")
        os.chdir("Documents")
        cwd1 = os.getcwd()

    except:
        os.chdir("../")
        os.chdir("../")
        os.chdir("Documents")
        cwd2 = os.getcwd()
except:
    new_dir = os.mkdir('C:\\Users\\Public\\DB')

# CONNECT TO SQLITE DB & CREATE A TABLE
try:
    try:
        db = sqlite3.connect(cwd1 + "\\" + 'contacts.sqlite')
    except:
        db = sqlite3.connect(cwd2 + "\\" + 'contacts.sqlite')
except:
    db = sqlite3.connect(new_dir + "\\" + 'contacts.sqlite')


# CREATE A TABLE IN DATABASE
cur = db.cursor()
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")


# FUNC FOR ADD A CONTACT
def add_new():
    print("FOLLOW THESE STEPS TO ADD A NEW CONTACT")
    name = input("Enter The Name: ").upper()
    while name.isnumeric() or name == "":
        print("You didn't enter a valid name, try again.")
        name = input("Enter The Name: ")
    try:
        phone = int(input("Enter The Number: "))
    except Exception as e:
        print('invaild number, recheck')
        phone = input("Enter Number: ")

    email = input("Enter Email: ")
    while email.isnumeric() or email == "":
        print("You didn't enter a valid email, try again.")
        email = input("Enter The Name: ")
    cur.execute("INSERT INTO contacts VALUES('{}', {}, '{}')".format(name, phone, email))
    db.commit()
    print("Want To Add Another Contact? (Y for yes, N for no)")
    ans = input().lower()
    if ans == "Y".lower():
        return add_new()
    if ans == "N".lower():
        print("Have A Good Day!")


# DELETE A CONTACT
def delete_one():
    user = input("Enter the name you want to delete: ").upper()
    cur.execute("DELETE FROM contacts WHERE name = '{}'".format(user))
    db.commit()
    print("Deleted contact details of {}".format(user))


# DELETE ALL YOUR CONTACTS
def delete_all():
    user = input("Do you want to delete all your contacts?(Y to yes & N to no) :").lower()
    if user == "y":
        cur.execute("DELETE FROM contacts")
        db.commit()
        print("Successfully deleted all of your contacts")
    else:
        print("Hurray! You saved your contacts")


# PROGRAM FLOW
active = True
while active:
    print("------CONTACT BOOK-------")
    print("1.Add A New Contact")
    print("2.Show Your Contacts")
    print("3.Delete A Contact")
    print("4.Delete All Your Contacts")
    print("Enter The Numbers: ")
    user = int(input())
    if user == 1:
        add_new()
    if user == 2:
        print("-----NAME------------PHONE NUMBER---------------EMAIL-----")
        for name, phone, email in cur.execute("SELECT * FROM contacts"):
            print(name + " ------ " + str(phone) + " ------ " + email)
    if user == 3:
        delete_one()
    if user == 4:
        delete_all()
    break
