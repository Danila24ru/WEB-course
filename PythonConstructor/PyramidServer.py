
# coding=utf-8

from pyramid.httpexceptions import HTTPFound
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.response import Response
from jinja2 import Template
import os 
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')

HOST, PORT = '127.0.0.1' , 6543

FilesAddress = "http://" + HOST + "/gameFiles/"

datagame = { "scene 1" :
                    {
                        "Images": {
                                        "LeftImage" : {},
                                        "RightImage" : {},
                                        "ForwardImage" : {}
                                  },
                        "Videos":
                                  {
                                    "LeftVideo" : {},
                                    "RightVideo" : {},
                                    "ForwardVideo" : {}
                                  }
                    },
            "scene 2" :
                    {
                        "Images": {
                                        "LeftImage" : {},
                                        "RightImage" : {},
                                        "ForwardImage" : {}
                                  },
                        "Videos":
                                {
                                "LeftVideo" : {},
                                "RightVideo" : {},
                                "ForwardVideo" : {}
                                }
                    }
            }

datagame["scene 1"]["Images"]["LeftImage"]["Description"] = "heeh....."
datagame["scene 1"]["Images"]["LeftImage"]["Image"] = "/gameFiles/scene1/images/LeftImage.png"
datagame["scene 1"]["Images"]["LeftImage"]["PreviewImage"] = "/gameFiles/scene1/images/LeftImagePreview.png"

datagame["scene 1"]["Images"]["RightImage"]["Description"] = "ahahaha RightImage"
datagame["scene 1"]["Images"]["RightImage"]["Image"] = "/gameFiles/scene1/images/RightImage.png"
datagame["scene 1"]["Images"]["RightImage"]["PreviewImage"] = "/gameFiles/scene1/images/RightImagePreview.png"

datagame["scene 1"]["Images"]["ForwardImage"]["Description"] = "Forward Image"
datagame["scene 1"]["Images"]["ForwardImage"]["Image"] = "/gameFiles/scene1/images/ForwardImage.png"
datagame["scene 1"]["Images"]["ForwardImage"]["PreviewImage"] = "/gameFiles/scene1/images/ForwardImagePreview.png"

datagame["scene 2"]["Images"]["ForwardImage"]["Description"] = "Forward Image"
datagame["scene 2"]["Images"]["ForwardImage"]["Image"] = "/gameFiles/scene2/images/LeftImage.png"
datagame["scene 2"]["Images"]["ForwardImage"]["PreviewImage"] = "/gameFiles/scene2/images/LeftImagePreview.png"

def SaveToJson():
    
    with open('static/gameFiles/GameConfig.json', 'w') as outfile:
        json.dump(datagame, outfile)
    print("Json updated!!!")


CURRENT_DIR = os.path.dirname(os.path.realpath("__file__")) + '/static'

@view_config(route_name='upload_file', request_method='POST')
def upload_file(request):
    if request.method == 'POST':

        print(request.POST.items())

        fileType = next(iter(request.POST.items() or []), None)

        print(fileType[0])
        data = request.POST[fileType[0]]

        

        open(CURRENT_DIR + '/gameFiles/scene1/images/%s.png' %(fileType[0]), 'wb').write(data.file.read())
        print("try upload file")
        print(data.filename + " loaded!")

        SaveToJson()

        url = request.route_url('index')
        return HTTPFound(location = url)
    return Response('Erorka')


@view_config(route_name = 'index', request_method = 'GET')
def index_view(request):
    file = open(CURRENT_DIR + '/index.html', 'r')

    Temp = Template(file.read())
    resp = Temp.render(data = datagame)

    return Response(resp)



if __name__ == '__main__':
    print('Starting server :)')
    with Configurator() as config:

        config.add_static_view('css', 'static/css')
        config.add_static_view('js', 'static/js')
        config.add_static_view('images', 'static/images')
        config.add_static_view('gameFiles', 'static/gameFiles')

        config.add_route('index', '/index')
        config.add_route('upload_file', '/upload_file')
        config.add_view(index_view, route_name = 'index', request_method = 'GET')
        config.add_view(upload_file, route_name ='upload_file', request_method = 'POST')
        app = config.make_wsgi_app()
    server = make_server(HOST, PORT, app)
    server.serve_forever()
    print('Server started :)')








    





    



