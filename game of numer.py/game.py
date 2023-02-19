import random

onemoretime = "д"
print ("Компьютер: Привет! давно не виделись. Как же я по тебе скучал! Давай поиграем!")
print ("Вы: А во что?")
print ("Компьютер: В числа! числа от 1 до 500!")
print("Вы: Ну, давай попробуем.")
while onemoretime == "д":
    guess = 0
    tries = 0
    secret = random.randint(1, 500)
    while guess != secret and tries < 10:
        print("Попытка №{}".format(tries+1))
        guess = int(input("число:"))
        if guess < secret:
            print ("слишком мало!")
        elif guess > secret:
            print ("слишком много!")
            
        tries = tries + 1

    if guess == secret :
        print ("Ты угадал. Давай еще разок!")
        print("(ну вот как ты угадываешь-то...)")
    else:
        print ("У тебя закончились попытки. Жаль! :(")
        print ("это было число", secret)
        
    onemoretime = input("Хочешь попробовать еще раз? да/нет ")
