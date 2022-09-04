from random import randrange

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

cntPw = int(input('Укажите количество паролей для генерации:'))
lenPw = int(input('Укажите длину одного пароля:'))
digOn = input('Включать ли цифры 0123456789? (y/n)')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')

def chars_kit(): #Формирование переменной из нужного набора символов
    global chars
    if digOn == 'y':
        chars += digits
    if ABCon == 'y':
        chars += lowercase_letters
    if abcOn == 'y':
        chars += lowercase_letters
    if chOn == 'y':
        chars += punctuation
    return chars

def generate_password(lenght, chars): #функция генератора паролей
    global cntPw
    global rand_num
    while cntPw != 0:
        new_password = ''
        for i in range(lenPw):
            rand_num = randrange(len(chars))
            if excOn == 'y':
                examonation_ambiguous_characters()
            new_password += chars[rand_num]
        cntPw -= 1
        print(new_password)

def examonation_ambiguous_characters(): #проверка на неоднозначные числа
    global rand_num
    while chars[rand_num] in 'il1Lo0O':
        rand_num = randrange(len(chars))
    return rand_num

generate_password(lenPw, chars_kit()) #основнвя функция