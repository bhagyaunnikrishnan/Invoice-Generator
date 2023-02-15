import datetime
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item
from pyinvoice.templates import SimpleInvoice

customer_Name = input('Enter Customer\'s Name : ')

doc = SimpleInvoice('invoice.pdf')

now = datetime.datetime.now()

doc.invoice_info = InvoiceInfo(1023, now, datetime.timedelta(days=3))
doc.service_provider_info = ServiceProviderInfo(
   name='Dany Super Market',
    street='Bhola Nath Nagar, 110032.',
    city='New Delhi'
)

doc.client_info = ClientInfo(name = customer_Name)

Item1 = input('Name of first item : ')
item1desc = input('Enter the description of item: ')
Price1 = int(input('Enter price of the item : '))
Unit1 = int(input('Number of units sold : '))
doc.add_item(Item(Item1, item1desc, Unit1, Price1))
print('\n')

Item2 = input('Name of second item : ')
item2desc = input('Enter the description of item: ')
Price2 = int(input('Enter price of the item : '))
Unit2 = int(input('Number of units sold : '))
doc.add_item(Item(Item2, item2desc, Unit2, Price2))
print('\n')

Item3 = input('Name of third item : ')
item3desc = input('Enter the description of item: ')
Price3 = int(input('Enter price of the item : '))
Unit3 = int(input('Number of units sold : '))
doc.add_item(Item(Item3, item3desc, Unit3, Price3))
print('\n')

message = 'Thanks for shopping with us today!'

doc.set_item_tax_rate(6)
doc.set_bottom_tip("Thanks for shopping with us today!")
doc.finish()

print("pdf saved as invoice.pdf")











