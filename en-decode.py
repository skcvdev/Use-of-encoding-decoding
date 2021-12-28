# Suppose the username and password of an user is 'birendra07' and 'i_love_Nepal' respectively.
user_name = "birendra07"
password = "i_love_Nepal"

# Here I am using "utf8" as an encoding and "strict" as an error response. [syntax: encode (encoding, error)]
password = password.encode("utf8", "strict") 

# For an example, the user want to acess something using his username and password so here he has to enter his password.
def login():
    i = 1
    while i <= 3:
        i += 1
        user_typed_password = input()
        
        if (user_typed_password == password.decode("utf8", "strict")):
            print("You are sucessfullly logged in!!") 
            break 
        
        else:
            if i<=3:
                print("You entered incorrect password.\n********************************************\nPlease!, Enter your correct Password.")
            
            else:
                print("Sorry!, The session has been expired.")

print("******************            \"Welcome to the our service\"                **********************\n")
print("Enter your password to login: ")
login()


    

