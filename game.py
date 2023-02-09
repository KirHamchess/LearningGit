import random
secret = random.randint(1, 100)
guess = 0
tries = 0
print ("Компьютер: Привет! давно не виделись. Как же я по тебе скучал! Давай поиграем!")
print ("Вы: А во что?")
print ("Компьютер: В числа! числа от 1 до 100!")
print("Вы: Ну, давай попробуем.")
while guess != secret and tries < 10:
    guess = int(input("число:"))
    if guess < secret:
        print ("слишком мало!")
    elif guess > secret:
        print ("слишком много!")

    tries = tries + 1

if guess == secret :
    print ("Ты угадал. Давай еще разок!")
else:
    print ("У тебя закончились попытки. Жаль! :(")
    print ("это было число", secret)