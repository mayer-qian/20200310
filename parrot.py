message = input("Tell me something, and I will repeat it back to you")
print(message)


prompt = "If you tell us who you are, we can personalize the message you see"
prompt += "\nWhat is your first name"
name = input(prompt)
print("\nHello, " + name + "!")