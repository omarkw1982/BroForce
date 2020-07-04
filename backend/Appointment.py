import os, os.path
import cherrypy
import calendar
import time


class Appointment(object):

    def __init__(self, _s, _e, _p, _d, _t, _c):
        self.start = _s
        self.end = _e
        self.patient = _p
        self.doctor = _d
        self.subject = _t;
        self.owner = _c  #ref to clinic


    def createAppointment(self,dt1,dt2,p,d,t):
        #check if appt is available
        if self.owner.isAvailable(dt1,dt2):
            self.start = dt1
            self.end = dt2
            self.patient = p
            self.doctor = d
            self.subject = t
            #Book appointment with clinic
            self.owner.book(self)
            return True
        return False

    def editAppointment(self, dt1, dt2, p, d, t):
        clinic = self.owner
        Appointment modified = Appointment(owner=clinic)

        #Modify changed values and commit
        #If appointment needs to be rescheduled, then we need to check available datetime
        clinic.cancel(self)

        if dt1 == None:
            dt1 = self.start
        if dt2 == None:
            dt2 = self.end

        if clinic.isAvaiable(dt1,dt2):
            modified.start = dt1
            modified.end = dt2
        else: #revert
            clinic.book(self)
            return False;

        if p != None:
            modified.patient = p;
        if d != None:
            modified.doctor = d;
        if t != None:
            modified.subject = t;

        clinic.book(modified)
        return True

    def cancelAppointment(self):
        return self.owner.cancel(self);





