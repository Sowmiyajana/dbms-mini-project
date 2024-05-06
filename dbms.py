PROGRAM
import mysql.connector
from datetime import datetime
from time import sleep
def tprint(string):
 for i in range (len(string)):
 print(string[i],end='')
 sleep(0.003)
 print()
# Connect to MySQL database
def connect_to_database():
 try:
 connection = mysql.connector.connect(
 host="localhost",
 user="varun",
 password="admin",
 )
 return connection
 except mysql.connector.Error as error:
 print("Error connecting to MySQL database:", error)
 return None
# Create student table if not exists
def create_student_table(cursor):
 cursor.execute("""CREATE TABLE IF NOT EXISTS students (
 register_number BIGINT PRIMARY KEY,
name VARCHAR(255),
department VARCHAR(50),
section VARCHAR(10),
dob DATE,
blood_group VARCHAR(5),
age INT,
gender ENUM('Male', 'Female', 'Others'),
native_city VARCHAR(100)
 )""")
# Add a new student
def add_student(cursor, connection):
 flag = 0
 register_number = int(input("Enter Register Number (12 digits): "))
 name = input("Enter Name: ").upper()
 department = input("Enter Department: ").upper()
 section = input("Enter Section: ").upper()
 dob_str = input("Enter Date of Birth (dd-mm-yyyy): ")
 
 try:
 # Parse the date string to a datetime object
 dob = datetime.strptime(dob_str, "%d-%m-%Y").date()
 except ValueError:
6
 print("Invalid date format. Please enter date in the format dd-mmyyyy.")
 return
 blood_group = input("Enter Blood Group: ").upper()
 age = int(input("Enter Age: "))
 gender = input("Enter Gender (Male/Female/Others): ").upper()
 native_city = input("Enter Native City: ").upper()
 # Insert into database
 try:
 cursor.execute("""INSERT INTO students 
 (register_number, name, department, section, dob, 
blood_group, age, gender, native_city)
 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
 (register_number, name, department, section, dob,
blood_group, age, gender, native_city))
 connection.commit()
 except:
 print("\nStudent",register_number,"is already exists")
 flag = 1
 cursor.execute("SELECT * FROM students WHERE register_number = %s",
(register_number,))
 student = cursor.fetchone()
 if student:
 tprint("\nStudent Details:")
 tprint("Register Number: "+ str(student[0]))
 tprint("Name: " +student[1])
 tprint("Department: "+ student[2])
 tprint("Section:" + student[3])
 tprint("Date of Birth: "+ str(student[4]))
 tprint("Blood Group: "+ student[5])
 tprint("Age: "+ str(student[6]))
 tprint("Gender: "+ student[7])
 tprint("Native City: "+ student[8])
 print()
 if flag==0:
 print("\nStudent added successfully\n")
# Search for a student by register number
def search_student(cursor):
 register_number = int(input("Enter Register Number to search: "))
 cursor.execute("SELECT * FROM students WHERE register_number = %s",
(register_number,))
 student = cursor.fetchone()
 if student:
 tprint("\nStudent Details:")
 tprint("Register Number: "+ str(student[0]))
 tprint("Name: " +student[1])
 tprint("Department: "+ student[2])
 tprint("Section:" + student[3])
 tprint("Date of Birth: "+ str(student[4]))
 tprint("Blood Group: "+ student[5])
 tprint("Age: "+ str(student[6]))
 tprint("Gender: "+ student[7])
 tprint("Native City: "+ student[8])
 print()
 else:
7
 print("Student",register_number,"not found")
 print()
# Delete a student by register number
def delete_student(cursor, connection):
 register_number = int(input("Enter Register Number to delete: "))
 cursor.execute("DELETE FROM students WHERE register_number = %s",
(register_number,))
 connection.commit()
 print("\nStudent",register_number,"deleted successfully\n")
def main():
 connection = connect_to_database()
 if not connection:
 return
 cursor = connection.cursor()
 cursor.execute("create database IF NOT EXISTS student_management;")
 cursor.execute("use student_management;")
 # Create student table if not exists
 create_student_table(cursor)
 while True:
 tprint("\nStudent Management System")
 tprint("1. Add Student")
 tprint("2. Search Student")
 tprint("3. Delete Student")
 tprint("4. Exit")
 choice = input("Enter your choice: ")
 if choice == '1':
 add_student(cursor, connection)
 elif choice == '2':
 search_student(cursor)
 elif choice == '3':
 delete_student(cursor, connection)
 elif choice == '4':
 break
 else:
 tprint("Invalid choice. Please enter again.")
 cursor.close()
 connection.close()
 tprint("CLOSED")
if __name__ == "__main__":
 main()
8
RESULT
i) ADDS STUDENT DETAILS
ii) SEARCH STUDENT DETAILS
9
iii) DELETE STUDENT DETAILS