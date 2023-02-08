import datetime
from tabulate import tabulate

store_name = 'Dany Super Market'
store_address = 'Bhola Nath Nagar, 110032.'
store_city = 'New Delhi'
customer_Name = input('Enter Customer\'s Name : ')

now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

Item1 = input('Name of first item : ')
Price1 = int(input('Enter price of the item : '))
Unit1 = int(input('Number of units sold : '))
totalprice1 = int(Unit1 * Price1) 
print("Total price is : " + str(totalprice1))
print('\n')

Item2 = input('Name of second item : ')
Price2 = int(input('Enter price of the item : '))
Unit2 = int(input('Number of units sold : '))
totalprice2 = int(Unit2 * Price2) 
print("Total price is : " + str(totalprice2))
print('\n')

Item3 = input('Name of third item : ')
Price3 = int(input('Enter price of the item : '))
Unit3 = int(input('Number of units sold : '))
totalprice3 = int(Unit3 * Price3) 
print("Total price is : " + str(totalprice3))
print('\n')

subtotal = totalprice1 + totalprice2 + totalprice3 

tax = (subtotal * 0.06)

grand_total = subtotal + tax

message = 'Thanks for shopping with us today!'

print('*' * 55)
print('\t\t{}'.format(store_name.title()))
print('\t\t{}'.format(store_address.title()))
print('\t\t{}'.format(store_city.title()))
print('=' * 55)
print(f"Customer Name : {customer_Name}")
print(f"{date_time[0:10]}\t\t\t\t{date_time[10:]}")
print('=' * 55)
print("List of Items\n")

table = [[Item1,Unit1,Price1,totalprice1],[Item2,Unit2,Price2,totalprice2],[Item3,Unit3,Price3,totalprice3]]
headers = ["Item"    ,    "Unit"    ,    "Price per one"    ,    "Total price"]
print(tabulate(table, headers, tablefmt="outline"))
print('')
print('=' * 55)
print("SUBTOTAL: ${:.2f}".format(subtotal))
print("TAX @ 6% : ${:.2f}".format(tax))
print("TOTAL AMOUNT: ${:.2f}".format(grand_total))
print('=' * 55)

print('\n\t{}\n'.format(message))
print('*' * 50)













