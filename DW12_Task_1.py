import re
def register():
    email = input("Enter email address: ")
    passwd = input("Enter password: ")
    conf_pwd = input('Confirm password: ')

    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,15}$"
    pattern = "^\S+@\S+\.\S+$"

    if(re.fullmatch(pattern, email)):
        print("Email is Valid")
    else:
        print("Invalid Email")
        register()

    # compiling regex
    pat = re.compile(reg)
      
    # searching regex                 
    mat = re.search(pat, passwd)
      
    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")
        print("Must have minimum one special character")
        print("one digit")
        print("one uppercase")
        print("one lowercase character")
        register()

    if conf_pwd == passwd:
        with open('credentials.txt', 'w') as f:
             f.write(email + '\n')
             f.write(passwd)
        f.close()
        print('You have registered successfully!')
    else:
        print('Password is not same as above! \n')
        register()
        
def login():
    email = input('Enter email: ')
    passwd = input('Enter password: ')
    with open('credentials.txt', 'r') as f:
        stored_email, stored_pwd = f.read().split('\n')
    f.close()
    if email == stored_email and passwd == stored_pwd:
         print('Logged in Successfully!')
    else:
         print('Login failed! \n')
         register()
         
while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        register()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")
