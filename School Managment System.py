# School Management System
print("Your user_name is dua")
print("Your password is 1122") 


class student():
     def __init__(self, name, age, Grade):
      self.name = name
      self.age = age
      self.Grade = Grade

class teacher():
     def __init__(self, name, subject, salary):
      self.name = name
      self.subject = subject
      self.salary = salary


students = []
teachers = []


def add_student():
  name = input("Enter student's name: ")
  age = input("Enter student's age: ")
  Grade = input("Enter Student's Grade:")
  students.append(student(name, age,Grade))
  print("Student added successfully.")


def add_teacher():
  name = input("Enter Teacher's name: ")
  subject = input("Assign subject to teacher: ")
  salary = int(input("Enter teacher's salary:"))
  teachers.append(teacher(name, subject,salary))
  print("Teacher added successfully.")


user_name = "dua"
password = 1122
login = str(input("Enter your user name: "))
pin = int(input("Enter your password:"))
if login == user_name and pin == password:
  print("welcome to Dua school management system")
else:
  print("invalid user_name and password")
  exit()
while True:
 menu = int(input("Main Menu \n1. Add Student Data \n2. Add Teacher Data \n3. Exit"))
 if menu == 1:
      print(add_student())
 elif menu == 2:
      print(add_teacher())
 elif menu == 3:
      print("Program is close")
      exit()


      
