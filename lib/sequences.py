#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    for x in range(length):
        if(x == 0):
            fib_list.append(0)
        elif(x == 1):
            fib_list.append(1)
        else:
            fib_list.append(fib_list[x-1] + fib_list[x-2])

    print(fib_list)
    
    pass