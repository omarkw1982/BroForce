import cherrypy
from backend.Auth import AuthController, require, member_of, name_is


class Admin:
    # all methods in this controller (and subcontrollers) is
    # open only to members of the admin group

    _cp_config = {
        'Auth.require': [member_of('admin')]
    }

    @cherrypy.expose
    @require()
    def index(self):
        return """This is the admin only area."""

class RestrictedArea:
    _cp_config = {
        'tools.sessions.on': True,
        'tools.auth.on': True
    }

    @cherrypy.expose
    def appointments(self):
        return "This is the appointment's page"
        #return open('../web/appointments.html')

    @cherrypy.expose
    def doctor(self):
        return "This is the doctor's page"
        #return open('../web/doctor.html')

    @cherrypy.expose
    def patient(self):
        return "This is the patient's page"
        #return open('../web/patient.html')

