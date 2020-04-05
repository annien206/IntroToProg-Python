# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ANg,2.18.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
# TODO: Add Code Here
#("---Using a Dictionary object")
dicRow = {}
objFile = open("ToDoList.txt", "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()
print(lstTable)

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
# Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print(lstTable)
        continue

# Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        #print("---Using a List of Dictionary objects")
        objFile = open("ToDoList.txt", "r")

        for row in objFile:
            t, p = row.split(",")  # Split can be Unpacked
        objFile.close()

        while (True):
            strTask = input("Please Enter Task: ")
            strPriority = input("Please Enter Priority: ")
            lstTable.append({"Task": strTask, "Priority": strPriority})
            strChoice = input("Exit? ('y/n':) ")
            if strChoice.lower() == 'y':
                break

        print(lstTable)
        continue

# Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", "r")

        for row in objFile:
            t, p = row.split(",")  # Split can be Unpacked
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}

        while (True):
            strTask = input("Item to Remove: ")
            strStatus = "row not found"
            for row in lstTable:
                if row["Task"].lower() == strTask.lower():
                    lstTable.remove(row)
                    strStatus = "row removed"
            print(strStatus)
            print("Current Data", lstTable)
            strChoice = input("Exit? ('y/n'): ")
            if strChoice.lower() == 'y':
                break

        print(lstTable)
        continue
# Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", "r")
        lstTable.append({"Task": 'Sleep', "Priority": 'Low'})
        print(lstTable, '<< Now in Memory')

        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + ',' + str(row["Priority"] + '\n'))
        objFile.close()
        print("Now in file!")
        continue
# Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("You are going to exit the program.")
        break  # and Exit the program