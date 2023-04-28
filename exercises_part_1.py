
# Exercise 1
def famous_quote():
    quote = '“Battle not with monsters, lest ye become a monster, and if you gaze into the abyss, the abyss gazes also into you.”'
    author = "Friedrich Nietzsche"

    print(f"{author} once said: {quote}\n")


# Exercise 2
def number_eight():
    print(4 + 4)
    print(12 - 4)
    print(2 * 4)
    print(24 / 3)
    print(2 ** 3, "\n")


def name_age():  # Exercise 3
    name = input("Please enter your name:")
    age = int(input("Please enter your age:"))
    print(f"Hello, {name}. You are {age} years old.")
    print("Hello, {0}. You are {1} years old.".format(name, age))
    print("Hello, " + name + ". You are " + str(age) + " years old.\n")


def swap_integers():  # Exercise 4
    x = int(input("Please enter a value for x:"))
    y = int(input("Please enter a value for y:"))
    print(f"x={x}\ny={y}")
    z = x
    x = y
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
    else:
        return False


def sum_up(number1, number2):  # Exercise 6
    gesamt = 0
    if number1 < number2:
        for num in range(number1, number2 + 1):
            gesamt += num
        print(f"The sum is {gesamt}\n")
        return gesamt
    else:
        print(f"The second number is bigger than the first\n")
        return None


def sequence(number):  # Exercise 7
    if 0 <= number <= 9:
        for x in range(10):
            if x != number:
                print(x)
    else:
        raise Exception("The number is not between 0-9\n")


def check_string(text):  # Exercise 8
    a, b = 0, 0
    a = text.lower().count('a', 0, 1)
    b = text.lower().count('a', len(text)-1, len(text))
    if a or b:
        return True
    else:
        return False


def triangle(rows):  # Exercise 9
    for row in range(rows):
        print("* "*(row+1))


famous_quote()  # Exercise 1
number_eight()  # Exercise 2
name_age()  # Exercise 3
swap_integers()  # Exercise 4
# Exercise 5
num1 = int(input("Please enter the first number:"))
num2 = int(input("Please enter the second number:"))
print("Boolean from the function 'check_numbers' is ", check_number(num1, num2), "\n")
sum_up(3, 9)  # Exercise 6
sequence(3)  # Exercise 7
print("\n", check_string("Ah, Ich bin ein Test String"), "\n")  # Exercise 8
triangle(10)  # Exercise 9

