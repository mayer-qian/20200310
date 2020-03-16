def greet_user(user):
    print("hello," + user.title() + "!")


greet_user('mayer')

print("===================================================")


def describe_pets(animal_type, pet_name='harry'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is '" + pet_name.title() + ".")


describe_pets('hamster')

print("====================================")


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

print("==========================================")


def build_persion(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_persion('jimi', 'hendrix')
print(musician)
