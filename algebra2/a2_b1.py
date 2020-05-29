import readline
import mpmath
from subprocess import check_call
from sympy import parse_expr, solve, Symbol
from sys import platform

def introduction():
    print("\nA2.B1 - solve linear equations\n")
    print("enter the equation.")
    print("the program will return the solution of the equation.")
    print("type 'e' to exit.\n")

def copy(answer): # copy to clipboard
    cmd = ("echo " + answer.strip() + "|clip") if platform == "Windows" else ("echo " + answer.strip() + "|pbcopy")
    return check_call(cmd, shell=True)

def solve_ixl():
    while True:
        try:
            user_input = input()
            if user_input == "e":
                print("exiting a2.a1...\n")
                break
            split_input = user_input.split("=")
            left_side = parse_expr(split_input[0])
            right_side = parse_expr(split_input[1])
            if (len((left_side - right_side).free_symbols) > 1):
                raise Exception("too many variables")
            expression = left_side - right_side
            answer = str(solve(expression)[0])
            copy(answer)
            print(answer + "\n")
        except Exception as e:
            print(str(e) + "\n")