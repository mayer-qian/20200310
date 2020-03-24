import json

username = input("please input your name, and i will show it to you")
filename = 'username.txt'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("hello! " + username + "!")


with open(filename) as f_obj:
    name = json.load(f_obj)
    print("hello! " + name + "!")