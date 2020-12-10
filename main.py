from mws import mws
import MySQLdb

db = MySQLdb.connect(host='localhost',
                     user='root',
                     passwd='root',
                     db='test_database')

cur = db.cursor()

access_key = ''  # replace with your access key
seller_id = ''  # replace with your seller id
secret_key = ''  # replace with your secret key
marketplace_usa = 'ATVPDKIKX0DER'

orders_api = mws.Orders(access_key, secret_key, seller_id, region='US')
orders = orders_api.list_orders(marketplaceids=[marketplace_usa], created_after='2020-12-10', max_results='1')

products_as_dict = orders.parsed
print(products_as_dict)
if 'Error' in products_as_dict:
    print('Error')
if not bool(products_as_dict):
    print('Empty')
    exit()
    BuyerEmail = ''
    BuyerName = ''
    AddressLine1 = ''
    OrderTotal = '0.00'
for y in products_as_dict['Orders']['Order']:
    BuyerEmail = ''
    BuyerName = ''
    AddressLine1 = ''
    OrderTotal = '0.00'
    Name = ''
    City = ''
    StateOrRegion = ''
    PostalCode = ''
    AddressType = ''
    print(y)

s = products_as_dict['Orders']['Order']['PurchaseDate']['value']

print(f'PurchaseDate => {s}')

cur.execute(s)
db.commit()

db.close()
