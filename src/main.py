#!/usr/sbin/python

import curses
import manual
import menu
import sys
import os


#Printing out instruction for add_item and remove_item functions
def print_instruction(stdscr):
    instructions = ["1. Hit Ctrl+G to save", "2. Hit Ctrl+H to delete character backward",
                "3. Save first and Hit any key to return to main menu"]
    x = 0
    y = 1 
    for instruction in instructions:      
        stdscr.addstr(y,x,instruction)
        y+=1

#Reading data from a textfile
def get_shopping_list(filename):
    text_file = open(filename,"r")
    temp = text_file.readlines()
    text_file.close()
    shopping_list = []
    for item in temp:
        shopping_list.append(item.strip("\n"))
    return shopping_list

#Writing data to a textfile
def update_shopping_list(filename, param_list):
    text_file = open(filename,"w")
    for item in param_list:
        text_file.write(item +"\n")
    text_file.close()

#main function
def main(stdscr):
    curses.curs_set(0)
    #Set the highlight color
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    #Set the position menu default at the first menu option
    current_row_index = 0
    #Display the main menu list
    menu.display_menu(stdscr, current_row_index)
    #Get the stored data from the textfile into the application shopping_list
    shopping_list = get_shopping_list("shopping_list.txt")

    while True:
        #Waiting for any input from user
        user_key = stdscr.getch()
        stdscr.clear()
        #Handling pressed key by the user for navigation
        if user_key == curses.KEY_UP and current_row_index > 0 :
            current_row_index -= 1
        elif user_key == curses.KEY_DOWN and current_row_index < len(menu.menu) - 1:
            current_row_index += 1
        elif user_key == curses.KEY_ENTER or user_key in [10,13]:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(0,0,f"{(menu.menu[current_row_index]).upper()}")
            stdscr.attroff(curses.color_pair(1))

            stdscr.refresh()

            #Customisation of each menu selected
            #View Shopping List option
            if current_row_index == 0:
                stdscr.addstr(1,0,"Hit any key to return to main menu")
                menu.view_list(stdscr,shopping_list)
            
            #Add Item to Shopping List option
            elif current_row_index == 1:
                print_instruction(stdscr)
                stdscr.addstr(6,0,"Please type in the item that you want to add into your shopping list.(1 item per line)")
                stdscr.addstr(5,0,f"Your curent shopping list: {shopping_list}")
                stdscr.refresh()
                menu.add_item(shopping_list)
                stdscr.addstr(menu.height-1,0,"The item(s) has been added to the shopping list")
            
            #Remove Item from Shopping List option
            elif current_row_index == 2:
                print_instruction(stdscr)
                stdscr.addstr(6,0,"Please type in the item that you want to remove from shopping list.(1 item per line)")
                stdscr.addstr(5,0,f"Your curent shopping list: {shopping_list}")
                stdscr.refresh()
                menu.remove_item(stdscr,shopping_list)
            
            #Clear Shopping List option
            elif current_row_index == 3:
                stdscr.addstr(1,0,"Hit any key to return to main menu")
                menu.clear_shopping_list(stdscr,shopping_list)
            
            # Exit option
            elif current_row_index == len(menu.menu)-1:
                update_shopping_list("shopping_list.txt",shopping_list)
                sys.exit()

            #pressed any key
            stdscr.getch()    

        #return back to menu list
        menu.display_menu(stdscr, current_row_index)
        stdscr.refresh()



if "--help" in sys.argv:
    user_input = manual.help()
    if user_input == "q":
        pass
    else: 
        print("The input you enter is invalid")
elif "--about" in sys.argv:
    user_input = manual.about()
    if user_input == "1":
        shopping_list = get_shopping_list("shopping_list.txt")
        if (len(shopping_list)!= 0):
            print(shopping_list)
        else:
            print("Shopping List is currently empty")
    elif user_input == "q":
        pass
    else: 
        print("The input you enter is invalid")          
else:
    #wrapping the main function to be able to work in conjuction with curses.
    #It has error handling for SystemError which may happen if there is issue with the python interpreter
    try:
        curses.wrapper(main)
    except SystemError:
        print("Oops! Something is wrong. Please ensure that you are using Python3 and try again later.")
    
