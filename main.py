# part 1

my_name = input("Enter your name: ")
my_age = input("Enter your age: ")

print(f"My name is {my_name.title()} and I am {my_age} years old")


# part 2

number1 = input("Type the first number: ").strip()

number2 = input("Type the secound number: ").strip()

operation = input("Type the operation type (+,-,*,/): ").strip()

if operation.strip() == '+':
    print(number1, " + ",number2, " = ",(int(number1) + int(number2)))

elif operation.strip() == '-':
    print(number1, " - ",number2, " = ",(int(number1) - int(number2)))

elif operation.strip() == '*':
    print(number1, " * ",number2, " = ",(int(number1) * int(number2)))

elif operation.strip() == '/':
    print(number1, " / ",number2, " = ",(int(number1) / int(number2)))

else:
    print("the operation is not valid make sure to use (+,-,/,*)!")

# part 3

print("Mad libs where libs get mad.\nStart below:")

random_number = input("Enter a random number from 1 to 12: ")

plural_noun = input("Enter a plural noun: ")

name = input("Enter a name: ")

sentance = input("Enter a sentance: ")

verb = input("Enter a verb: ")

print(f"""
The story goes...
It was {random_number} o'clock when I heard a knock at the door.
I opened the door and there was a box full of {plural_noun} with a note saying \"From {name.title()}.\"
Just as I closed the door I heard a scream \"{sentance.upper()}\"
I froze in place and all I could do was {verb}.
""")

