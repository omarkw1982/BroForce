import os, os.path
import cherrypy
import calendar
import time


class Appointment(object):
    var _start
    var _end
    var _patient
    var _doctor
    var _title
    var owner

    def __init__(self, clinic):
        self.owner = clinic

    def createAppointment(self,dt1,dt2,p,d,t):
        #check if appt is available
        if self.owner.isAvailable(dt1,dt2):
            self._start = dt1
            self._end = dt2
            self.patient = p
            self.doctor = d
            #Book appointment with clinic
            self.owner.book(self)
            return True
        return False

    def editAppointment(self, dt1, dt2, p, d, t):
        Appointment modified = Appointment(self.owner)
        modified.createAppointment(self)
        //check
        return True

    def cancelAppointment(self, dt):
        return True

    def isAvailable(self, d, start_time, finish_time):
        return True


