from functools import reduce

def lyginiu_sandauga(skaiciai):
    lyginiai = [sk for sk in skaiciai if sk % 2 == 0]
    sandauga = reduce(multiply, lyginiai)
    return sandauga

def multiply(x, y):
    return x * y

def nelyginiu_kvadratai(skaiciai):
    nelyginiai_kvadratai = [sk ** 2 for sk in skaiciai if sk % 2 != 0]
    return nelyginiai_kvadratai

skaiciai = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lyginiu_sandauga_resultatas = lyginiu_sandauga(skaiciai)
nelyginiu_kvadratai_resultatas = nelyginiu_kvadratai(skaiciai)

print("Lyginių skaičių sandauga:", lyginiu_sandauga_resultatas)
print("Nelyginių skaičių kvadratai:", nelyginiu_kvadratai_resultatas)
