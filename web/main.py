import os, os.path
import cherrypy


class MainApp(object):

    @cherrypy.expose
    def index(self):
        return open('../web/index.html')

    @cherrypy.expose
    def register(self):
        return open('../web/register.html')

    @cherrypy.expose
    def login(self):
        return open('../web/login.html')

    @cherrypy.expose
    def appointments(self):
        return open('../web/appointments.html')

    @cherrypy.expose
    def doctor(self):
        return open('../web/doctor.html')

    @cherrypy.expose
    def patient(self):
        return open('../web/patient.html')

    @cherrypy.expose
    def admin(self):
        return open('../web/admin.html')



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

    cherrypy.quickstart(MainApp(), '/', conf)