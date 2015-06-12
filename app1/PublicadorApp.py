# -*- coding: utf-8 -*-
__author__ = 'rafaeltavares'
import pygtk
import gtk
import loader
from string import replace
from classes import News

# Criando a Classe do Programa
class PublicadorApp(object):
    def __init__(self):
        # Agora como eu havia dito vamos utilizar uma função da classe gtk.Builder
        # para carregar o arquivo XML gerado pelo Glade.

        builder = gtk.Builder()  # Primeiramente criamos uma instância da classe
        builder.add_from_file("PublicadorApp.glade")  # Função para carregar o arquivo

        # Agora nós podemos acessar os widgets do arquivo XML, caso você tenha
        # alterado o nome de algum widget e não seguiu o tutorial exatamente como
        # eu fiz, preste atenção e utilize o nome que você definiu.
        # Caso não se lembre os nomes abra o arquivo XML no glade novamente e veja
        # os nomes na ávore de widgets do lado direito.
        # Utilizaremos a função get_object passando como parâmetro o nome do widget.

        # Obtendo o widget window1 nossa janela principal
        self.window = builder.get_object("windowMain")

        # Obtendo o widget text_entry (a área de texto do nosso programa) pois
        # iremos utiliza-la nas funções de inversão da URL e para adicionar o a
        # URL já invertida
        self.title = builder.get_object("title_text")
        self.author = builder.get_object("author_text")
        self.content = builder.get_object("content_text")
        self.image = builder.get_object("selected_image")

        # Exibindo a janela do programa
        self.window.show()

        # Agora nós iremos conectar os sinais que definimos para cada widget no
        # Glade Para isso usamos a função connect_signals(). Se você definiu o nome
        # de algum sinal de um modo diferente dos que eu utilizei preste atenção
        # nessa parte e substitua pelo nome que você definiu.

        # Falta ler o sinal do botão de publicar
        builder.connect_signals({"gtk_main_quit": gtk.main_quit,
                                 "on_new_activate": self.new_notice,
                                 "on_open_news_activate": self.open_news,
                                 "on_save_news_activate": self.save_news,
                                 "on_button_publisher_clicked": self.publish_news
                                 })

    # Criando as funções que eu especifiquei como valor no dicionário dos Sinai

    def open_news(self, widget):

        with open("ok.xml", "rb") as xmlToRead:
            xml = xmlToRead.read()
        noticia = News.newsFromXml(xml)
        self.title.set_text(noticia.title)
        self.author.set_text(noticia.publishers)
        self.content.get_buffer().set_text(noticia.content)



    def new_notice(self, widget):
        self.title.set_text("")
        self.author.set_text("")
        self.content.get_buffer().set_text("")
        gtk.FileChooserButton.set_filename(self.image, "macaco")

    def save_news(self, widget):
        encodeImg = News.encodeImg(gtk.FileChooserButton.get_filename(self.image))
        title = self.title.get_text()
        author = self.author.get_text()
        content = self.content.get_buffer().get_text(self.content.get_buffer().get_start_iter(), self.content.get_buffer().get_end_iter())
        content = replace(content, '\n' ,' ')
        summary = content[:20]
        noticia = News(author, title, summary, content, encodeImg, False)
        with open(title+'.xml', 'wb') as new_file:
            new_file.write(noticia.toXml())

    def publish_news(self, widget):
        encodeImg = News.encodeImg(gtk.FileChooserButton.get_filename(self.image))
        title = self.title.get_text()
        author = self.author.get_text()
        content = self.content.get_buffer().get_text(self.content.get_buffer().get_start_iter(), self.content.get_buffer().get_end_iter())
        content = replace(content, '\n' ,' ')
        summary = content[:20]
        noticia = News(author, title, summary, content, encodeImg,'false')
        loader.publish(noticia)

        if title != "" and author != "" and content != "":
            noticia = News(author, title, summary, content, encodeImg, 'false')
            loader.publish(noticia)
        else:
            diag=gtk.MessageDialog(self.window, gtk.DIALOG_MODAL,gtk.MESSAGE_ERROR,gtk.BUTTONS_OK)
            diag.set_markup("Preencha todos os campos de forma correta!")
            diag.run()
            diag.destroy()


if __name__ == "__main__":
    # Criando uma instância do Programa
    app = PublicadorApp()


    # Função do GTK que deixa a janela principal do nosso programa em loop para
    # que ela permanceça em execução, sendo encerrada apenas ao chamar a função
    # gtk.main_quit que está configurado no sinal gtk_main_quit, referente ao
    # botão fechar do programa
    gtk.main()

