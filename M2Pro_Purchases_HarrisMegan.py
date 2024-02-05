# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:20:19 2024

@author: harrism8464
"""

#Functions program to calculate item cost
#2-5-24
#CSC-121 M2Pro-Purchases
#Megan Harris

import fn

def main():
    user_choice="y"
    quantity=0
    total_cost=0
    
    while user_choice == 'y':
   
        quantity += 1
    
        #item will count
        print('Item', quantity)
    
        #user enters count of item and cost
    
        count, unit_cost=fn.get_info() 
        item_cost= fn.calc_cost(count, unit_cost)
        
        total_cost += item_cost
        
             
    
        #ask the user if they want to input more items
        user_choice=input("Add more items? (y/n):")
        
    return total_cost

    


    
if __name__=="__main__":
    total_cost=main()
    fn.calc_tax(total_cost)
    tax_amount=fn.calc_tax(total_cost)
    fn.display_results(total_cost, tax_amount)
    

    
    