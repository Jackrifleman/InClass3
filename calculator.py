#Jackson Eubank
#CS 362
#InClass 3

def add(a,b):
    return a + b;

def subtract(a,b):
    return a - b;

def multiply(a,b):
    return a * b;

def divide(a,b):
    if (b == 0):
        raise ValueError('Cannot divide by zero!');
    return a / b;
