import random
students = ['Tom', 'Sally', 'Betty', 'Eric', 'Angela', 'Stephany']

for i in range(1, 5):
    print(random.choice(students))

fruits = ['apple', 'banna', 'lemon']
my_fruit = random.sample(fruits, 2)
print(my_fruit)

my_int = random.randint(0, 10)

for i in range(1, 10):
    print(my_int)