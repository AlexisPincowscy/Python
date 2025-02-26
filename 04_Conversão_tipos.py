# aula de conversão de tipos no python
# vai imprimir apenas o inteiro
print(int(10.034))

# vai transformar um int em float
valor = 15
print(float(valor))

# vai transformar um float em string (muito usado)
valor = 10.50
valor_str = str(valor)
print("Eu comprei um produto com valor de R$:" + valor_str)

# int quando / vira float, mas usando // continua o Int
div = 10/2
print(div)
div_int= 10//2
print(div_int)