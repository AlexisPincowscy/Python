# Variáveis podem mudar durante o execucção do algoritmo

name = "Alexis"
age = 36
print(f'Meu nome é {name} e tenho {age} anos.')

name = "Carlos"
age = 11
print(f'Meu nome agora é {name} e minha idade mudou poara {age}')
# nesse exemplo acima, começou com um nome e uma idade e foi alterado durante o curso da execucção

# python NÃO tem constante, para declarar constante usamos a convenção de letras maiúsculas e sanke case(_ para separar palavras)

NOME_ALUNO = "Lígia"
IDADE_ALUNO = 32
print(f'O alun@ {NOME_ALUNO} tem {IDADE_ALUNO} anos')
# aqui esses valores não devem mudar durante as próximas etapas.
# FICAR ATENTO PQ O PYTHIN VAI DEIXAR ISSOA ACONTECER!!

# você pode definir variáveis tudo de uma vez
# só separar por vírgulas
name, age, ESTADO = "Aelxandre" , 25 , ["DF", "SP", "ES"]
print(f'O {name}, que tem {age} anos, mora no {ESTADO}.')