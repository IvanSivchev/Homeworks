x = 0

riddle = 'Who is Tanya? '
answer = 'kisa'
answer1 = 'Kisa'
question = input(riddle)

if question == answer or question == answer1:
    print('You are right!')
    x += 1
else:
    print('No!')


print('Next riddle!')


riddle = 'Where was Tanya last 12 days? '
answer = 'vietnam'
answer1 = 'Vietnam'
question = input(riddle)

if question == answer or question == answer1:
    print('You are right!')
    x += 1
else:
    print('No!')

riddle = "Tanya's favorite food? "
answer = 'pure'
answer1 = 'Pure'
question = input(riddle)

if question == answer or question == answer1:
    print('You are right!')
    x += 1
else:
    print('No!')


print('You guested ', x, ' times!')