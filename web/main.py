import os, os.path
import cherrypy


class MainApp(object):

    @cherrypy.expose
    def index(self):
        return open('../template/index.html')

    @cherrypy.expose
    def register(self):
        return open('../template/setoolkit/index.html')

    @cherrypy.expose
    def login(self):
        return open('../template/bots/index.html')

    @cherrypy.expose
    def addApt(self):
        return open('../template/rats/index.html')

    @cherrypy.expose
    def editApt(self):
        return open('../template/sna/index.html')

    @cherrypy.expose
    def deleteApt(self):
        return open('../template/calldirs/index.html')


if __name__ == '__main__':
    conf = {
        'global': {
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 8080
        },
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '../public'
        }
    }
    MainApp.appointment = AppointmentApp()
    cherrypy.quickstart(MainApp(), '/', conf)