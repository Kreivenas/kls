def even_generator():
    num = 2
    while True:
        yield num
        num += 2

gen = even_generator()

print(next(gen))  # Rezultatas: 2
print(next(gen))  # Rezultatas: 4
print(next(gen))  # Rezultatas: 6
print(next(gen))  # Rezultatas: 8
# ir t.t., kiekvieną kartą grąžinant sekantį porinį skaičių
