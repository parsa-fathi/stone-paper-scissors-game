import random


def pc_choice():
    choice = random.choice(["st", "pa", "sc"])
    return choice


def user_message():
    print(
        """
    please choose your choice :

    1_stone :\t"st"
    2_paper :\t"pa"
    3_scissor :\t"sc"
    4_exit:\t"e"
        """
    )
    userinput = input("Your choice :\t")
    return userinput


options = {
    "stst": 0,
    "stpa": 1,
    "stsc": -1,
    "past": -1,
    "papa": 0,
    "pasc": 1,
    "scst": 1,
    "scpa": -1,
    "scsc": 0,
}


def main():
    pc = pc_choice()
    user = user_message()
    if user == "e":
        exit()
    print("My choice was :\t", pc)
    result = pc + user
    final = options.get(result, 2)
    if final == 1:
        print("You won!")
    elif final == 0:
        print("Tie!")
    elif final == -1:
        print("Computer won!")
    else:
        print("something went wrong")


while True:
    main()
