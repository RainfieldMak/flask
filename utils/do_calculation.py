import sys

def add_numbers(num1, num2):
    result = int(num1) + int(num2)
    return str(result)

if __name__ == '__main__':
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    result = add_numbers(num1, num2)
    print(result)

