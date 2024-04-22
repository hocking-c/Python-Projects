print("Welcome to Treasure Island.")
print("Your mission is to find this treasure.")
print("Let us begin! You are at a crossroad where the path splits right or left.")
crossroads = input('Which way would you like to go? Type "right" or "left"\n').lower()
if crossroads == "right":
    print("Now we are at a the end of a pond where we need to decide whether to swim across or wait for our canoe to arrive.")
    pond = input('What would you like to do? Type "swim" or "wait"\n').lower()
    if pond == "wait":
        print("We've arrived to the other side of the pond and come to a log cabin with a front door, back door, and little window.")
        cabin = input('Which way would you like to enter the cabin? Type "front" , "back" , or "window".\n').lower()
        if cabin == "window":
            print("You have managed to get into the cabin and are rewarded with a chest of gold!")
        elif cabin == "back":
            print("Oh no, you have been spotted by the guard dogs and get mauled!")
        elif cabin == "front":
            print("Oh no, there was a hidden security camera that caught you and triggered the alarm!")
        else:
            print("You have entered an invalid input. Game over.")
    elif pond == "swim":
        print("Uh oh, there was a large school of piranha that quickly devour your flesh!")
    else:
        print("You have entered an invalid input. Game over.")
elif crossroads == "left":
    print("Ooops, not the smartest decision you've made. There was a trap there!")
else:
    print("You have entered an invalid input - Game over.")