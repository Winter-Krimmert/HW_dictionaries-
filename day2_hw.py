

# Task 1 Restaurant Menu Update
# Add a new category called "Beverages" with at least two items.
# Update the price of "Steak" to 17.99.
# Remove "Bruschetta" from "Starters".


restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
print(restaurant_menu)
# Adding a new category to restaurant menu dictionary called 'Beverages' with items: Coca Cola and Pepsi.
restaurant_menu_add = {"Beverages": {"Coca Cola": 4.00, "Pepsi": 3.00}}
restaurant_menu.update(restaurant_menu_add)

# update cost of Steak to 17.99
restaurant_menu["Main Course"]["Steak"] = 17.99

# Using del keyword and list(#list of dictionary keys)
menulist = list(restaurant_menu)
del restaurant_menu ["Starters"]["Bruschetta"]

print (restaurant_menu)


# 2. Customer Service Data Handling

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:

# Open a new service ticket.
# Update the status of an existing ticket.

# Display all tickets or filter by status.

# Initialize with some sample tickets and include functionality for additional ticket entry.


# Service ticket records

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
def new_ticket():
# Add new ticket
    new_ticket = input("Add your ticket number (ex.'Ticket001'): ")
# # Updation of service_tickets to add new ticket.
    service_tickets[f"Ticket{new_ticket}"] = {"Customer": "first name", "Issue": "ticket issue", "Status": "open"}


def update_status():
    ticket_num = input("Enter ticket number (i.e. 'Ticket00')")
    attribute = input("Update status to 'open' or 'close': ") # here I'm updating the attribute, status.
    new_value = input("Change Ticket Status to 'open' or 'closed': ") 
    service_tickets[ticket_num][attribute]= new_value

def update_customer():
    ticket_num = input("Enter ticket number (i.e. 'Ticket00')")
    attribute = input("Update status to 'open' or 'close': ") # here I'm updating the attribute, status.
    new_value = input("Change Ticket Status to 'open' or 'closed': ") 
    service_tickets[ticket_num][attribute]= new_value

def update_issue():
    ticket_num = input("Enter ticket number (i.e. 'Ticket00')").replace(" ", "")
    attribute = input("Type 'Issue' to change the ticket issue: ") # here I'm updating the attribute, issue.
    new_value = input("Enter your issue: ") 
    service_tickets[ticket_num][attribute]= new_value

def print_open_tickets():
# print all open tickets:
    open = input("Type 'open' to view open tickets. ")
    for ticket in service_tickets:
        if service_tickets["ticket_num"]["Status"] == "closed":
            print(ticket)
def print_closed_tickets():
# print all closed tickets
    closed = input("Type 'closed' to view closed tickets.")
    for ticket in service_tickets:
        if service_tickets["ticket_num"]["Status"] == "closed":
            print([service_tickets])

def print_all_tickets():
# print all tickets
            print ([service_tickets])

def del_ticket():
    # delete an entire ticket
    delete_ticket = input("type ticket number 'Ticket001' to remove ticket. ")
    for ticket in service_tickets:
        if delete_ticket in service_tickets:
            del delete_ticket

def manage_service_tickets():

    while True:
        response = input("""                  MENU
            1. Add new ticket0
            2. Update ticket status
            3. Update customer
            4. Update Issue
            5. Display closed tickets
            6. Display open tickets
            7. Display all tickets
            8. Delete a ticket
            9. Quit
                            
            Enter a number to select menu option: """)
        if response == "1":
            # Add new ticket
            new_ticket()
        elif response == "2":
            # Update ticket status
            update_status()
        elif response == "3":
            # update customer
            update_customer()
        elif response == "4":
            # update issue
            update_issue()
        elif response == "5":
            # display closed tickets
            print_closed_tickets()
        elif response == "6":
            # display open tickets
            print_open_tickets()
        elif response == "7":
            # display all tickets
            print_all_tickets()
        elif response == "8":
            # delete a ticket
            del_ticket()
        elif response == "9":
            # quit 
            break
        else:
            print("Please enter a valid response. ")

manage_service_tickets()






