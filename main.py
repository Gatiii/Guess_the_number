import random


def hint_one():
    if random_number % 2 == 0:
        print("HINT 1: Your number is even")
    else:
        print("HINT 1: Your number is odd")


def hint_two():
    if random_number <= 0 and random_number >= 20:
        print("HINT 2: Liczba jest z przedziału 0 - 20")
    elif random_number > 20 and random_number <= 40:
        print("HINT 2: Liczba jest z przedziału 20 - 40")
    elif random_number > 40 and random_number <= 60:
        print("HINT 2: Liczba jest z przedziału 40 - 60")
    elif random_number > 60 and random_number <= 80:
        print("HINT 2: Liczba jest z przedziału 60 - 80")
    elif random_number > 80 and random_number <= 100:
        print("HINT 2: Liczba jest z przedziału 80 - 100")


def hint_three():
    if random_number % 3 == 0:
        print("HINT 3: Your number can be divided by three")
    else:
        print("HINT 3: Your number can't be divided by three")


def hint_four():
    if user_number5 > random_number:
        print(f"HINT: number is too high")
    else:
        print(f"HINT: number is too low")


random_number = random.randrange(1, 101)
user_number1 = int(input("put your first random guess: "))

if user_number1 == random_number:
    print(f"Congratulations you're correct. The number was {random_number}")
else:
    print("You're wrong")
    print(hint_one())

    user_number2 = int(input("put your second guess: "))

    if user_number2 == random_number:
        print(f"Congratulations you're correct. The number was {random_number}")
    else:
        print("You're wrong")
        print(hint_two())

        user_number3 = int(input("put your third guess: "))

        if user_number3 == random_number:
            print(f"Congratulations you're correct. The number was {random_number}")
        else:
            print("You're wrong")
            print(hint_three())

            user_number4 = int(input("put your fourth guess: "))

            if user_number4 == random_number:
                print(f"Congratulations you're correct. The number was {random_number}")
            else:
                print("You're wrong")
                for i in range(1, 4):
                    user_number5 = int(input(f"put your next guess: "))
                    print(hint_four())
                    if user_number5 == random_number:
                        print(f"Congratulations you're correct. The number was {random_number}")
                        break
