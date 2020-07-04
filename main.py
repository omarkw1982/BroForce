import os, os.path
from hashlib import sha1
#from Auth import AuthController, require, member_of, name_is
import cherrypy
import pymysql.cursors

from backend.Admin import *
from backend.Auth import *

class RootServer():
    @cherrypy.expose
    def index(self):
        return """This is a public page!"""

class MainApp(object):

    @cherrypy.expose
    def index(self):
        return "This is the public section"
        #return open('./web/index.html')

    @cherrypy.expose
    def register(self):
        return "This is the registration page"
        #return open('../web/register.html')

    @cherrypy.expose
    def login(self):
        return "This is the login page"
        #return open('../web/login.html')



if __name__ == '__main__':
    users = get_users()

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
            'tools.staticdir.dir': os.path.abspath(os.getcwd())+'/web'
        },
        '/session': {
            'tools.sessions.on': True,
            'tools.auth.on': False
        }
    }

    broforce = RootServer()
    broforce.session = MainApp()
    broforce.admin = Admin()
    broforce.internal = RestrictedArea()
    broforce.auth = AuthController()
    cherrypy.quickstart(broforce, '/', conf)




