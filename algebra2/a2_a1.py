import readline
import mpmath
from .global_functions import copy
from sympy import parse_expr, Symbol


def introduction():
    print("\nA2.A1 - evaluate variable expressions involving integers\n")
    print("enter the expression. you will be asked what each variable's value is.")
    print("the program will return the solution.")
    print("type 'e' to exit.\n")


def solve_ixl():
    while True:
        try:
            user_input = input()
            if user_input == "e":
                print("exiting a2.a1...\n")
                break

            expression = parse_expr(user_input)
            variables = expression.free_symbols
            variable_value_pairs = [] # create a list of 2-tuples: item 1 is the variable, item 2 is its value

            for variable in variables:
                # ask the user what each variable's value is; cast to int since this ixl only deals with integers
                substitution = int(input(str(variable) + " = "))
                variable_value_pairs.append((variable, substitution))

            answer = str(int(expression.subs(variable_value_pairs)))

            print(answer + "\n")
            copy(answer)

        except Exception as e:
            print(str(e) + "\n")
