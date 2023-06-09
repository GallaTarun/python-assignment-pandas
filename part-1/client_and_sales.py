import pandas as pd
from constants import Constants

def getClientsInfo(printDf=False):
    '''
    This function returns a dataframe containing clients data 
    in the client_sales.xlsx file.

    printDf - to print the Dataframe if True
    '''
    # read clients data from excel sheet into a dataframe
    clients_df = pd.read_excel(Constants.CLIENTS_AND_SALES_EXCEL_PATH, sheet_name='clients')
    if printDf:
        print(clients_df)
    return clients_df

def getSalesInfo(printDf=False):
    '''
    This function returns a dataframe containing sales data 
    in the client_sales.xlsx file.

    printDf - to print the Dataframe if True
    '''
    sales_df = pd.read_excel(Constants.CLIENTS_AND_SALES_EXCEL_PATH, sheet_name='sales')
    if printDf:
        print(sales_df)
    return sales_df

def analyzeClientSales():
    '''
    This function prompts user to enter a client name, and then prints 
    mean sales, maximum spend for a sale, and total sales done by the client
    '''
    # retrieving clients and sales data
    clients_df = getClientsInfo()
    sales_df = getSalesInfo()

    while True:
        # user input for client name
        clientName = input(Constants.RETRIEVE_CLIENT_SALES_STRING)
        # finding the client number of the client entered 
        clientIndex = clients_df.index[clients_df['name'].str.lower() == clientName.lower()]
        # check if any record with entered name found in clients data
        if len(clientIndex) > 0:
            # client found, get all sales done by the client and
            # calculate mean sales, maximum sale and total sales 
            # rounding off the values to 2 decimal places
            clientID = clients_df['client number'][clientIndex[0]]
            salesMadeByClient = sales_df[sales_df['Client number'] == clientID]

            salesMean = round(salesMadeByClient['Sales'].mean(), 2)
            maxSaleSpend = round(salesMadeByClient['Sales'].max(), 2)
            sumOfSales = round(salesMadeByClient['Sales'].sum(), 2)
            # print the above values
            print(clientID)
            print(f"The client has bought {len(salesMadeByClient)} products.")
            print(f"Here is the mean of its sales {salesMean}")
            print(f"Here is the maximum spend of for a sale {maxSaleSpend}")
            print(f"Here is the sum of sale {sumOfSales}\n")
        else:
            print("Client with the given name not found!\n")
        # user input to check another client's sales info.
        shouldContinue = input("Would you like to continue (y or n): ") == 'y'
        if not shouldContinue:
            return

def clientAndSalesAction():
    '''
    This function is invoked when user selects 3rd option in main menu,
    prompt to enter an option [1-4] to view clients data, sales data and
    analyze a client's sales
    '''
    while True:
        try:
            action = int(input(Constants.CLIENTS_AND_SALES_INFORMATION_STRING))
            if action == 1:
                # choice 1 to view clients data
                getClientsInfo(printDf=True)
            elif action == 2:
                # choice 2 to view sales data
                getSalesInfo(printDf=True)
            elif action == 3:
                # choice 3 to view a client's sales
                analyzeClientSales()    
            elif action == 4:
                # Go back to main menu
                return
        except:
            continue


def exportCategoryVsRegionData():
    '''
    This function exports a pivot table constructed on "Category" in rows and 
    "Region" in columns, and "Sales" sum as values.
    '''
    # get sales data
    sales_df = getSalesInfo()
    # creating pivot table for required criteria
    pivot_table = sales_df.pivot_table(index='Category', columns='Region', values='Sales', aggfunc='sum')
    # export it to an excel file
    pivot_table.to_excel(Constants.CATETGORY_REGION_EXCEL_PATH)

def exportClientsVsCategoryMeanData():
    '''
    This function exports a pivot table constructed on "Client number" in rows and 
    "Category" in columns, and "Sales" average as values.
    '''
    # get sales data
    sales_df = getSalesInfo()
    # creating pivot table for required criteria
    pivot_table = sales_df.pivot_table(index='Client number', columns='Category', values='Sales', aggfunc='mean')
    # export it to an excel file
    pivot_table.to_excel(Constants.CLIENT_CATEGORY_EXCEL_PATH)

def mergeTables():
    '''
    This function merges clients and sales data on a common column,
    and exports to an excel file
    '''
    # get clients and sales data
    client_df = getClientsInfo()
    sales_df = getSalesInfo()
    # Merging clients table and sales table on common column 'client number'
    merged_df = pd.merge(client_df, sales_df, left_on='client number', right_on='Client number')
    # export it to an excel file
    merged_df.to_excel(Constants.MERGED_TABLES_EXCEL_PATH)

def analyzeClientSalesData():
    '''
    This function is invoked when user selects option 4 in main menu,
    prompts the user to select one option in [1-4], invokes above export functions
    and merge function based on the option entered
    '''
    while True:
        try:
            action = int(input(Constants.ANALYZE_CLIENT_SALES_STRING))
            if action == 1:
                exportCategoryVsRegionData()
            elif action == 2:
                exportClientsVsCategoryMeanData()
            elif action == 3:
                mergeTables()
            elif action == 4:
                return
        except:
            continue