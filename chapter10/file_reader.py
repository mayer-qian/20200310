with open('pi_digis.txt') as file_object:
    #contents = file_object.read()
    #print(contents.rstrip())
    #for line in file_object:
       # print(line.rstrip())
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
