print("welcome to the love calculator")
name1=input("what is your name? \n")
name2=input("what is their name? \n")

comb_str = name1+name2
low_case=comb_str.lower()
t=low_case.count("t")
r=low_case.count("r")
u=low_case.count("u")
e=low_case.count("e")

true = t+r+u+e

l=low_case.count("l")
o=low_case.count("o")
v=low_case.count("v")
e=low_case.count("e")

love = l+o+v+e

love_score = int(str(true)+str(love))
#print(love_score)

if (love_score < 10) or (love_score >90):
    print(f"your love score is {love_score}, you can go for dinner")
elif (love_score >= 40) and (love_score <= 50):
    print(f"your love score is {love_score}, you are alright togather")
else:
    print(f"your score is {love_score}, you can find new person for better future")