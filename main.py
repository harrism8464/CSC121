#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:40:42 2024

@author: Kelsey
"""
#Megan Harris
#M6Lab
#4-16-2024
#CSC-121


#create student registry for 20 students
student_registry = [ 

    {"stu_id": 1, "first_name": "John","last_name": "Doe","major": "Computer Science",
     "courses": ["Intro to Programming", "Data Structures", "Algorithms", "Database Management"] },

    {"stu_id": 2, "first_name": "Jane", "last_name": "Smith", "major": "Electrical Engineering", 
     "courses": ["Circuit Analysis", "Digital Electronics", "Signals and Systems", "Power Systems"]},

    {"stu_id": 3,"first_name": "Michael", "last_name": "Johnson","major": "Mechanical Engineering",
     "courses": ["Statics", "Dynamics", "Thermodynamics", "Flustu_id Mechanics"] },

    {"stu_id": 4, "first_name": "Emily", "last_name": "Brown", "major": "Biology", "courses": ["Cell Biology", "Genetics", "Ecology", "Anatomy"] },

    {"stu_id": 5, "first_name": "David", "last_name": "Wilson", "major": "Psychology", 
     "courses": ["Introduction to Psychology", "Abnormal Psychology", "Cognitive Psychology", "Social Psychology"]},

    {"stu_id": 6, "first_name": "Sarah", "last_name": "Lee", "major": "English Literature",
     "courses": ["Shakespeare", "American Literature", "Victorian Literature", "Modern Poetry"]},

    {"stu_id": 7, "first_name": "Christopher", "last_name": "Martinez", "major": "History",
     "courses": ["World History", "American History", "European History", "Ancient Civilizations"]},

    {"stu_id": 8, "first_name": "Jessica", "last_name": "Garcia", "major": "Chemistry", 
     "courses": ["General Chemistry", "Organic Chemistry", "Analytical Chemistry", "Physical Chemistry"]},

    {"stu_id": 9, "first_name": "Daniel", "last_name": "Rodriguez", "major": "Mathematics",
     "courses": ["Calculus I", "Calculus II", "Linear Algebra", "Differential Equations"]},

    {"stu_id": 10, "first_name": "Amanda", "last_name": "Lopez", "major": "Nursing",
     "courses": ["Anatomy and Physiology", "Pharmacology", "Nursing Ethics", "Nursing Care Management"]},

    {"stu_id": 11, "first_name": "Robert", "last_name": "Perez", "major": "Civil Engineering",
     "courses": ["Structural Analysis", "Geotechnical Engineering", "Transportation Engineering", "Construction Management"]},

    {"stu_id": 12, "first_name": "Jennifer", "last_name": "Ramirez", "major": "Sociology",
     "courses": ["Introduction to Sociology", "Social Stratification", "Criminology", "Research Methods"]},

    {"stu_id": 13, "first_name": "Matthew", "last_name": "Torres", "major": "Political Science",
     "courses": ["American Government", "Comparative Politics", "International Relations", "Political Theory"]},

    {"stu_id": 14, "first_name": "Ashley", "last_name": "Flores", "major": "Art History",
     "courses": ["Ancient Art", "Renaissance Art", "Modern Art", "Contemporary Art"]},

    {"stu_id": 15, "first_name": "Ryan", "last_name": "Gonzalez", "major": "Physics",
     "courses": ["Classical Mechanics", "Quantum Mechanics", "Electromagnetism", "Thermodynamics"]},

    {"stu_id": 16, "first_name": "Nicole", "last_name": "Sanchez", "major": "Communications",
     "courses": ["Media Studies", "Public Speaking", "Journalism", "Advertising"]},

    {"stu_id": 17, "first_name": "Kevin", "last_name": "Rivera", "major": "Economics",
     "courses": ["Microeconomics", "Macroeconomics", "Econometrics", "International Economics"]},

    {"stu_id": 18, "first_name": "Lauren", "last_name": "Taylor", "major": "Environmental Science",
     "courses": ["Ecology", "Environmental Chemistry", "Climate Change", "Conservation Biology"]},

    {"stu_id": 19, "first_name": "Brandon", "last_name": "Hernandez", "major": "Computer Engineering",
     "courses": ["Digital Logic Design", "Computer Architecture", "Operating Systems", "Embedded Systems"]},

    {"stu_id": 20, "first_name": "Megan", "last_name": "Hill", "major": "Music", "courses": ["Music Theory", "Music History", "Voice Lessons", "Piano"]}
]





import functions

#displays menu

def menu ():
    print("Menu","-" * 30, sep= '')
    print("1: Display Registry Content")
    print("2: Display Course Roster")
    print("3: List of Students by Major")
    print("4: Student Search by ID")
    print("5: Exit")
    print("-" * 30)
    
    
#calls display menu and functions

def main():
    
    menu ()
    
    #initilazes choice variable
    
    choice= input ("Enter your choice:")
    
    #choices used determines what function is called
    
    #choice displays registry content
    if choice =="1":
        functions.display_registry()
        input("Press enter to return to the main menu")
        main()
        
    #choice displays course roster
    elif choice =="2":
        functions.course_lookup()
        input("Press enter to return to the main menu")
        main()
        
    #choice searches student my major
    elif choice =="3":
        functions.major_lookup()
        input("Press enter to return to the main menu")
        main()
        
    #choice searches student by their ID
    elif choice =="4":
        functions.stu_lookup()
        input("Press enter to return to the main menu")
        main()
        
    #choice exits program
    elif choice =="5":
        print("Thanks for using our student registry program. Goodbye!")
        
        
    #invalid entry if 1-5 is not chosen
    else:
        print("Invalid option..try again!")
        main()
        
if __name__ == "__main__":
    main()
    
    
    
    