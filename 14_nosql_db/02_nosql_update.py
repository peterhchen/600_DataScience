# Import Python Libraries
from pymongo import MongoClient
from pprint import pprint

# Select MongoClient
client = MongoClient()

# Connect to test db
db = client.test

# test db only have one collection 'employee'
employee = db.employee
employee.drop () # clean up collection before insert

employee_row = {
    'Name': 'Jessica Chen',
    'Address': '652 Calle Victoria, Sunnyvale, CA',
    'Age': '31'
}

# Insert row to employee collection 
res = employee.insert_one (employee_row)

db.employee.update_one(
    {'Name': 'Jessica Chen'},
    {
        '$set': {
            'Name': 'Jasmine Chen',
            'Address': '652 Calle Victoria, Sunnyvale, CA',
            'Age': '26'
        }

    }
)
# Query the insert document from collection employee
qRes = employee.find_one ({'Name': 'Jasmine Chen'})
print('qRes:')
pprint(qRes)