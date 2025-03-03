saldo = 200
limite = 1000
saque = 100

print(saldo > limite and saldo == limite)
print(saque <= saldo or saque < saldo)

expressao = (saldo > limite and saldo == limite) or (saque <= saldo or saque < saldo)
print(expressao)
# operadores AND ("e" só fica TRUE se as duas condicionais forem verdadeiras)
# operadores OR ("ou" fica TRUE se alguma das condicionais forem vedadeiras)
# pode se suar NOT para fazer a negação (se a condição original for TRUE, vai vir FALSE e vice-versa)
# dentro do parênteses é usado para dar sentido de condição (indentear a lógica tb)
print(not expressao)

# true and true = v
# true and false = F
# false and false = F
# true or true = v
# true or false = v
# false or false = F

# No AND ara ser true tem que ser todos V
# No OR precisa apenas de um true para ser V