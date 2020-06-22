import csv
import math
import random
from person import *

weeks = 0
projects_per_week = 0

people = [] 
all_projects = []

def main():
    weeks = int(input("How many weeks will this be over the course of?\n"))
    people = get_data()

    projects_per_week = math.ceil(get_projects_length(people) / weeks)
    all_projects = get_all_projects(people)

    print(get_random_project(all_projects))

"""Example of a Line: ['Christopher R.', 'Lego Mindstorm BS', 'COMP110 - SPACECHEM']"""
def get_data():
    people = []
    amount_of_projects = 0

    with open ('data/test-data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            #Removing one since the first should always be a name
            amount_of_projects += len(line) - 1
            people.append(assign_person(line))

    return people

"""Sets and returns a Person class for grouping the data"""
def assign_person(details):
    name = details[0]
    
    details.remove(name)
    person = Person(name, details)
    return person

"""Returns the total amount of projects from everyone"""
def get_projects_length(people):
    amount = 0;
    for person in people:
        amount += len(person.projects)

    return amount

def get_all_projects(people):
    all_projects = []
    for person in people:
        for item in person.projects:
            all_projects.append(item)

    return all_projects

def get_random_project(all_projects):
    random_value = random.randrange(0, len(all_projects))

    project = all_projects[random_value]
    all_projects.remove(project)

    return project
    

main();