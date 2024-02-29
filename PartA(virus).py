#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:55:53 2024

@author: Kelsey
"""

#Virus Spread
#2-26-24
#CSC121 M3Pro-List
#Megan Harris

#define a function to calculate expected number of people infected

def calcInfected(start, weeklyRates):
    #begin a list to store number of infected people and list rates for each week
    
    #initialize the list
    infected = [start]
    
    for rate in weeklyRates:
        #calculate new infections for the week
        new_infected = infected[-1] * rate
        
        #add new infections to the list
        infected.append(new_infected)
        
    return infected[1:]

#test function assumping r=3 for next eight weeks
    
initial_infected = 1

#infected rate of 3 for the next eight weeks
weekly_rates = [3] * 8

expected_infected = calcInfected (initial_infected, weekly_rates)

print ("Expected number of people infected each week:", expected_infected)