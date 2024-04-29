#
print("welcome to the tip calculator.")
total_amount_bill=float(input("what was the total amount of bill? $"))
tip=int(input("what percentage tip you would like to give? "))
peolpe=int(input("How many peolpe to split the bill? "))

tip_cal=total_amount_bill*(tip/100)
split_bill=(total_amount_bill+tip_cal)/peolpe
split_bill_twodec=round(split_bill,2)
split_bill_twodec="{:.2f}".format(split_bill)
print(f"Each person should pay:${split_bill_twodec}")
 