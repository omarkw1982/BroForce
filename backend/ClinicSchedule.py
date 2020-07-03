import os, os.path
import cherrypy
import calendar
import time


class ClinicSchedule(object):
    var _visitList = [];
    var _appointmentList = [];
    var currentDateTime;

    def book(self,




