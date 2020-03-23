def print_models(unprinted_list, completed_list):
    while unprinted_list:
        current_list = unprinted_list.pop()
        print("\n Printing " + current_list)
        completed_list.append(current_list)


def show_completed_list(completed_list):
    for completed_model in completed_list:
        print(completed_model)


unprinted_design = ['iphone case', 'robot pendant', 'dodecahedrom']
completed_design = []
#用[:]只传的是副本，不加的话源文件会受影响
print_models(unprinted_design[:], completed_design)
show_completed_list(completed_design)
print(unprinted_design)