import os, os.path
import cherrypy
import calendar
import time


class ClinicSchedule(object):
    var appointmentList = [];
    var currentDateTime = 0;

    def __init__(self, _v, _app, _t):
        self.visitList = _v
        self.appointmentList = _app
        self.currentDateTime = _t

    def book(self, appt):
        return None;

    def cancel(self, appt):
        return None;

    def isAvailable(self, dt1, dt2):
        return True;

    def findUpcomingAppointmentsForPatient(self,patient_name):
        return True;

    def findUpcomingAppointmentsForDoctor(self,doctor_name):
        return True;

    def findPastAppointmentsForPatient(self, patient_name):
        return True;

    def findPastAppointmentsForDoctor(self, doctor_name):
        return True;










