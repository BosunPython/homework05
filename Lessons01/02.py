import random

Rock = 1
Scissors = 2
Paper = 3

player = int(input("Выберите один из вариантов: Rock=1/Scissor=2/Paper=3 "))
bot = random.randint(1,3)

if bot == player:
    print(bot)
    print("ничья")
elif bot > player:
    print(bot)
    print("проиграл")
elif bot < player:
    print(bot)
    print("ты выиграл")