#!/usr/bin/env python
import pygtk
import gtk
import webkit
import urllib
import urlparse
import sys

FB_TOKEN_FILE = 'access_token.txt'

class Browser(object):

    def __init__(self, app_key, token_file=FB_TOKEN_FILE):
        self.debug = False
        self.close_window = True
        self.token_file = token_file
        self.token = ''

        #app
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.scrolled_window = gtk.ScrolledWindow()
        # Cria a webview
        self.web_view = webkit.WebView()
        self.scrolled_window.add(self.web_view)
        self.window.add(self.scrolled_window)
        # Coonectando eventos
        self.window.connect('destroy', self._destroy_event_cb)
        self.web_view.connect('load-committed', self._load_committed_cb) # evento de redirecionamento carregado
        self.window.set_default_size(1024, 800)
        # carrega pagina Facebook usando OAuth
        self.web_view.load_uri(
            'https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s&response_type=token&scope=email' % (urllib.quote(app_key), urllib.quote('https://www.facebook.com/connect/login_success.html'))
            )

    def _load_committed_cb(self, web_view, frame):

		# Pega a url corrente da webview e checa se foi redirecionado para https://www.facebook.com/connect/login_success.html
		# parametros como "access_token" são recuperados via get :)
        uri = frame.get_uri()
        parse = urlparse.urlparse(uri)
        if (hasattr(parse, 'netloc') and hasattr(parse, 'path') and
            hasattr(parse, 'fragment') and parse.netloc == 'www.facebook.com' and
            parse.path == '/connect/login_success.html' and parse.fragment):
            # pega token da URL
            params = urlparse.parse_qs(parse.fragment)
            self.token = params['access_token'][0] # aqui pego o parametro access_token que está na Url :) só alegria
            # faço o que quiser com ele > salvei no arquivo.
            token_file = open(self.token_file, 'w')
            token_file.write(self.token)
            token_file.close()
            gtk.main_quit() # Finish
            if self.close_window:
                try:
                    self.window.destroy()
                except RuntimeError:
                    pass

    def _destroy_event_cb(self, widget):
        return gtk.main_quit()

    def authorize(self):
        self.window.show_all()
        gtk.main()

if (__name__ == '__main__'):
    # Creates the browser
    browser = Browser(app_key='768606509924888', token_file=FB_TOKEN_FILE)
    # Launch browser window
    browser.authorize()

