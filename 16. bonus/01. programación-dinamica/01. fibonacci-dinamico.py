import sys


def fibonacci_recursivo(n):
    # Implementación Sucesión Fibonacci Recursiva
    if (n == 0 or n == 1):
        return 1
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


def fibonacci_dinamico(n, memoization={}):
    ''' Implementación sucesión fibonacci de manera dinámica '''
    if n == 0 or n == 1:
        return 1
    try:
        return memoization[n]
    except KeyError:
        resultado = fibonacci_dinamico(
            n-1, memoization) + fibonacci_dinamico(n-2, memoization)
        memoization[n] = resultado
        return resultado


if __name__ == "__main__":
    # resultado = fibonacci_recursivo(100)
    # print(resultado, end="\n")
    resultado_dinamico = fibonacci_dinamico(500)
    print(resultado_dinamico)
