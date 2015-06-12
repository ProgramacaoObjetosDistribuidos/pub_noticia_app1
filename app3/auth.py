#!/usr/bin/env python
import pygtk
import gtk
import webkit
import urllib
import urlparse
from threading import Thread

APP_KEY = '768606509924888'

class Browser():
    def __init__(self, app_key):
        self.debug = False
        self.close_window = True
        self.token = ''

        # app
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Notify Client")
        self.scrolled_window = gtk.ScrolledWindow()
        # Cria a webview
        self.web_view = webkit.WebView()
        self.scrolled_window.add(self.web_view)
        self.window.add(self.scrolled_window)
        # Coonectando eventos
        self.window.connect('destroy', self._destroy_event_cb)
        self.web_view.connect('load-committed', self._load_committed_cb)  # evento de redirecionamento carregado
        self.window.set_default_size(1024, 700)
        # carrega pagina Facebook usando OAuth
        self.web_view.load_uri(
            'https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s&response_type=token&scope=email' % (
                urllib.quote(app_key), urllib.quote('https://www.facebook.com/connect/login_success.html'))
        )

    def _load_committed_cb(self, web_view, frame):

        uri = frame.get_uri()
        parse = urlparse.urlparse(uri)
        if (hasattr(parse, 'netloc') and hasattr(parse, 'path') and
                hasattr(parse, 'fragment') and parse.netloc == 'www.facebook.com' and
                    parse.path == '/connect/login_success.html' and parse.fragment):
            # pega token da URL
            params = urlparse.parse_qs(parse.fragment)
            self.token = params['access_token'][0]
            with open("access_token.txt","wb") as token_file:
                token_file.write(self.token)
            self.window.destroy()

    def _destroy_event_cb(self, widget):
        return gtk.main_quit()

if (__name__ == '__main__'):
    b = Browser(APP_KEY)
    b.window.show_all()
    gtk.main()


