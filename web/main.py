import os, os.path
from hashlib import sha1

import cherrypy
import pymysql.cursors

class RootServer():
    @cherrypy.expose
    def index(self):
        return """This is a public page!"""

class MainApp(object):
    @cherrypy.expose
    def index(self):
        return "This is a secure section"
        #return open('./web/index.html')

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

def get_users():
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='BroForce',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `name` FROM `BroForce`.`Users`;"
            cursor.execute(sql)
            users = dict(cursor.fetchall())
            print("User list: "+users)
    finally:
        connection.close()
        return users

def encrypt_pw(pw):
        return sha1(pw).hexdigest()



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
            'tools.staticdir.dir': '../public'
        },
        '/secure': {'tools.basic_auth.on': True,
                    'tools.basic_auth.realm': 'Virtual Clinic',
                    'tools.basic_auth.users': users,
                    'tools.basic_auth.encrypt': encrypt_pw}
    }

    root = RootServer()
    root.secure = MainApp()
    cherrypy.quickstart(root, '/', conf)




