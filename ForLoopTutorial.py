username = ["Francis", "Andrea", "Noaim"]
password = ["Francis123","Andrea123","Noaim123"]

uname = input("Username: ")
pword = input("Password: ")

for x in range(len(username)):
    if uname == username[x] and pword == password[x]:
        print("Access Granted")
        break
else:
        print("User not found")