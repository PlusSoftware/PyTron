import cherrypy
import pyqrcode
import shutil
import os.path

current_dir = os.path.dirname(os.path.abspath(__file__))
readyID = 0

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        global readyID
        cherrypy.session['identifier'] = str(readyID)
        readyID = readyID + 1
        qr = pyqrcode.create(cherrypy.session['identifier'])
        qr.png(cherrypy.session['identifier'] + ".png", scale=50)
        shutil.move(cherrypy.session['identifier'] + ".png","public/" + cherrypy.session['identifier'] + ".png")
        return '<style>body{background-color:black;}img{display: block; height: 100%; width: auto; margin-left: auto; margin-right: auto;}</style><img src="/static/' + cherrypy.session['identifier'] + ".png" + '"></img>'

if __name__ == '__main__':
     conf = {
         '/': {
             'tools.sessions.on': True
         },
         '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': current_dir + '/public'
         }
     }
     cherrypy.quickstart(StringGenerator(), '/', conf)