import curses
from curses.textpad import Textbox
import os

#Global variable of width and height of the screen. It is used by most of the function to positioned string that they want to display to sreen
width, height = os.get_terminal_size()
#Menu is set into global as it is used in main.py to control the user navigation ability
menu = ["View Shopping List", "Add Item to Shopping List",
            "Remove Item from Shopping List","Clear Shopping List",
            "Exit"]

#Printing out all the menu option to the center of the screen
def display_menu(stdscr, selected_row_index):
    stdscr.clear()
    curses.curs_set(0)
    #get the screen size
    height, width = stdscr.getmaxyx()

    #display menu and positioned at the center of the screen
    for index, row in enumerate(menu):
        x = width//2 - len(row)//2
        y = height//2 - len(menu)//2 + index

        #highlight the current position of user navigation
        if index == selected_row_index:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x,row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y,x,row)
    stdscr.refresh()

#Printing out all the items that is inside the shopping list
def view_list(stdscr,param_list, y=3,x=0):
    curses.curs_set(0)
    if len(param_list) > 0:
        for index,item in enumerate(param_list,1):
            stdscr.addstr(y,x,f"{index}.{item.capitalize()}")
            y+=1
    else:
        stdscr.addstr(y,x,"Your shopping list is currently empty")

 #Adding one or multiple items to the shopping list   
def add_item(param_list):
    curses.curs_set(1)
    #Create textbox to allow user input character
    window = curses.newwin(20, 100, 7, 0)
    box = curses.textpad.Textbox(window)

    #Let the user edit until Control-G is struck
    box.edit()

    #Get resulting contents and added it into the shopping list
    message = box.gather()
    temp = []
    temp.append(message)
    items = temp[len(temp)-1].split("\n")
    for item in items:
        param_list.append(item.strip().capitalize())
    param_list.pop(-1)

#Removing one or multiple items from the shopping list.
def remove_item(stdscr,param_list):
    remove_item = []
    curses.curs_set(1)
    
    #Create textbox to allow user input character
    window = curses.newwin(20, 100, 7, 0)
    box = curses.textpad.Textbox(window)
    
    #Let the user edit until Control-G is struck
    box.edit()

    #Get resulting contents and remove it from the shopping list
    message = box.gather()
    temp = []
    temp.append(message)
    items = temp[len(temp)-1].split("\n")
    for item in items:
        remove_item.append(item.strip().capitalize())
    remove_item.pop(-1)
    exist = []
    not_exist = []
    #check each item input by user whether it is exist or not exist in the shopping list
    for item in remove_item:
        if item in param_list:
            exist.append(item)
            param_list.remove(item)
            stdscr.addstr(height-1,0,f"The item(s) {exist} has been removed from the list")
        else:
            not_exist.append(item)
            stdscr.addstr(height-1,width//2,f"The item {not_exist} does not exist in the shopping list")

#clear all items inside shopping list at once
def clear_shopping_list(stdscr,param_list):
    #check the current length of shopping list 
    length = len(param_list)
    #keep removing item inside shopping list until it is empty. While loop need to be used to ensure the list is empty before the user press any key to direct back to the main menu list
    while len(param_list) > 0:
        text = f"Removing all {length} item(s) on your shopping list."
        stdscr.addstr(height//2,width//2-len(text)//2,text)
        for item in param_list:
            param_list.remove(item)
    #Printing message to acknowledge user that the shopping list is empty to begin with    
    if length == 0:
        text = "There is no item to be removed. Your shopping list is currently empty."
        stdscr.addstr(height//2,width//2-len(text)//2,text)












