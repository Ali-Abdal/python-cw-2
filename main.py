# part 1

my_name = input("Enter your name: ")
my_age = input("Enter your age: ")

print(f"My name is {my_name.title()} and I am {my_age} years old")


# part 2

print("""
Rules:
1. only 2 numbers
2. you should leave space between the operation and the numbers (a + b)
""")

message = input("Type the math question: ")

list = message.split()

number1 = list[0]
number2 = list[2]
operation = list[1]

if operation.strip() == '+':
    print(number1, " + ",number2, " = ",(int(number1) + int(number2)))

elif operation.strip() == '-':
    print(number1, " - ",number2, " = ",(int(number1) - int(number2)))

elif operation.strip() == '*':
    print(number1, " * ",number2, " = ",(int(number1) * int(number2)))

elif operation.strip() == '/':
    print(number1, " / ",number2, " = ",(int(number1) / int(number2)))

else:
    print("Invaild input !")

    
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

