def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


filename = 'tekstinis_failas.txt'
generator = read_file(filename)

for line in generator:
    print(line)
