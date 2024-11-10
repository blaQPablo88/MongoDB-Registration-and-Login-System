from pymongo import MongoClient

uri = 'mongodb://localhost:27017/'
client = MongoClient(uri)
database = client.get_database('testDB')
collection = database.get_collection('user')

select = 0

def registration():
    print('Registration')
    print('==========================')
    firstname = input('Please enter your firstname: ')
    lastname = input('Please enter your lastname: ')
    username = input('Please create a username: ')
    password = input('Please create a password: ')
    try:
        query = {'firstname': firstname, 'lastname': lastname, 'username': username, 'password': password, }
        results = collection.insert_one(query)
        if results is not None:
            print('Successfully registered')
        else:
            print('Registration unsuccessfully')
            return
    except Exception as e:
        raise Exception('Error', e)

def login():
    login_action = True 
    try:
        while login:
            print('UserLogin')
            print('==========================')
            username = input('enter username: ')
            password = input('enter password: ')
            query = {'username': username, 'password': password}
            user = collection.find_one(query)
            if user is None:
                print('Incorrect username or password')
                login_action = True
            else:
                print(user)
                print(f'Welcome, {user['firstname']} {user['lastname']}')
                login_action = False

    except Exception as e:
        raise('Cant find document due to', e)

while select < 2:
    print('Please select an option: ')
    print('==========================')
    print('1 -> Register')
    print('2 -> Login')
    selection = int(input('Please select an option: '))
    if selection == 1:
        registration()
    elif selection == 2:
        login()
    else:
        selection = int(input('Please select an option: '))

    