weight = float(input("what is your weight?: "))
measurement = input("(k)gs or (l)bs: ")
if measurement.upper() == "L":
    convert = weight / 0.45
    print("weight in lbs: " + str(convert))
else:
    convert = weight * 0.45
    print("weight in kgs: " + str(convert))
