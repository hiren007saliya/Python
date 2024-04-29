#
height=int(input("what is your height(cm): "))

bill=0

if height>120:
    print("allowe for ticket")
    age=int(input("what is your age?: "))
    if age<12:
        bill=3
        print("child tickets are $3.")
    elif age<=18:
        bill=5
        print("youth tickets are $5.")
    elif age>=45 and age <= 55:
        print("you can ride free of cost")
    else:
        bill=10
        print("elder tickets are $10.")

    photo=input("you want take a photo? Y or N. ")
    if photo =="Y":
        bill += 3

    print(f"your final bill is ${bill}")

else:
    print("do not allowe for ticket") 

