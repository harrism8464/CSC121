#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 12:19:33 2024

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

#define infection rates for scenario 1 and scenario 2

#infection rate of 3 for eight weeks
scenario1_rates = [3] * 8

#infection rate of 3 for four weeks then 0.8 for next four weeks
scenario2_rates = [3] * 4 + [0.8] *4 

initial_infected= 1

scenario1_infected =calcInfected(initial_infected, scenario1_rates)
scenario2_infected = calcInfected(initial_infected, scenario2_rates)

#compare and display the two scenarios

print("Scenario 1:", scenario1_infected)
print("Scenario 2:", scenario2_infected)
    
    
