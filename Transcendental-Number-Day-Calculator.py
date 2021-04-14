# -*- coding: utf-8 -*-

import datetime
from datetime import date

import numpy as np

e = "71828182845904523536"
pi = "14159265358979323846"
rad2 = "41421356237309504880"

class DateConverter:
    date_str = None
    day = None
    month = None
    dayandmonth = None
    year = None
    
    def __init__(self, date_np : np.datetime64):
        self.date_str = str(date_np)
        
        self.day = self.date_str[-2:]
        self.month = self.date_str[-5:-3]
        self.dayandmonth = self.date_str[-5:]
        
        dashIndex = self.date_str.split('-')
        if len(dashIndex) == 3:
            self.year = dashIndex[0] + ' CE'
        else:
            self.year = dashIndex[1] + ' BCE'
        
def getToday():
    return np.datetime64(date.today())

def getOneYearFromToday():
    today = getToday()
    return today + np.timedelta64(365, 'D')

def formatDistance(days_ago : int):
    days = str(days_ago)
    
    days_length = len(days)
    
    return days + (' ' * (20 - days_length))

def load_digits(number):
    return [number[:i] for i in range(2,len(number))]

def getDateForNumber(number):
    if number == e:
        return "02-01"
    elif number == pi:
        return "03-01"
    elif number == rad2:
        return "01-01"
    
def getOutputStringForNumber(number):
    if number == e:
        return '   E DAY   |   DAY OF FEBRUARY    |         YEAR'
    elif number == pi:
        return '  PI DAY   |    DAY OF MARCH      |         YEAR'
    elif number == rad2:
        return '  √2 DAY   |   DAY OF JANUARY     |         YEAR'

number_list = [e, pi, rad2] # Exchange for e, pi, or rad2

for number in number_list:
    print(getOutputStringForNumber(number))
    print('-----------+----------------------+----------------------')
    
    for future_date in np.arange(getToday(), getOneYearFromToday(), dtype='datetime64[D]'):
        for iteration in load_digits(number):
            days_ago = int(iteration)
            td = np.timedelta64(days_ago-1, 'D') #Subtract 1 because it includes the first day of the month as not part of the month
            number_day = future_date - td
            dc = DateConverter(number_day)
            if dc.dayandmonth == getDateForNumber(number):
                print(future_date, '|', formatDistance(days_ago), '|', dc.year)
                
    print('-----------┴----------------------┴----------------------')
    print()
    print()