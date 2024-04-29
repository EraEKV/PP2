import psycopg2
import csv
from config import password, host, user, database


try:
    connection = psycopg2.connect(
        host = host,
        database = database,
        user = user,
        password = password
    )
    
    connection.autocommit = True  # for autocommiting all changes  
    
    curs = connection.cursor()

    with connection.cursor() as curs:
        curs.execute(
            "SELECT version();"
        )
        print(f"server version: {curs.fetchone()}")
    
    
    # Creating a table users with properties id, username, score and pos 
    with connection.cursor() as curs:
        curs.execute(
            """CREATE TABLE users(
                    id SERIAL PRIMARY KEY,
                    firstname varchar(50) NOT NULL,
                    lastname varchar(50) NOT NULL,
                    phone varchar(12) NOT NULL
                )"""
        )
        connection.commit()
        print("[INFO] Table created")
    
    
    with connection.cursor() as curs:
        # curs.execute("DELETE FROM users WHERE username = 'username'")
        curs.execute("SELECT * FROM users")
        print(curs.fetchall())
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
# finally:
#     if connection:
#         # connection.close()
#         # print("[INFO] PostreSQL connection closed")



def existing_check(lname, phone) -> bool:
    curs = connection.cursor()
    curs.execute(' SELECT * FROM users WHERE lastname = %s AND phone = %s ', (lname, phone))
    return True if curs.fetchall() else False

def inputData() -> None:
    print("Hello! Please, carefully input your data by following steps")
    fname = input("Firstname: ").strip()
    lname = input("Lastname: ").strip()
    phone = input("Phone number: ").strip()
    if existing_check(fname, lname, phone):
        curs.execute(' INSERT INTO users ("firstname", "lastname", "phone") VALUES(%s, %s, %s); ' , (fname, lname, phone))
    else:
        print("""User already exists. Do you want to change data?\n\
            [1] Yes\n\
            [2] No""")
        choice = input()
        if choice == "1": update_contact()
        

def importFromCSV() -> None:
    with open("info.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            lname, fname, phone = row
            if not existing_check(lname, phone):
                curs.execute(' INSERT INTO users ("firstname", "lastname", "phone") VALUES( %s, %s, %s); ', (fname, lname, phone))


def update_contact() -> bool:
    print("Enter your lastname and latest phone number: ")
    lname = input().strip()
    phone = input().strip()
    if existing_check(lname, phone):
        # print("exist\n", check)
        print("Enter your new phone number: ")
        phone = input("Your new phone: ")
        curs.execute(' UPDATE users SET "phone" = %s WHERE "lastname" = %s ', (phone, lname))
        return True
    else:
        return False
    # curs.execute(' UPDATE users SET "phone" = %s WHERE "name" = %s ', (phone, name))

def queryData() -> None:
    print("""Select filter to querying\n\
            [1] id, name, phone\n\
            [2] Name, phone\n\
            [3] Name\n\
            [4] Phone\n\
            [5] Exit""")
    filter = input("Your choice: ")
    if filter != "5":
        curs.execute(' SELECT * FROM users ')
        data = curs.fetchall()
        with open("queredData.txt", "w") as file:
            if filter == "1":
                for row in data:
                    file.write(f"id: {str(row[0])}, name: {str(row[1])} {str(row[2])[0]}., phone: {str(row[3])}\n")
            elif filter == "2":
                for row in data:
                    file.write(f"Name: {str(row[1])} {str(row[2])[0]}., phone: {str(row[3])}\n")
            elif filter == "3":
                for row in data:
                    file.write(f"Name: {str(row[1])} {str(row[2])[0]}.\n")
            elif filter == "4":
                for row in data:
                    file.write(f"Phone: {str(row[3])}\n")
        # path = "queredData.txt"
        # f = open(path, "w")
        # for row in data:
        #     f.write("Name: " + str(row[1]) + "\n" + "Number: " + str(row[2]) + "\n")
        # f.close()

def deleteData() -> None:
    print("Enter lastname that you want to delete, then input phone number:")
    lname = input("Lastname: ").strip()
    phone = input("Phone number: ").strip()
    print(f"""Are you sure to delete user {lname} from database?\n\
        [1] - Yes\n\
        [2] - No""")
    sure = input()
    if sure == "1":
        print("Initializing deleting...")
        try:
            curs.execute(f''' DELETE FROM users WHERE "lastname" = '{lname}' AND "phone" = '{phone}' ''')
            print(f"User {lname} deleted successfully!")
        except Exception as _ex:
            print("Error:", _ex)
        
        

def deleteAllData() -> None:
    sure = input("Are you absolutely shure about that?: ")
    if sure == "1":
        print("Initializing deleting...")
        curs.execute(' DELETE FROM users  ')
        print("All data successfully deleted!")
    else:
        print("Data not deleted")


done = False
while not done:
    curs = connection.cursor()
    curs.execute(' SELECT * FROM users ')
    print(curs.fetchall())
    print("What do you want to do?\n\
          [1] Input data from console\n\
          [2] Upload form csv file\n\
          [3] Update existing contact\n\
          [4] Query data from the table\n\
          [5] Delete data from table by person name\n\
          [6] Delete all data from table\n\
          [7] Exit")
    x = int(input("Enter number 1-7: "))
    if(x == 1):
        inputData()
    elif(x == 2):
        importFromCSV()
    elif(x == 3):
        if not update_contact():
            update_contact()
            
    elif(x == 4):
        queryData()
    elif(x == 5):
        deleteData()
    elif(x == 6):
        deleteAllData()
    else:
        done = True
    
curs.close()
connection.close()