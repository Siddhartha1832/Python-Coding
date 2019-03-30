print("\n *** Find Factors of Given Number *** \n")

factor = int(input(" Enter the factor number : "))

result = [i for i in range(1, factor + 1) if factor % i == 0]

print("\n Factors of {} is {} ".format(factor,result))
