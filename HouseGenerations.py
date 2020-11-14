import random
number_of_houses = 6
for n in range(number_of_houses):
    monthlyCare = random.randint(0, 1200)
    if monthlyCare < 500:
        monthlyCare = 0
    print("House {}, Street {}, {}, {}, {}".format(n+1,
                                                   n+1,
                                                   random.randint(40000, 90000),
                                                   random.randint(24, 96),
                                                   monthlyCare))