import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Perform experiment
    HTs = []
    for i in range(100):
        if random.randint(0, 1):
            HTs.append('H')
        else:
            HTs.append('T')

    # Find a streak of six
    lastFlip = HTs[0]
    count = 1
    total = 0
    for i in range(1,100):
        if HTs[i] == lastFlip:
            count += 1
        else:
            # Store number of streaks
            total += bool(count//6)
            # Reset the counter
            count = 1
    numberOfStreaks+=bool(total)
    
print('Chance of streak: %s%%' % (numberOfStreaks/100))