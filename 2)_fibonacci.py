def is_fibonacci(num):
    if num < 0:
        return False
    
    fibo1, fibo2 = 0, 1
    
    if num == 0 or num == 1:
        return True
    
    while fibo2 <= num:
        fibo_proximo = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibo_proximo
        
        if fibo2 == num:
            return True
    
    return False


num = int(input("Informe um número: "))

if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
