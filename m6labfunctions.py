#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 10:56:03 2024

@author: Kelsey
"""

#Megan Harris
#M6Lab
#4-16-24
#CSC-121


#import student registry

from main import student_registry

import csv

#display registry

def display_registry():
    print(f"{'Student ID': <10}{'First Name':<15}{'Last Name':<15}{'Major':<25}{'Courses':}")
    print("-" *60)

    rows = []
    
    #loops over columns
    
    for student in student_registry:
        courses= student['courses']
        
        #loops over rows
        for course in courses:
            #prints statements in rows
            print (f'{student["stu_id"]:<10}{student["first_name"]:<15}{student["last_name"]:<15}{student["major"]:<25}{course}')

            rows.append({'Stu ID': student["stu_id"], 'First Name': student["first_name"], 'Last Name': student["last_name"], 'Major': student["major"], 'Course': courses})

    #writes to .csv file
            
    field_names = ['Stu ID', 'First Name', 'Last Name', 'Major', 'Course']
    with open('stu_registry.csv', 'w', newline= '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(rows)
              
            
#search by course

def course_lookup():
    course = str.title(input("Enter a course for the lists of students that are enrolled: "))
    


#combines user input with .csv for later writing to the file
    
    file = course + '.csv'


    found_course=False
    
    #print header
    print(f"{'Stu ID':<15}{'First Name':<15}{'Last Name':<15}{'Major':<15}")
    print("-" * 50)


    #initialize empty list

    rows = []
    
    #loops over columns
    
    for student in student_registry:
        
        if course in student['courses']:
            
            #exits loop if found
            found_course=True

            #appends info in rows if it is found in list

            rows.append({'Stu ID': student["stu_id"], 'First Name': student["first_name"], 'Last Name': student["last_name"], 'Major': student["major"]})

            
            #prints statemnts
            print(f'{student["stu_id"]:<15}{student["first_name"]:<15}{student["last_name"]:<15}{student["major"]}',sep=' ')
            #if course is not found
    
            field_names = ['Stu ID', 'First Name', 'Last Name', 'Major']
            with open(file, 'w', newline= '') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(rows)

    if not found_course:
        print("Invalid Entry")
        
#search by major

def major_lookup():
    
    major=str.title(input("Enter a major to view lists of students obtaining said major:"))

#combines user input with .csv for later writing to the file
    file = major + '.csv'
    
    found_major=False
    
    #print header
    print(f"{'Stu ID':<15}{'First Name':<15}{'Last Name':<15}{'Major':<15}")
    print("-" * 50)


    rows = []
    
    #loops over columns
    
    for student in student_registry:
        if major in student ['major']:
            
            #exits loop if found
            found_major=True


            rows.append({'Stu ID': student["stu_id"], 'First Name': student["first_name"], 'Last Name': student["last_name"]})
            
            #print statements
            print(f'{student["stu_id"]:<15}{student["first_name"]:<15}{student["last_name"]:<15}{student["major"]}',sep=' ')


            field_names = ['Stu ID', 'First Name', 'Last Name']
            with open(file, 'w', newline= '') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(rows)
            
        #if course is not found
        
    if not found_major:
        print("Invalid Entry")
        
#searcg by student IF

def stu_lookup():
    
    stu_id=int(input("Enter a student ID to search for student:"))

    #combines users input with .csv for later when writing to the file
    file = 'stu_' + str(stu_id) + '.csv'
    
    found_id=False
    
    #print header
    print(f"{'Stu ID':<15}{'First Name':<15}{'Last Name':<15}{'Major':<15}")
    print("-" * 50)

    rows = []
    
    #loops over columns
    
    for student in student_registry:
        if stu_id ==student["stu_id"]:
            found_id=True

            rows.append({'Stu ID': student["stu_id"], 'First Name': student["first_name"], 'Last Name': student["last_name"], 'Major': student["major"]})

            
            #print statements
            print(f'{student["stu_id"]:<15}{student["first_name"]:<15}{student["last_name"]:<15}{student["major"]}',sep=' ')


            field_names = ['Stu ID', 'First Name', 'Last Name', 'Major']
            with open(file, 'w', newline= '') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(rows)
            
    if not found_id:
        print ("Invalid Entry")
        
#calls functions

def main():
    
    #user choices determine which function is called
    choice= input("Enter your choice:")
    
    if choice =="1":
        display_registry()
        
    elif choice =="2":
        course_lookup()
        
    elif choice =="3":
        major_lookup()
        
    elif choice=="4":
        stu_lookup()
        
    elif choice=="5":
        print("Thank you for using our program. Goodbye!")
        
    else:
        print("Your option is invalid. Try again")
        main()
        
if __name__ == "__main__":
    main()
              
        
        
    
    
    

            
    
            
        
    
