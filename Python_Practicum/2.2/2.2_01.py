print('Как Вас зовут?')
name = str(input())
print(f'Здравствуйте, {name}!')
print('Как дела?')
mood = str(input())
if mood == 'хорошо':
    print('Я за вас рада!')
elif mood == 'плохо':
    print('Всё наладится!')
