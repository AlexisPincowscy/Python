import pyautogui #biblioteca para automação de mouse e teclado

pyautogui.PAUSE = 0.5 # Pausa de 0.5 segundos entre cada ação

pyautogui.press('win') 
pyautogui.write('microsoft edge')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

pyautogui.sleep(1) # Espera 1 segundos para a página carregar

pyautogui.click(x=695, y=361)
pyautogui.write("teste@teste.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.click(x=912, y=527)

pyautogui.sleep(2)

import pandas as pd

tabela = pd.read_csv("Automação/produtos.csv")
print(tabela)

# Acessar a página de produtos

for i in tabela.index: 
        pyautogui.click(x=721, y=244)

        codigo = tabela['codigo'] # ou tabela.loc[i (a linha), 'codigo' (a coluna)]  
        pyautogui.write(codigo[i]) # se usar o de cima não precisa do i

        pyautogui.press('tab')
        marca = tabela['marca'] 
        pyautogui.write(marca[i])

        pyautogui.press('tab')  
            
        tipo = tabela['tipo']
        pyautogui.write(tipo[i])

        pyautogui.press('tab')
        categoria = tabela['categoria']
        pyautogui.write(str(categoria[i]))

        pyautogui.press('tab')
        preco_unitario = tabela['preco_unitario']
        pyautogui.write(str(preco_unitario[i]))

        pyautogui.press('tab')
        custo = tabela['custo'] 
        pyautogui.write(str(custo[i]))

        pyautogui.press('tab')
        obs = tabela.loc[i, 'obs']
        if pd.isna(obs):
            pyautogui.write('')
        else:
            pyautogui.write(str(obs))

        pyautogui.press('tab')
        pyautogui.press('enter')

        pyautogui.scroll(10000) # fazer scroll para topo da tela, négativo irira para baixo
        