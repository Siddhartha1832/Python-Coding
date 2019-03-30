print("\n *** Conversion of Kilometers to Miles & Vice Versa *** \n")

value = float(input(" Enter Input Value : "))

conv_fac = 0.621371
miles = conv_fac * value
kilometers = miles / conv_fac

print("\n {} Kilometers is Equal to {} Miles.".format(round(value,2), round(miles,2)))
print("\n {} Miles is Equal to {} Kilometers. ".format(round(miles,2), round(kilometers,2)))