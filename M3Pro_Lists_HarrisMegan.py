# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 13:21:27 2024

@author: harrism8464


"""

#Megan Harris
#2-29-24
#CSC-121 M3Pro-List
#VirusRates



#function calls main program
def main():
    
    #define infection rates for scenario 1 and scenario 2
    
    #infection rate of 3 for eight weeks
    scenario1_rates = [3] * 8
    
    #infection rate of 3 for four weeks then 0.8 for next four weeks
    scenario2_rates = [3] * 4 + [0.8] *4 
    
    initial_infected= 1
    
    scenario1_infected =calcInfected(initial_infected, scenario1_rates)
    scenario2_infected = calcInfected(initial_infected, scenario2_rates)
    
    displayResults(scenario1_infected, scenario2_infected)
    
    #compare and display the two scenarios

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


#function displays information in a table
def displayResults(scenario1_infected, scenario2_infected):   
    print(f'{"Week":<10}{"R=3":<10}{"Vaccine":<10}')
    
    
    for i in range(len(scenario1_infected)):
        print(f'{i+1:<10}{scenario1_infected[i]:<10}{scenario2_infected[i]:<10.0f}')
        
if __name__=='__main__':
    main()
    

