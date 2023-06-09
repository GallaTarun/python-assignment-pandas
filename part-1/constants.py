import os

class Constants:
    PASSWORD = "EMLyon"

    MAIN_MENU_STRING = '''
--------------------------------------
Welcome to the student, client and sales analysis

1) Create a new student in the list
2) Show all the student in the list
3) Show Excel file client and sales
4) Analyze Excel file client and sales
5) Analyze CSV file
6) Quit

Choose an option between 1 and 6: '''
    
    STUDENT_CREATION_STRING = '''
--------------------------------------
STUDENT CREATION

    '''

    STUDENT_CREATION_SUCCESS = "The student has been created and saved in the list.\n"

    STUDENT_CSV_DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "students_list.csv")

    STUDENT_INFORMATION_STRING = '''
--------------------------------------
STUDENT INFORMATION 

    '''

    CLIENTS_AND_SALES_INFORMATION_STRING = '''
--------------------------------------
EXCEL CLIENT AND SALES INFORMATION

1) Show clients
2) Show sales
3) Analyze clients sales
4) Go back

Choose an option between 1 and 4: '''

    CLIENTS_AND_SALES_EXCEL_PATH = os.path.join(os.path.dirname(__file__), "data", "clients_sales.xlsx")

    RETRIEVE_CLIENT_SALES_STRING = '''
RETRIEVE CLIENTS SALES INFORMATION

What is the name of the client? :'''

    ANALYZE_CLIENT_SALES_STRING = '''
--------------------------------------
ANALYZE CLIENT SALES INFORMATION

1) Sum of sales per category rows per region columns
2) Mean of sales per clients rows and category columns
3) Merge tables of clients and sales
4) Go back

Choose an option from 1 to 4: '''

    CATETGORY_REGION_EXCEL_PATH = os.path.join(os.path.dirname(__file__), "data", "Sum of sales cat reg.xlsx")

    CLIENT_CATEGORY_EXCEL_PATH = os.path.join(os.path.dirname(__file__), "data", "Mean of sales client cat.xlsx")

    MERGED_TABLES_EXCEL_PATH = os.path.join(os.path.dirname(__file__), "data", "Merge_tables.xlsx")