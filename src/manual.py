import os

def help():
    os.system("clear")
    print("                                                              === SHOPPING CHECKLIST MANUAL === ")
    print("""
    These are common Shopping List key handler used by user to navigate and interact with the application
    
    Arrow_Up
    Arrow_Down
    Ctrl+G to save items
    Ctrl+H to delete character when type in input
    Enter to select a menu or coming back to main menu list
    """)

    return input("Press 'q' to quit ").lower().strip()

def about():
    os.system("clear")
    print("This is the overview of the Shopping List Application")
    print("""
    This is a terminal application that allows you to create shoppping list and store them in your personal machine.
    The application includes five menu options:
    1. View Shopping List : Display all the items that is currently in shopping list
    2. Add Item to Shopping List : User interactive that ask user to type in the item to add to the shopping list
    3. Remove Item from Shopping List : User interactive that ask user to type in the item wish to be removed from shopping list
    4. Clear Shopping List: Clear all items in shopping list at once
    5. Exit: Store data and terminate the application"
    """)
    return input("Press number  '1' to view the current shopping list or 'q' to quit ").lower().strip()


