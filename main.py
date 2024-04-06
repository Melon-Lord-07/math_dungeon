import time
print("hello world")
time.sleep(2)
print("get ready to perish...")
time.sleep(0.5)

print("3...")
time.sleep(0.5)

print("2...")
time.sleep(0.5)

print("1...")
time.sleep(0.5)

attack = str(input("A monsters here !! Quick! To attack, type the smallest number that's a mutiple"
                   " of the numbers 1-20!!"))

if attack == "232792560":
    print("you beat the monster! good job")

    print("you are walking in the dungeon, when suddenly.. a little man appears!")
    time.sleep(3)
    print("his name is myrial. he is a single father of 3, and recently he became a grandfather")
    print("you should congratulate him!")
    time.sleep(3)
    print("to congratulate him, solve the following math problem:")
    print("what is the 6th element of the 8th row of pascals triangle (google it if u dunno")
    time.sleep(3)
    answer = str(input("so??"))
    if answer == "21":
        print("hes very happy! he shows you photos of his grandchildren then gives u a carved toy he made then leaves")
        time.sleep(3)
        print("the carved toy has come to life! the little man wanted to share the miracle of childbirth with you")
        answer = input("considering that you give birth to the child from the ground at an angle of 20 degrees, and the"
                       " child is born at a speed of 15m/s, how many meters does the baby travel rounded to 2 decimals"
                       "in meters, assuming there is no air resistance and you have a spherical baby")
        if answer == "7.85":
            print("you have sucessfully given birth! you are now a proud parent and feeling fulfilled")

            answer = input("the excitement of childbirth fills your body with electricity! if it is 20 volts and 4 amps"
                           ", calculate the resistance in ohms")
            if answer == "5":
                print("good job!")
            else:
                print("you didnt resist properly and you turn into an electric eel man who is shunned from society.")
        else:
            print("you are a failure of a parent and your kids move out immediately once they are of legal age")

    else:
        print("myrial is offended and brutally murders you. you lose.")

else:
    print("you died")
    time.sleep(0.5)
    print("bitch")
