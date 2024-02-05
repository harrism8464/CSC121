# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:34:25 2024

@author: harrism8464
"""

def get_info():
    count = int(input("Enter count of item:"))
    unit_cost = float(input("Enter unit cost:"))
    return count, unit_cost

def calc_cost(count, unit_cost):
    return count *unit_cost

def calc_tax(total_cost):
    tax_rate =0.075
    tax_amount = total_cost * tax_rate
    return tax_amount

def display_results(total_cost, tax_amount):
    total_cost_with_tax= total_cost + tax_amount
    
    print(f"\nPre-tax cost: ${total_cost:.2f}")
    print(f"Tax (7.5%): ${tax_amount:.2f}")
    print(f"Total cost including tax: ${total_cost_with_tax:.2f}")