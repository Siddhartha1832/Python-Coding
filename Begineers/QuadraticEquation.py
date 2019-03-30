import cmath
print("\n *** Quadratic Equation *** \n")

first_value = int(input(" Enter the first value : "))
second_value = int(input(" Enter the second value : "))
third_value = int(input(" Enter the third value : "))

calc = (second_value ** 2) - (4 * first_value * third_value)
solution1 = (-second_value - cmath.sqrt(calc)) / (2 * first_value)
solution2 = (-second_value + cmath.sqrt(calc)) / (2 * first_value)

print("\n The solutions are {0} and {1} \n".format(solution1, solution2))