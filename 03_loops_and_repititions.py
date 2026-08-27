import random

response = ""
rand_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

print("Welcome to my program!")

while response != "3":
    print("")
    print("1. Tell me a joke")
    print("2. Give me a random number 1-10")
    print("3. Quit")
    
    response = input("What would you like to do? ")
    
    if response == "1":
        print("What do you call a cow with no legs? Ground beef!") 
    elif response == "2":
        print(random.choice(rand_num))
    elif response == "3":
        print("Goodbye!") 
    else:
        print("Try again!")