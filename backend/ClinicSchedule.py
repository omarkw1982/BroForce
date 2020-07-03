import os, os.path
import cherrypy
import calendar
import time


class ClinicSchedule(object):
    var visitList = [];
    var appointmentList = [];
    var currentDateTime = None;

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





