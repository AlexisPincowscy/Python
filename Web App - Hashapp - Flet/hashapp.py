# Criar um sistema de chat virtual

# Título: HashZap
# Botão: Iniciar Chat
    # quando clicar no botão:
    # Janela/ PopUp
        # Título: Bem-vindo ao Chat
        # Escreva seu nome
        # Botão: Entrar no chat
            # clicou no botão
            # fechar o PopUp
                # criar chat
                # cair o campo de mensagem
                # botão Enviar mensagem
                    # enviar mensagem ao clicar no botão

# importar o flet -> framework utilizado na construção

import flet as ft

# criar a função principal (main) do app, é o nome padrão no uso do flet
def main(pagina):
# criar os elementos
    titulo = ft.Text("Meu chat", size=35)

    

    def enviar_mensagem(evento):
        texto_mensagem = ft.Text(campo_mensagem.value) # pega o texto que o usuário escreve no campo da mensagem
        campo_mensagem.value = ""
        chat.controls.append(texto_mensagem) # acrescenta no chat
        pagina.update()

    # criando o padrão do chat
    campo_mensagem = ft.TextField(label="Escreva sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar mensagem", on_click=enviar_mensagem)
    chat = ft.Column()
    linha_mesagem = ft.Row([campo_mensagem, botao_enviar])


    # criando funcioanlidade no botão entrar
    def entrar_chat(evento):
        # fechar o Dialog/popup
        janela.open = False
        # remover o título e o botão iniciar
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)

        # criar chat
        pagina.add(chat)
        # acrescentar o campo de mensagem e o botão enviar mensagem
        pagina.add(linha_mesagem)
        # atualiza a pag automaticamente
        pagina.update()

    campo_nome = ft.TextField(label="Digite seu nome", on_submit=entrar_chat) # área de texto
    botao_entrar = ft.ElevatedButton("Entrar no chat!", on_click=entrar_chat, bgcolor="red")


    # criando o popup/dialog
    titulo_janela = ft.Text("Bem vindo ao Chat")
    
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome, actions=[botao_entrar], open=True)

    def abrir_popup(evento): # no flet é necessário passar o evento como parâmetro
        pagina.open(janela)
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton("Iniciar o Chat", on_click=abrir_popup)
    
# colcoar os elementos na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# rodar o seu app
ft.app(main)