def Choice():
    choice = int(input("Enter (1) for HowBigCanuGet or (2) for SocialButterfly: "))
    if choice == 1:
        HowBigCanuGet()
    elif choice == 2:
        SocialButterfly()


def HowBigCanuGet(): 
    x = []
    while True:
        In = input("insert number: ")
        if In == 'q':
            break
        else:
            x.append(int(In))
        print(x)
    print(f"Largest number is {max(x)}\nSmallest number is {min(x)}")


def SocialButterfly():
    Friends1 = []
    Friends2 = []
    while True:
        In = input("User1: ")
        if In == 'q':
            break   
        else:
            Friends1.append(In)
    while True:
        In = input("User2: ")
        if In == 'q':
            break
        else:
            Friends2.append(In)
    print(f"The mutual friends are: {list(set(Friends1).intersection(Friends2))}")
    print(f"The mutual friends are: {[x for x in Friends1 if x in Friends2]}")
Choice()