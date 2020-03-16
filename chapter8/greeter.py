def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\n please input your name ")
    print("type q to quit")
    f_name = input("first name")
    if f_name == 'q':
        break
    l_name = input("last name")
    print("type q to quit")
    if f_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
