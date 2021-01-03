
def login_name(func):
    def wrapper():
        n = input('Enter a Name \n')
        if n =='':
            print('Name not entered! ')
        else:
            print (f'Hello, {n} ! You are registered! ')
            func()
    return wrapper
     

def func_1():
    print('Welcome to the app!')

@login_name
def func_2():
    print('This is private data.\n')

@login_name
def func_3():
    print('This is private video.\n')

while True:
    i = input(' Menu\n'
             '1 -- Welcome to the app!\n'
             '2 -- This is private data. Name is required!\n'
             '3 -- This is private video. Name is required!\n'
             'q -- Exit\n'
             'what is your choice? : ')

    if i == '1':
        func_1()
    elif i == '2':
        func_2()
    elif i == '3':
        func_3()
    else:
        i == 'q'
        break

print('exit')