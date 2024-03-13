#print("Hello World!")
#print("Git is Awesome!")

print("Welcome!")

message = "Git is Awesome!"
alternates = ""
for i, char in enumerate(message):
    if i % 2 == 0:
        alternates += char.upper()
    else:
        alternates += char.lower()
print(alternates)
#output = GiT iS aWeSoMe!

# Adding the reverse functionality
print("Reversed:", message[::-1])

print("Goodbye!")
