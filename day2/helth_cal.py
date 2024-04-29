height=input("enter your height in meter: ")
weight=input("enter your weight in kg: ")

BMI=int(weight)/float(height)**2
bmi_int=round(BMI,2)
print(bmi_int)

