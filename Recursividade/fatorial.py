def soma(n):
    if n == 1:
        return 1
    else:
        return n * soma(n - 1)
numero = 5
result = soma(numero)
print(f"o fatorial do {numero} é {result}")