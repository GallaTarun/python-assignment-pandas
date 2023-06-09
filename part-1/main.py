import os
import pandas as pd

from student import Student
from constants import Constants
from client_and_sales import clientAndSalesAction, analyzeClientSalesData

def createNewStudent(student):
    '''
    This function adds a new student record to the students_list.csv

    student - Student object
    '''
    # retrieve exisiting student data
    student_df = pd.read_csv(Constants.STUDENT_CSV_DATA_PATH)
    # inserting new record at the end of the data
    student_data = {'Student Name': student.studentName, 'Student Email': student.studentEmail}
    student_df.loc[len(student_df)] = student_data
    # exporting the updated data to same file. 
    student_df.to_csv(Constants.STUDENT_CSV_DATA_PATH, index=False)
    print(f"\nStudent name : {student.studentName} \nStudent email : {student.studentEmail}\n")
    print(Constants.STUDENT_CREATION_SUCCESS)

def printAllStudentsData():
    '''
    This function prints all student data present in students_list.csv file
    '''
    print(Constants.STUDENT_INFORMATION_STRING)
    # retrieve existing student data
    student_df = pd.read_csv(Constants.STUDENT_CSV_DATA_PATH)
    # print all records
    for i in range(len(student_df)):
        print(f"Student name : {student_df['Student Name'][i]}")
        print(f"Student email : {student_df['Student Email'][i]}\n")


def performChoosenAction(choice):
    '''
    When user enters choice between 1 and 5, this function will be called to 
    perform certain action based on choice.
    '''
    if choice == 1:
        # Choice 1 to create new student
        print(Constants.STUDENT_CREATION_STRING)
        studentName = input("What is the name of the student? ")
        studentEmail = input("What is the email of the student? ")
        student = Student(studentName, studentEmail)
        createNewStudent(student)

    elif choice == 2:
        # Choice 2 to display all existing students data
        printAllStudentsData()

    elif choice == 3:
        # Choice 3 to display client and sales excel file data
        clientAndSalesAction()

    elif choice == 4:
        # Choice 4 to analyze sales data
        analyzeClientSalesData()

    elif choice == 5:
        # Choice 5 to analyze the CSV file (bonus question)
        pass
    

def showMainMenu():
    '''
    When user enters "EMLyon" password, main menu with 6 options will be shown,
    prompting the user to enter a choice from 1 to 6, if 6 is entered, this function 
    stops running. 
    '''
    while True:
        try:
            choice = int(input(Constants.MAIN_MENU_STRING))
            if choice == 6:
                return
            performChoosenAction(choice)
        except:
            continue
    
def login():
    '''
    This function prompts user to enter a password, and until user enters
    "EMLyon" as password, this function keeps on prompting for password.
    '''
    password = input("What is the password?\n")
    while password != Constants.PASSWORD:
        password = input("Wrong! What is the password?\n")

def initData():
    '''
    This function initializes the data folder
    '''
    CUR_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(CUR_DIR, "data")
    #  creating an empty 'students_list.csv' if not present inside 'data' folder.
    if 'students_list.csv' not in os.listdir(DATA_DIR):
        empty_df = pd.DataFrame({'Student Name':[], 'Student Email': []})
        empty_df.to_csv(Constants.STUDENT_CSV_DATA_PATH, index=False)

if __name__ == "__main__":
    initData()
    login()
    showMainMenu()