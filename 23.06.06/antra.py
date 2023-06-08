def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci_generator()

print(next(gen))  # Rezultatas: 0
print(next(gen))  # Rezultatas: 1
print(next(gen))  # Rezultatas: 1
print(next(gen))  # Rezultatas: 2
print(next(gen))  # Rezultatas: 3
print(next(gen))  # Rezultatas: 5
# ir t.t., gauti kiekvieną sekantį Fibonačio sekos skaičių
