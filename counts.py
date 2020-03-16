count = 0
while count <= 10:
    count += 1
    if count % 2 != 0:
        continue
    print(count)


print("========================================")

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#for unconfirmed_user in unconfirmed_users:
    #confirmed_users.append(unconfirmed_user)
#print(confirmed_users)

print("========================================")
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verify user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
