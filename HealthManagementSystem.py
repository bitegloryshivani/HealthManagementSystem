#Health Management System
# 3 clients -shivu ,Manu and Sweta
# 3 files for food log and 3 files for Excercise log(to enter the data with time stamp)
#first input - lock or retrieve
#second input- for whom (name= 1 for Harry)
#third - what u want to log?exercise or diet

import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food\n"))
        if (c == 1):
            value = input("type here\n")
            with open("shivani-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully added")
        elif (c == 2):
            value = input("type here\n")
            with open("shivani-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully added")
    elif (k == 2):
        c = int(input("Enter 1 for exercise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("manu-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully added")
        elif (c == 2):
            value = input("type here\n")
            with open("manu-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully added")
    elif (k == 3):
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("sweta-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully added")
        elif (c == 2):
            value = input("type here\n")
            with open("sweta-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully added")
    else:
        print("plz enter valid input (1(Shivani),2(Manu),3(Sweta)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            with open("shivani-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("shivani-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 2):
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            with open("manu-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("manu-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            with open("sweta-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("sweta-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (Shivani,Manu,Sweta)")


print("********Health management system:*********** ")
a = int(input("Press 1 for log the value and 2 for retrieve\n "))

if a == 1:
    b = int(input("Press 1 for Shivani 2 for Manu 3 for Sweta\n "))
    take(b)
else:
    b = int(input("Press 1 for Shivani 2 for Manu 3 for Sweta\n "))
    retrieve(b)
