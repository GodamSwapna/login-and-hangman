import random
print("*****Well Come to The Cow and Bull Game******")

def bull():
    return "******Bull*****"


def cow():
    return "******Cow******"


def main(secret_numbers,guessed_numbers):
    user_name=input("Enter you are name :")
    index=0
    correct_position=[]
    guessed_num=[]
    while index<len(guessed_numbers):
        guess_num=int(input("ente you are guessing number:"))
        choose_pos=int(input("enter position of guessed number :"))
        # sec_pos=index(secret_numbers[guess_num])
        if guess_num in secret_numbers:
            sec_pos=secret_numbers.index(guess_num)
            if choose_pos==sec_pos:
                print(bull())
                correct_position.insert(choose_pos,guess_num)
            else:
                print(cow())
                print("”These are correct numbers you can reuse it”")
                guessed_num.append(guess_num)
                print("guessednumbers :",guessed_num )
        else:
            print("You are Guessing number is Wrong")
        index+=1
    if correct_position==secret_numbers:
        print("Congratulation" + user_name + "You are the winner")
    else:
        print("Oops you are the looser")

list1=[0,1,2,3,4,5,6,7,8,9]
list2=random.sample(list1,5)
print(list2)
server=input("Do you want to play this game :")
if server=="yes":
    main(list2,list1)
else:
    print("user quit from the Game")
























# l=[0,1,2,3,4,5,6,7,8,9]
# l = [0, 1, 2, 3, 4]
# print(random.choices(l, k=3, weights=[1, 1, 10,1, 1, 1]))
# # [0, 2, 3]

# print(random.choices(l, k=3, weights=[1, 1, 0, 0, 0]))
# # [0, 1, 1]





