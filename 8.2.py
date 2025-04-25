import random  

def function():
    numbers = set()
    for i in range(10):
            a=random.randrange(15,45)
            numbers.add(a)
    
    print("original:", numbers)

    counter = sum(1 for i in numbers if i < 30)
    print("numbers less than 30:", counter)

    remover = {i for i in numbers if i <= 35}
    print("Set after removing numbers > 35:", remover)

function()
