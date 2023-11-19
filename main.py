words_easy = { 
    "family":"семья", 
    "hand": "рука", 
    "people":"люди", 
    "evening": "вечер",
    "minute":"минута", 
}

words_medium = { 
    "believe":"верить", 
    "feel": "чувствовать", 
    "make":"делать", 
    "open": "открывать",
    "think":"думать", 
}

words_hard = {
    "rural":"деревенский", 
    "fortune": "удача", 
    "exercise":"упражнение", 
    "suggest": "предлагать",
    "except":"кроме", 
}

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

answers = {}

words = None

user_input = input('Введите уровень сложности.\n'
                   'Легкий, средний, сложный.\n')

if user_input.lower() == 'легкий':
    words = words_easy
elif user_input.lower() == 'средний':
    words = words_medium
elif user_input.lower() == 'сложный':
    words = words_hard


for key, value in words.items():
    print(f'{key}, {len(value)} букв, начинается на {value[0]}...')
    user_input = input('Ваш ответ: ')

    if user_input.lower() == words[key]:
        print(f'Верно, {key.title()} — это {value}.')
        answers[key] = True
    else:
        print(f'Неверно. {key.title()} — это {value}.')
        answers[key] = False

answers_list = list(answers.values())

print('Правильно отвечены слова: ')
for key, value in answers.items():
    if value:
        print(key)

print('Неправильно отвечены слова: ')
for key, value in answers.items():
    if not value:
        print(key)

print('Ваш ранг:\n'
      f'{levels[len(list(filter(lambda x: x == True, answers_list)))]}')


