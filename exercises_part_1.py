def new_Exercise(exer):
    exercise_string = "Exercise " + str(exer)
    print("\n", exercise_string.center(80, '*'))
    return exer + 1


def numb_input(question):  # Function to check if an integer was entered
    try:
        return int(input(question))
    except ValueError:
        print("Please only enter a number!")
        numb_input(question)


# Exercise 1
def famous_quote():
    quote = '“Battle not with monsters, lest ye become a monster, and if you gaze into the abyss, the abyss gazes also into you.”'
    author = "Friedrich Nietzsche"

    print(f"{author} once said, {quote}\n")


# Exercise 2
def number_eight():
    print(4 + 4)
    print(12 - 4)
    print(2 * 4)
    print(24 // 3)
    print(2 ** 3, "\n")


def name_age():  # Exercise 3
    name = input("Please enter your name:")
    age = numb_input("Please enter your age:")
    print(f"Hello, {name}. You are {age} years old.")
    print("Hello, {0}. You are {1} years old.".format(name, age))
    print("Hello, " + name + ". You are " + str(age) + " years old.\n")


def swap_integers():  # Exercise 4
    x = numb_input("Please enter a value for x:")
    y = numb_input("Please enter a value for y:")
    print(f"x={x}\ny={y}")
    z, x = x, y
    y = z
    print(f"After Swap\nx={x}\ny={y}\n")


def check_number(number1, number2):  # Exercise 5
    if number1 % 6 == 0 or number2 % 6 == 0:
        print("At least one number is divisible by 6")
        if number1 % 10 == 0 and number2 % 10 == 0:
            print("Both numbers are divisible by 10")
            return True
        else:
            return False
    return False


def sum_up(number1, number2):  # Exercise 6
    gesamt = 0
    if number1 < number2:
        for num in range(number1, number2 + 1):
            gesamt += num
        print(f"Adding values from {number1}-{number2}...\n The sum is {gesamt}\n")
        return gesamt
    else:
        print(f"The second number is bigger than the first\n")
        return None


def sequence(number):  # Exercise 7w
    sequence_string = ""
    if 0 <= number <= 9:
        for x in range(10):
            if x != number:
                sequence_string += str(x) + " "
        print(sequence_string)
    else:
        print("The number is not between 0-9\n")
        num = numb_input("Please enter a number between 0-9:")
        number = sequence(num)


def check_string(text):  # Exercise 8
    a, b = 0, 0
    a = text.lower().count('a', 0, 1)
    b = text.lower().count('a', len(text) - 1, len(text))
    if a or b:
        return True
    else:
        return False


def triangle(rows):  # Exercise 9
    for row in range(rows):
        print("* " * (row + 1))


Exercise_num = 1

Exercise_num = new_Exercise(Exercise_num)# Exercise 1
famous_quote()

Exercise_num = new_Exercise(Exercise_num)# Exercise 2
number_eight()

Exercise_num = new_Exercise(Exercise_num)# Exercise 3
name_age()

Exercise_num = new_Exercise(Exercise_num)# Exercise 4
swap_integers()

Exercise_num = new_Exercise(Exercise_num)# Exercise 5
print("Check numbers!")
num1 = numb_input("Please enter the first number:")
num2 = numb_input("Please enter the second number:")
print("Boolean from the function 'check_numbers' is ", check_number(num1, num2), "\n")

Exercise_num = new_Exercise(Exercise_num)# Exercise 6
print("Enter 2 numbers and add all numbers inbetween together!")
a = numb_input("Please enter the first number: ")
b = numb_input("Please enter the second number: ")
if a > b:
    sum_up(b, a)
else:
    sum_up(a, b)

Exercise_num = new_Exercise(Exercise_num)
seq = numb_input("Please enter a number between 0-9: ") #  Exercise 7
sequence(seq)

Exercise_num = new_Exercise(Exercise_num)# Exercise 8
test_string = "h, Ich bin ein Test Stringa"
print(f"Der String '{test_string}' hat am Anfang oder am Ende ein 'a'? -->", check_string(test_string), "\n")

Exercise_num = new_Exercise(Exercise_num)  # Exercise 9
tria = numb_input("How many rows of stars do you want:")
triangle(tria)
