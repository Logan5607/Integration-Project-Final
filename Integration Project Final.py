"""Integration Project: This is a math quiz that tests your knowledge on
basic math skills like addition and subtraction. Depending on what's being
asked, the answer may be a string, an integer, or a float. """

__author__ = "Logan Nguyen"

# This is my integration project, which is a simple math test.

# When question asks for an integer answer, create a function to check.

import math


def calculate_area(radius):
    """

    :param radius:
    :return:
    """
    area = math.pi * radius ** 2
    return round(area, 2)


def calculate_radius(diameter):
    """

    :param diameter:
    :return:
    """
    radius = diameter / 2
    return radius


while True:
    score = 0

    # When I was creating this question, I wanted to make it so that it
    # would count "yes" as correct either with or without capital letters.
    # After doing some research on Google, I discovered the "lower()"
    # function. https://www.geeksforgeeks.org/python-string-lower/
    print("Welcome to this short math quiz.")
    pollQuestion = input("Do you like doing math? ")
    if pollQuestion.lower() == "yes":
        print("Let's get started!")
    else:
        print("Unfortunately, you can't take this quiz because you hate math!")
        quit()

    # I also found the quit() function while doing some research and thought
    # I'd throw it in for fun in the first question.
    # https://codeberryschool.com/blog/en/how-to-end-a-program-in-python/

    # I also found out that you can implement a scoring system.
    # https://codereview.stackexchange.com/questions/202532/python-multi-choice-quiz-with-a-score-to-count
    addition_symbol = input("What does this symbol represent? (+) ")
    if addition_symbol.lower() == "addition":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # Addition (+) adds 2 numbers together.

    num1 = 6
    num2 = 2
    additionAnswer = num1 + num2
    print("What is 6 + 2? ")
    your_addition_answer = int(input())
    if additionAnswer == your_addition_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("Does 2 + 2 = 5?")
    joke_question = input()
    joke_answer = not (2 + 2 == 5)
    if joke_question.lower() == "no" and joke_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    subtraction_symbol = input("What does this symbol represent? (-) ")
    if subtraction_symbol.lower() == "subtraction":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    num1 = 9
    num2 = 5
    subtraction_answer = num1 - num2
    print("What is 9 - 5? ")
    yourAnswer = int(input())
    if subtraction_answer == yourAnswer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # Subtraction (-), subtracts 2 numbers.

    multiplication_symbol = input("What does this symbol represent? (*) ")
    if multiplication_symbol.lower() == "multiplication":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    num1 = 7
    num2 = 2
    multiplication_answer = num1 * num2
    print("What is 7 * 2? ")
    your_multiplication_answer = int(input())
    if multiplication_answer == your_multiplication_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # Multiplication (*), multiplies 2 numbers together.

    division_symbol = input("What does this symbol represent? (/) ")
    if division_symbol.lower() == "division":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    num1 = 10
    num2 = 2
    division_answer = num1 / num2
    print("What is 10 / 2? ")
    your_division_answer = int(input())
    if division_answer == your_division_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # Division (/), divides a number by another number.

    exponent_question = input("What tells you to multiply a number by itself? "
                              )
    if exponent_question.lower() == "exponent":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    num1 = 4
    num2 = 2
    power_answer = num1 ** num2
    print("What is 4^2? ")
    your_power_answer = int(input())
    if power_answer == your_power_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # Exponent (**), is raising a number to the power of another number (
    # aka, telling you how many times to multiply a number by itself).

    quotient_question = input("What is the whole number you get when you "
                              "divide? ")
    if quotient_question.lower() == "quotient":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("What is the square root of 4?")
    square_root_answer = int(input())
    if square_root_answer == 2 or square_root_answer == -2:
        print("Correct!")
    else:
        print("Incorrect!")

    num1 = 5
    num2 = 2
    whole_number_answer = num1 // num2
    print("What is the quotient for 5/2? ")
    your_whole_number_answer = int(input())
    if whole_number_answer == your_whole_number_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # Floor division, gives you the quotient when you divide 2 numbers,
    # but rounds it down to the nearest whole number.

    num1 = 9
    num2 = 4
    remainder_answer = num1 % num2
    print("What is the remainder for 9/4? ")
    your_remainder_answer = int(input())
    if remainder_answer == your_remainder_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # Modulus (%), gives you the remainder when you divide 2 numbers.

    num1 = 100
    num2 = 100
    equal = num1 == num2
    print("Does 100 = 100")
    equal_answer = input()
    if equal_answer.lower() == "yes":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # The equal sign in Python (==) checks if two values are equal to each
    # other.

    num1 = 800
    num2 = 200
    not_equal = num1 != num2
    print("Does 800 = 200")
    not_equal_answer = input()
    if not_equal_answer.lower() == "no":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # The not equal sign in Python (!=) checks if two values aren't equal
    # with each other

    num1 = 500
    num2 = 300
    num3 = 90

    var = num1 > num2 > num3
    print("Is 300 less than 500 and greater than 90?")
    greater_than_answer = input()
    if greater_than_answer.lower() != "yes" or var != True:
        print("Incorrect!")
    else:
        print("Correct!")
        score += 1
    # Greater than (>) compares two numbers to see which number is the largest.

    print(
        "Calculate the radius and the area of a circle with a diameter of 10:")
    correct_radius = calculate_radius(10)
    correct_area = calculate_area(correct_radius)

    user_answer_radius = int(input("Radius: "))
    user_answer_area = float(input("Area: "))

    if user_answer_radius == correct_radius:
        print("Correct!")
        score += 0.5

    else:
        print("Incorrect")

    if user_answer_area == correct_area:
        print("Correct!")
        score += 0.5

    else:
        print("Incorrect")

    print("Your score was a", format(score, ".0f") + "/18!")
    print("Thanks for taking this quiz.")
    print("If you have any questions email me, lwnguyen3410", "eagle.fgcu.edu",
          sep="@")
    print("You go have a", "awesome " * 2 + "day!")

    if score == 18:
        print("Nice work. :)")
        break
    elif score < 18:
        print("Since you didn't get all the answers correct, would you like "
              "to take this quiz again? ")
        go_again = input()
        if go_again == "yes":
            print("Please restart the program.")
            break
        else:
            print("You have no choice but to take the quiz again!")
# In print statements, (+) combines 2 strings into one and (*) tells the
# program to repeat a certain string by a given number of times.
