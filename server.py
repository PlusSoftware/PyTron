import random
import string
import cherrypy

readyID = 0

class StringGenerator(object):

    @cherrypy.expose
    def index(self, length=1):
        cherrypy.session['identifier'] = readyID
        readyID = readyID + 1

    @cherrypy.expose
    def display(self):
        return cherrypy.session['identifier']

if __name__ == '__main__':
     conf = {
         '/': {
             'tools.sessions.on': True
         }
     }
     cherrypy.quickstart(StringGenerator(), '/', conf)