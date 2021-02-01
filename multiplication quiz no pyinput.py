import random, time

number_of_questions = 10
correct_answers = 0
for question_number in range(number_of_questions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s x %s = ' % (question_number, num1, num2)
    print(prompt)

    while time.time() < 8 and i in range(1,4):
        answer = input()

print('Score: %s / %s' % (correct_answers, number_of_questions))
