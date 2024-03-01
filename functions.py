# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 14:39:37 2024

@author: harrism8464
"""

import M3Pro_Lists_HarrisMegan as fn

def main():
    scenario1_rates = [3] * 8
    
    #infection rate of 3 for four weeks then 0.8 for next four weeks
    scenario2_rates = [3] * 4 + [0.8] *4 
    
    initial_infected= 1
    
    scenario1_infected = fn.calcInfected(initial_infected, scenario1_rates)
    scenario2_infected = fn.calcInfected(initial_infected, scenario2_rates)
    
    fn.displayResults(scenario1_infected, scenario2_infected)
    
if __name__=='__main__':
    main()
    