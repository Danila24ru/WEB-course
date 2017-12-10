from webob import Request
import jinja2

includeJS = [
    'app.js',
    'react.js',
    'leaflet.js',
    'D3.js',
    'moment.js',
    'math.js'
]

includeCSS = [
    'main.css',
    'bootstrap.css',
    'normalize.css'
]

env = Environment(loader = FileSystemLoader('.'))	

class WsgiTopBottomMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):       
    
            css = ""
            js = ""
            for x in includeCSS:
                css += '<link rel="stylesheet" href="/_static/' + x + '"/>\n'
            for x in includeJS:
                js += '<script src="/_static/' + x + '"></script>\n'

            response = self.app(environ, start_response).decode() 
            return (response).encode() 

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/HTML')])
    template = env.get_template('/index.html')
    return template

app = WsgiTopBottomMiddleware(app)

print(Request.blank('/index.html').get_response(app))
