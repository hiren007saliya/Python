print("welcome to pizza deliveries")
size=input("what is the size you want? S,M or L")
add_pepperoni=input("do you want peppperon? Y or  N ")
extra_chesse=input("do you want extra chesse? Y or N ")
bill=0

if size=="S":
    bill += 15
elif size=="M":
    bill += 20
elif size=="L":
    bill += 25

if add_pepperoni == "Y":
    if size =="S":
        bill += 2
    else:
        bill += 3

if extra_chesse == "Y":
    bill += 2

print(f"your final bill is ${bill}")