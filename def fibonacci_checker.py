def fibonacci_checker(num):
    if num < 0:
        return False
    
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    
    return b == num

numero = 21

if fibonacci_checker(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")
