"""
Simple Calculator
"""

# Provide your solution here
def calculate(operand1: int, operand2: int, operator: str) -> int or float or str:
    if operator == "+":
        print(operand1 + operand2)
    elif operator == "-":
        print(operand1 - operand2)
    elif operator == "*":
        print(operand1 * operand2)
    elif operator == "/" and operand2 != 0:
        print(operand1 / operand2)
    elif operator == "/" and operand2 == 0:
        print("Devision by 0 is not allowed")
    else:
        print("Invalid operator")


"""
Reverse Word
"""
# Provide your solution here

def reverse_word(word: str) -> str:
    print(word[-1].capitalize(), end="")
    i = -2
    while i > -1 * (len(word)):
        print(word[i].lower(), end="")
        i -= 1
        if i == len(word) * -1:
            print(word[i].lower())



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

# Task 01
calculate(3,4,"+")
calculate(3,4,"-")
calculate(3,4,"/")
calculate(3,4,"*")
calculate(3,0,"/")
calculate(3,0,"*")
calculate(3,4,"?")

# # Task02
reverse_word("hello")
reverse_word("WORLD")
reverse_word("lEOn")