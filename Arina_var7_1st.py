from random import shuffle
mainSq = [1, 2, 3, 4, 5, 6, 7, 8, 9]

aPoints = 0
bPoints = 0

shuffle(mainSq)
print (mainSq[0:3])
print (mainSq[3:6])
print (mainSq[6:9])
cnt = 0
dic = {
    
}
alrdy = {}
for i in range(0, 9):
    dic[mainSq[i]] = i # присваиваем индексы числам из нашей таблицы, чтоб быстро доставать их из массива
    alrdy[i + 1] = 0 #словарь использованных чисел

print("Выбирай любое число")

def endgame():
    if (aPoints > bPoints):
        print ("1st player WON!")
    elif (aPoints < bPoints):
        print ("2nd player WON!")
    else:
        print ("Draw!")


# присуждение очков и помечаем, что число выбрано и больше выбираться не сможет
def f (x):
    mainSq[dic[x]] = '' # в таблице помечаем число выбранным и не отображаем его
    alrdy[x] = 1 # помечаем что выбрали
    if (cnt == 9): # условие конца игры
        endgame()
    return x



# проверка на корректность ввода данных
def check(ch, tr, ls):
    if (tr == 0):
        if (ls // 3 == dic[ch] // 3):
            return False
        else:
            return True
    if (ls % 3 == dic[ch] % 3):
        return False
    else:
        return True

    

turn = 0 #определяем через turn чей ход. 0/1.
chosen = int(input()) #игрок выбрал впервые число
last = dic[chosen] #нам надо запоминать какое число выбрал игрок, чтобы для оппонента определять корректность ввода
aPoints = f(chosen) #присудили ему очки и пометили его число использованным
cnt += 1
anyChosing = 0
while (True):
    print (mainSq[0:3])
    print (mainSq[3:6])
    print (mainSq[6:9])
    if (anyChosing):
        print ("Ход перешел, выбирай любое число")
    elif (turn == 1):
        print ("Выбери число из " + str(last % 3 + 1) + " столбца")
    else:
        print("Выбери число из " + str(last // 3 + 1) + " строки")
    chosen = int(input())
    errors_cnt = 0
    error_flag = 0
    while (True): # пока чел не выберет корректное число, будет просить его выбрать заново
        if (errors_cnt == 3):
            error_flag = 1
            break
        if (anyChosing):
            break
        if (check(chosen, turn, last)): #функция проверки на верный столбец и строчку (про деление на 3 и остаток на 3)
            if (turn == 0):
                print ("WARNING!\nВыбери число из строки оппонента")
            else:
                print ("WARNING!\nВыбери число из столбца оппонента")
        elif (alrdy.get(chosen) == 1):
            print ("Это число уже забрали")
        else:
            break
        print ("Осталось попыток:", 3 - errors_cnt)
        errors_cnt += 1
        chosen = int(input())
    #причисление очков
    if (error_flag):
        turn = (turn + 1) % 2
        anyChosing = 1
        print ('Переход хода, выбирай любое число')
        continue
    if (turn == 0):
        bPoints = bPoints + f(chosen)
    else:
        aPoints = aPoints + f(chosen)
    
    cnt += 1
    #прчисление очков
    turn = (turn + 1) % 2 #меняем ход
    last = dic[chosen] #меняем последний взятый элемент
    print ("Player A points:" + str(aPoints))
    print ("Player B points:" + str(bPoints))
    if (aPoints + bPoints == 45):
        if (aPoints > bPoints):
            print ("Игрок А выиграл")
        elif (aPoints < bPoints):
            print ("Игрок B выиграл")
        else:
            print ("Ничья")
        break
    anyChosing = 0