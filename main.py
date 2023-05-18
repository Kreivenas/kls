from file1 import cube as raise_cube
from utils.file2 import pi_constant
from file3 import square_root


def main():
    number = float(input("Įveskite skaičių: "))

    result1 = raise_cube(number)
    result2 = result1 * pi_constant
    result3 = square_root(result2)

    print("Galutinis rezultatas:", result3)


if __name__ == '__main__':
    main()
