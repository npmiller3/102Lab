# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(1,9):
        num0 = 0
        num1 = 1
        currNum = fibs[num0] + fibs[num1]
        fibs.append(currNum)
        num0++
        num1++
    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()

