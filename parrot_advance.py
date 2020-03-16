prompt = "If you tell us who you are, we can personalize the message you see"
prompt += "\nEnter 'quit' to end the program."
message = " "
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)