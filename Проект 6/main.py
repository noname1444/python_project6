win = False

counter = 0

points = [0, 0, 0]
all_letters = []
true_letters = []

secret_word = input("Введите слово для игры: ")
print("\033[2J")

while win == False:
    letter = input(f"\n\nИгрок {counter + 1}, введите букву: ")
    if letter in all_letters:
        print("Вы уже вводили эту букву")
    elif letter in secret_word:
        print("Вы угадали букву")
        true_letters.append(letter)
        points[counter] += 1
        win = True
        print("Ваши очки: ", points[counter])
    else:
        print("Такой буквы нет в слове")
    all_letters.append(letter)
    for letter in secret_word:
        if letter in true_letters:
            print(letter, end="")
        else:
            print("*", end="")
            win = False
    if win == False:
        counter = (counter + 1) % 3
print(f'''\n\nОчки игроков:
Игрок 1: {points[0]}
Игрок 2: {points[1]}
Игрок 3: {points[2]}''')
