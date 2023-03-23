#Get Choice from the user:
def GetChoice():
    while True:
        try : 
            c = int(input("Enter The number of Challenge u need the solution for, [1] or [2]: "))
            if(c == 1):
                Ch1Sol()
            elif(c == 2):
                Ch2Sol()
        except ValueError:
            continue

# Solution for the first challenge:
def Ch1Sol():
    sum = 0
    while True:
        try : 
            n = int(input("Enter a number: "))
            if(1 <= n < 942):
                break
        except ValueError:
            continue
    for i in range(n):
        sum += str(i).count('1')
    """
    There is another solution to this problem without using built in methods of strings..

    for i in range(n):
        x = i
        while(x > 0):
            rem = x%10
            if(rem == 1):
                sum += 1
            x //= 10
    """
    print(f"from 1 to {n} the number '1' shows up: {sum} times")
    exit()


#Solution for the Second Challenge:
import random

def Ch2Sol():
    bag = [4,2,0,6,9]
    for i in range(5):
        bag[i] = random.randint(0,1000)
    main(bag)

def main(bag):
    while(len(bag)>=5):
        print(f"The bag contains {len(bag)} numbers: {bag}")
        reply = GetOrder()
        if(reply == "remove"):
            if(len(bag) == 5):
                print("Bag can't have less than 5 items, enter another operation.")
                main(bag)
            else :
                RemoveItem(bag,GetItem())
        elif(reply == "enter"):
            AddItem(bag,GetItem())
        elif(reply == "sell"):
            SellBag(bag)

def GetOrder():
    while True:
            rep = input("Enter an operation: ")
            if( rep != "remove" and rep != "enter" and rep != "sell"):
                print("Enter a valid operation")
                continue
            else:
                return rep

def RemoveItem(bag,n):
    if(bag.count(n) != 0):
        bag.remove(n)
    else:
        print("The number doesn't exist in the bag, Enter another operation: ")
        GetOrder()

def AddItem(bag,n):
    bag.append(n)

def GetItem():
    while True:
        try : 
            return int(input("Enter a number: "))
        except ValueError:
            continue

def SellBag(bag):
    sum = 0
    for k in range(len(bag)):
        sum += bag[k]
    print(f"You sold the bag and you got {sum} farts worth of dollars")
    exit()

GetChoice()