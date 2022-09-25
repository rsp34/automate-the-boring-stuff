import random, time
from timeit import default_timer as timer

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    start = timer()
    attempts = 1
    int1 = random.randint(0, 9)
    int2 = random.randint(0, 9)

    while True:
        response = input(f"#{questionNumber+1}: {int1} x {int2} = ")
        attempts += 1
        if response.isnumeric() and int(response) == int1 * int2:
            print("Correct!")
            correctAnswers += 1
            break
        if timer() - start > 8:
            print("Out of time!")
            break
        if attempts > 3:
            print("Out of tries!")
            break
    time.sleep(1)  # Brief pause to let user see the result.

print(f"Score: {correctAnswers}/{numberOfQuestions}")
