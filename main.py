import random
import time
import os

dices = {
    1: (
        "┏━━━━━━━━━┓",
        "┃         ┃",
        "┃    ▪    ┃",
        "┃         ┃",
        "┗━━━━━━━━━┛"
    ),
    2: (
        "┏━━━━━━━━━┓",
        "┃  ▪      ┃",
        "┃         ┃",
        "┃      ▪  ┃",
        "┗━━━━━━━━━┛"
    ),
    3: (
        "┏━━━━━━━━━┓",
        "┃  ▪      ┃",
        "┃    ▪    ┃",
        "┃      ▪  ┃",
        "┗━━━━━━━━━┛"
    ),
    4: (
        "┏━━━━━━━━━┓",
        "┃  ▪   ▪  ┃",
        "┃         ┃",
        "┃  ▪   ▪  ┃",
        "┗━━━━━━━━━┛"
    ),
    5: (
        "┏━━━━━━━━━┓",
        "┃  ▪   ▪  ┃",
        "┃    ▪    ┃",
        "┃  ▪   ▪  ┃",
        "┗━━━━━━━━━┛"
    ),
    6: (
        "┏━━━━━━━━━┓",
        "┃  ▪   ▪  ┃",
        "┃  ▪   ▪  ┃",
        "┃  ▪   ▪  ┃",
        "┗━━━━━━━━━┛"
    ),
}

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    res = input("Quantas vezes você quer que o dado role (uma vez tem efeitos)? ")
    try:
        res = int(res)
    except:
        return print("Você deve colocar um número válido.")
    if res <= 0:
        return print("Você deve colocar um número válido.")
    if res == 1:
        clock = 0.5
        for i in range(0, 5):
            os.system('cls' if os.name == 'nt' else 'clear')
            n = random.randint(1, 6)
            for line in dices.get(n):
                print(line)
            print()
            time.sleep(clock)
            clock += 0.5
    else:
        diceList = []
        for _ in range(0, res):
            diceList.append(random.randint(1, 6))
        for line in range(0, 5):
            for dice in diceList:
                print(dices.get(dice)[line], end="")
            print()

if __name__ == "__main__":
    main()
    print("Código feito por mi66mc#7969...")