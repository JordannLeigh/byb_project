#print("Hello World!")
#print("Git is Awesome!")

message = "Git is Awesome!"
new_message = ""
for i, char in enumerate(message):
    if i % 2 == 0:
        new_message += char.upper()
    else:
        new_message += char.lower()
print(new_message)
#output = GiT iS aWeSoMe!
