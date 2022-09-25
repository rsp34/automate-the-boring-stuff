import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    try:
        int1 = random.randint(0,9)
        int2 = random.randint(0,9)
        response = pyip.inputInt(f'#{questionNumber+1}: {int1} x {int2} = ',allowRegexes=f'^{int1*int2}$',blockRegexes=[('.*', 'Incorrect!')],timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1
    time.sleep(1) # Brief pause to let user see the result.

print(f'Score: {correctAnswers}/{numberOfQuestions}')