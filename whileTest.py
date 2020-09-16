phrase = "zopa"
start = True
while start:
    guess = input("Введите слово : ")
    if guess == phrase:
        print("Фраза совпала!")
        start = False
    else:
        print("Гавной воняет")
else:
        print("Цикл закончен")
print("FIN")