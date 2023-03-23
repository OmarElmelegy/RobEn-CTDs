import random
while True:
    print("Choose the game you want to start or enter 'exit' to exit:\n1 - Toss a coin\n2 - Get a random number\n3 - Random Choice")
    x = input("Your choice: ")
    if x == '1':
        #Game 1 goes here
        coin = ["Heads","Tails"]
        print(f"A coin was tossed and it landed on: {random.choice(coin)}")
    elif x == '2':
        #Game 2 goes here
        while True:
            try: 
                y1,y2  = input("Enter two numbers seperated by a comma: ").split(",")
                print(random.randint(int(y1),int(y2)))
            except ValueError:
                print("Enter valid input..")
                continue
    elif x == '3':
        #Game 3 goes here
        choice = random.choice(input("Enter list of Choices: ").split())
        print(f"Your random choice is: {choice}")
    elif x == "exit":
        print("You ran out of arcade coins, see you soon..")
        break;
    else :
        continue