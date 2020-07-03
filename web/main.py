import os, os.path
import cherrypy


class RootServer():
    @cherrypy.expose
    def index(self):
        return """This is a public page!"""

class MainApp(object):
    @cherrypy.expose
    def index(self):
        return open('../web/index.html')
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
        db = MySQLdb.connect(host='localhost',
                             user='db_name',
                             passwd='db_pass',
                             db='db_name')
        curs = db.cursor()
        curs.execute('select username,password from users')
        return dict(curs.fetchall())

def encrypt_pw(pw):
        return md5(pw).hexdigest()



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
                    'tools.basic_auth.realm': 'Some site2',
                    'tools.basic_auth.users': users,
                    'tools.basic_auth.encrypt': encrypt_pw}
    }

    root = RootServer()
    root.secure = MainApp()
    cherrypy.quickstart(root, '/', conf)




