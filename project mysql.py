import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='supraja@2110',       
            database='testPython'  
        )

        # Create table if not exists
        query = '''CREATE TABLE IF NOT EXISTS user(
                    userid INT PRIMARY KEY,
                    username VARCHAR(100),
                    phone BIGINT)'''
        cur = self.con.cursor()
        cur.execute(query)
        print("Table 'user' ready.")

    # Insert user
    def insert_user(self, userid, username, phone):
        query = "INSERT INTO user(userid, username, phone) VALUES (%s, %s, %s)"
        cur = self.con.cursor()
        try:
            cur.execute(query, (userid, username, phone))
            self.con.commit()
            print("User saved to table.")
        except connector.IntegrityError:
            print("Error: UserID already exists!")

    # Fetch all users
    def fetch_data(self):
        query = "SELECT * FROM user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User ID:", row[0])
            print("User Name:", row[1])
            print("Phone No:", row[2])
            print("-" * 30)

    # Delete user
    def delete_row(self, userid):
        query = "DELETE FROM user WHERE userid = %s"
        cur = self.con.cursor()
        cur.execute(query, (userid,))
        self.con.commit()
        print("User deleted (if existed).")

    # Update user
    def update_user(self, userid, newName, newPhone):
        query = "UPDATE user SET username=%s, phone=%s WHERE userid=%s"
        cur = self.con.cursor()
        cur.execute(query, (newName, newPhone, userid))
        self.con.commit()
        print("User updated (if existed).")


def main():
    db = DBHelper()
    while True:
        print("\n====== WELCOME ======")
        print("PRESS 1 TO INSERT NEW USER")
        print("PRESS 2 TO DISPLAY ALL USERS")
        print("PRESS 3 TO DELETE USER")
        print("PRESS 4 TO UPDATE USER")
        print("PRESS 5 TO EXIT PROGRAM")
        print("=====================")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                uid = int(input("Enter User ID: "))
                name = input("Enter Username: ")
                phone = int(input("Enter Phone: "))
                db.insert_user(uid, name, phone)

            elif choice == 2:
                db.fetch_data()

            elif choice == 3:
                uid = int(input("Enter User ID to delete: "))
                db.delete_row(uid)

            elif choice == 4:
                uid = int(input("Enter User ID to update: "))
                newName = input("Enter new Username: ")
                newPhone = int(input("Enter new Phone: "))
                db.update_user(uid, newName, newPhone)

            elif choice == 5:
                print("Exiting program. Bye!")
                break

            else:
                print("Invalid Input... Try again.")

        except Exception as e:
            print("Error:", e)
            print("Invalid Input... Try again.")


if __name__ == "__main__":
    main()
