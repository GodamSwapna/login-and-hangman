import string
import json
def strong_password(user):
    data_l=string.ascii_lowercase
    data_u=string.ascii_uppercase
    data_p=string.punctuation
    data_d=string.digits
    # user=input("enter you are passward:")
    i=d=l=s=u=0
    # d=0
    # l=0
    # s=0
    # u=0
    while i<len(user):
        if user[i] in data_l:
            l+=1
        if user[i] in data_u:
            u+=1
        if user[i] in data_p:
            s+=1
        if user[i] in data_d:
            d+=1
        i=i+1
    # print(i)
    if i>=8 and l>=1 and u>=1 and s>=1 and d>=1:
        return True
    else:
        return False
def store(filename):
    f=open("userdetails1.json","r")
def sign_up():
    name=input("enter user name:")
    print("A password should contain atleast one lower letter one upper letter  one digit and one symboll")
    password=input("enter you are passward:")
    passward2=input("enter you are confirmation passward:")
    if password==passward2:
        psw=strong_password(password)
        if psw:
            d={"name":name,"password":password}
            server=input("do you want to submit'yes/no' file: ")
            with open("userdetails.json","r") as file:
                data=json.load(file)

            if server=="yes":
                dic={}
                if d not in data:
                    print("Congrats "+name+"  you are Sign Up Successfully.")
                    details={}
                    description=input("Enter you are Description:")
                    gender=input("Enter you are gender like'male/femal/transgender:")
                    hobbies=input("Enter you are Hobbies:")
                    dob=input("Enter you are Date of Birth:")
                    details["Description"]=description
                    details["Gender"]=gender
                    details["Hobbies"]=hobbies
                    details["Date_of_Birth"]=dob
                    d["Profile"]=details
                    dic["user"]=list(d)
                    print(dic)
                
                    # list1.append(user_info)
                    with open("userdetails.json","a") as file:
                        json.dump(dic,file,indent=4)
                else:
                    print("Username is already exists")
            else:
                print("Cancell")
        else:
            print("password should contain atleast one Symbool and one Digit ")
    else:
        print("Both passwords are not same")
def login():
    username=input("Enter you are name'He/She':")
    pass_word=input("Enter user password: ")
    json_file=open("userdetails.json","r")
    data=json_file.read()
    if (username in data) and (pass_word in data):
        print(username+" You are Logged in Successfully")
    else:
        print("Invalid Username and Password")
user_input=input("Do you want to sign up/login: ")
if user_input=="sign up":
    sign_up()
else:
    login()
