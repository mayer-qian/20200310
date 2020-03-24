import json
filename = 'username.txt'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What's your name")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("hello " + username + "!")
else:
    print("hello" + username + "!")