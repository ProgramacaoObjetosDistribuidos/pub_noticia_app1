# -*- coding: utf-8 -*-
__author__ = 'rafaeltavares'
import pygtk
import gtk
import loader
from string import replace
from classes import News

# Criando a Classe do Programa
class DesktopApp(object):
    def __init__(self):
        # Agora como eu havia dito vamos utilizar uma função da classe gtk.Builder
        # para carregar o arquivo XML gerado pelo Glade.

        builder = gtk.Builder()  # Primeiramente criamos uma instância da classe
        builder.add_from_file("DesktopApp.glade")  # Função para carregar o arquivo

        # Agora nós podemos acessar os widgets do arquivo XML, caso você tenha
        # alterado o nome de algum widget e não seguiu o tutorial exatamente como
        # eu fiz, preste atenção e utilize o nome que você definiu.
        # Caso não se lembre os nomes abra o arquivo XML no glade novamente e veja
        # os nomes na ávore de widgets do lado direito.
        # Utilizaremos a função get_object passando como parâmetro o nome do widget.

        # Obtendo o widget das janelas
        self.window = builder.get_object("windowMain")
        self.window_chat = builder.get_object("windowChat")
        self.window_notice = builder.get_object("windowNoticeDetails")
        self.notifications = (builder.get_object("label1"), builder.get_object("label2"), builder.get_object("label3"), builder.get_object("label4"), builder.get_object("label5"))

        # Obtendo os widgets de todos os componentes da janela de detalhes da noticia
        self.d_notice_title = builder.get_object("label_Title")
        self.d_notice_author = builder.get_object("label_Author")
        self.d_notice_content = builder.get_object("notice_text")
        self.d_notice_image = builder.get_object("image_notice")

        #Obtendo os widgets de todos os componentes da janela de chat
        self.c_view_message = builder.get_object("view_messages")
        self.c_text_message = builder.get_object("text_message")

        #Obtendo os widgets de todos os componentes da janela principal

        #ainda precisa mapear

        # Exibindo a janela do programa
        self.window.show()

        # Agora nós iremos conectar os sinais que definimos para cada widget no
        # Glade Para isso usamos a função connect_signals(). Se você definiu o nome
        # de algum sinal de um modo diferente dos que eu utilizei preste atenção
        # nessa parte e substitua pelo nome que você definiu.

        builder.connect_signals({"gtk_main_quit": gtk.main_quit,
                                 "on_button_send_clicked": self.send_message,
                                 "on_open_chat_activate": self.call_chat,
                                 "on_label5_activate_current_link": self.call_notice
                                 })

    # Criando as funções que eu especifiquei como valor no dicionário dos Sinais

    #função pra enviar uma mensagem no chat
    def send_message(self, widget):
        pass

    #função para chamar a janela do chat
    def call_chat(self, widget):
        #Executando a Janela do chat
        self.window_chat.show()

    #função para chamar a janela com os detalhes da noticia
    def call_notice(self, widget):
        #Executando a Janela Sobre
        self.window_notice.show()

if __name__ == "__main__":
    # Criando uma instância do Programa
    app = DesktopApp()
    app.window.maximize()
    nome = gtk.Label("Ihuuu")
    for notify in app.notifications:
        notify.set_text("Uhuuiiii ")

    # Função do GTK que deixa a janela principal do nosso programa em loop para
    # que ela permanceça em execução, sendo encerrada apenas ao chamar a função
    # gtk.main_quit que está configurado no sinal gtk_main_quit, referente ao
    # botão fechar do programa
    gtk.main()

