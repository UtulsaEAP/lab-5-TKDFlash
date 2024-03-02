def fibonacci(n):
    #write your code here

    if n < 0:
        return -1
    
    fib0, fib1 = 0, 1

    for _ in range(n):
        fib0, fib1 = fib1, fib0 + fib1
        
    return fib0

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')