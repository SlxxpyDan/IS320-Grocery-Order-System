"""IS 320 Project Final Version Developed by Julie Mai, Nouryani Saleh, Matthew Chan, Victor Man"""

import datetime
import random

products = {
    1001: {'name': 'Apples',  'unit_price': 0.1,  'stock': 500, 'in_stock': True},
    1002: {'name': 'Bananas', 'unit_price': 0.5,  'stock': 500, 'in_stock': True},
    1003: {'name': 'Oranges', 'unit_price': 0.75, 'stock': 750, 'in_stock': True},
}

order_id = 10000  
orders = {}       

customers = {
    1001: {'password': 'cpass1', 'name' : 'Alice'},
    1002: {'password': 'cpass2', 'name' : 'Bob'}
}

managers = {
    9001: {'password': 'mpass1', 'name': 'Manager One'}
}


def compute_price(product, quantity):  # 'product' is the product id
    unit_price = products[product]['unit_price']
    price = unit_price * quantity
    return price
#end function


def display_products(show_stock=False):
    print('\nAvailable Products:')
    if show_stock:
        width = 55
        line = '-' * width
        print(line)
        print(f'|{"ID":^10s}|{"Name":^15s}|{"Unit Price":^15s}|{"Stock":^10s}|')
        print(line)
        for pid in products:
            product_details = products[pid]
            name = product_details['name']
            unit_price = product_details['unit_price']
            stock = product_details['stock']
            print(f'|{pid:<10d}|{name:^15s}|{unit_price:^15.2f}|{stock:^10d}|')
        print(line)
    else:
        width = 43
        line = '-' * width
        print(line)
        print(f'|{"ID":^10s}|{"Name":^15s}|{"Unit Price":^15s}|')
        print(line)
        for pid in products:
            product_details = products[pid]
            name = product_details['name']
            unit_price = product_details['unit_price']
            print(f'|{pid:<10d}|{name:^15s}|{unit_price:^15.2f}|')
        print(line)
#end function

def get_date():
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date = current_date + datetime.timedelta(days=1)
    
    random_date = random.choice(dates)
    return random_date
#end function

def submit_order(customer_id):
    global order_id, orders
    
    display_products()
    
    pid = int(input('\nEnter product ID: '))
    while pid not in products:
        print('Invalid product ID. Please choose from available products.')
        pid = int(input('Enter product ID: '))
    
    stock = products[pid]['stock']
    if stock <= 0:
        print('Sorry, this product is out of stock.')
        return
    
    quantity = int(input('Enter quantity: '))
    while quantity <= 0 or quantity > stock:
        if quantity <= 0:
            print('Quantity must be greater than 0.')
        else:
            print(f'Sorry, only {stock:d} units of this product are available.')
        quantity = int(input('Enter quantity: '))
    
    order_price = compute_price(pid, quantity)
    
    order_date = get_date()
    
    product_name = products[pid]['name']
    
    products[pid]['stock'] -= quantity
    if products[pid]['stock'] <= 0:
        products[pid]['in_stock'] = False
    else:
        products[pid]['in_stock'] = True
    
    order_details = {
        'order_date': order_date,
        'customer_id': customer_id,
        'product_id': pid,
        'product_name': product_name,
        'quantity': quantity,
        'order_price': order_price
    }
    
    order_id += 1
    orders[order_id] = order_details
    
    print_order(order_id)
#end function

def print_order(oid):
    order_details = orders[oid]
    
    order_date = order_details['order_date']
    customer_id = order_details['customer_id']
    product_id = order_details['product_id']
    product_name = order_details['product_name']
    quantity = order_details['quantity']
    order_price = order_details['order_price']
    
    order_date_string = order_date.strftime("%m-%d-%Y")
    
    print('\nOrder Confirmation:')
    print(f'Order ID:\t{oid:d}')
    print(f'Date:\t\t{order_date_string:s}')
    print(f'Customer ID:\t{customer_id:d}')
    print(f'Product ID:\t{product_id:d}')
    print(f'Product Name:\t{product_name:s}')
    print(f'Quantity:\t{quantity:d}')
    print(f'Order Price:\t{order_price:.2f}')
#end function

def display_orders(customer_id):
    if not orders:
        print('No orders to display.')
        return
    
    if customer_id:
        filtered_orders = {}
        for oid in orders:
            if orders[oid]['customer_id'] == customer_id:
                filtered_orders[oid] = orders[oid]
        if not filtered_orders:
            print('No orders yet.')
            return
        orders_to_display = filtered_orders
    else:
        orders_to_display = orders
    
    print('\nAll Orders:')
    width = 90
    line = '-' * width
    print(line)
    print(f'|{"Order ID":^12s}|{"Customer":^12s}|{"Date":^12s}|{"Product ID":^12s}|{"Name":^12s}|{"Quantity":^10s}|{"Price":^12s}|')
    print(line)
    
    for oid in orders_to_display:
        order_details = orders_to_display[oid]
        order_date = order_details['order_date']
        customer_id = order_details['customer_id']
        product_id = order_details['product_id']
        product_name = order_details['product_name']
        quantity = order_details['quantity']
        order_price = order_details['order_price']
        
        order_date_string = order_date.strftime("%m-%d-%Y")
        
        print(f'|{oid:<12d}|{customer_id:^12d}|{order_date_string:^12s}|{product_id:^12d}|{product_name:^12s}|{quantity:^10d}|{order_price:^12.2f}|')
    
    print(line)
#end function

#Customer and Manager Login
def login():
    print('\nLogin as 1. Customer 2. Manager 3. Quit')
    user_choice = int(input('Enter choice: '))
    
    #Customer Login
    if user_choice == 1:
        uid = int(input('Enter customer ID: '))
        while uid not in customers:
            print('Invalid ID.')
            uid = int(input('Enter customer ID: '))
        
        password = input('Enter password: ')
        while password != customers[uid]['password']:
            print('Wrong password, please re-enter.')
            password = input('Enter password: ')
        
        print('You are logged in!')
        return 'customer', uid
    
    #Manager Login
    elif user_choice == 2:
        uid = int(input('Enter manager ID: '))
        while uid not in managers:
            print('Invalid ID.')
            uid = int(input('Enter manager ID: '))
        
        password = input('Enter password: ')
        while password != managers[uid]['password']:
            print('Wrong password. Please re-enter!')
            password = input('Enter password: ')
        
        print('You are logged in!')
        return 'manager', uid
    
    elif user_choice == 3:
        return 'quit', None
    
    else:
        print('Invalid choice.')
        return login()
#end login function

#Customer Menu
def customer_menu(customer_id):
    while True:
        print('\nCustomer Menu:')
        print('1. Submit Order 2. Display My Orders 3. Logout 4. Quit')
        choice = int(input('Enter choice: '))
        if choice == 1:
            submit_order(customer_id)
        elif choice == 2:
            display_orders(customer_id)
        elif choice == 3:
            print('Logging out.')
            return 'logout'
        elif choice == 4:
            return 'quit'
        else:
            print('Invalid choice!')
#end function

def edit_prices():
    display_products(show_stock=True)
    pid = int(input('\nEnter product ID to edit price: '))
    
    while pid not in products:
        print('Invalid product ID.')
        pid = int(input('Enter product ID to edit price: '))
    
    new_price = float(input('Enter new unit price: '))
    while new_price <= 0:
        print('Price must be greater than 0.')
        new_price = float(input('Enter new unit price: '))
    
    products[pid]['unit_price'] = new_price
    print('Price updated successfully.')
    display_products(show_stock=True)
#end function

#Reorder stock function for manager menu
def reorder_stock():
    display_products(show_stock=True)
    pid = int(input('\nEnter product ID to reorder: '))
    
    while pid not in products:
        print('Invalid product ID.')
        pid = int(input('Enter product ID to reorder: '))
    
    qty = int(input('Enter quantity to add: '))
    while qty < 0:
        print('Quantity cannot be negative.')
        qty = int(input('Enter quantity to add: '))
    
    products[pid]['stock'] += qty
    products[pid]['in_stock'] = products[pid]['stock'] > 0
    
    print('Stock updated successfully.')
    display_products(show_stock=True)
#end function

#Manager Menu
def manager_menu(manager_id):
    while True:
        print('\nManager Menu:')
        print('1. Display All Orders 2. Edit Prices 3. Reorder Stock 4. Logout 5. Quit')
        choice = int(input('Enter choice: '))
        
        if choice == 1:
            display_orders(None)
        elif choice == 2:
            edit_prices()
        elif choice == 3:
            reorder_stock()
        elif choice == 4:
            print('Logging out.')
            return 'logout'
        elif choice == 5:
            return 'quit'
        else:
            print('Invalid choice!')
#end function

#MAIN
while True:
    user_type, user_id = login()
    
    if user_type == 'quit':
        break
    
    if user_type == 'customer':
        result = customer_menu(user_id)
    elif user_type == 'manager':
        result = manager_menu(user_id)
    else:
        continue
    
    if result == 'quit':
        break

print('Goodbye!')