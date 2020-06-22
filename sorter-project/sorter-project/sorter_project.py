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

    projects_per_week = sort_per_week(weeks, projects_per_week, all_projects)
    save_schedule(projects_per_week)


def save_schedule(projects_per_week):
    with open('data/schedule.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        for week in projects_per_week:
            csv_writer.writerow(week)
    print("Saved Schedule to:\ndata/schedule.csv")


def print_schedule(projects_each_week):
    for projects in projects_each_week:
        print(projects)


def sort_per_week(weeks, projects_per_week, all_projects):
    projects_each_week = []
    
    for i in range(0, weeks):
        projects = []
        projects.append("WEEK " + str(i + 1))

        for j in range(0, projects_per_week):
          
            projects.append(get_random_project(all_projects))

        projects_each_week.append(projects)

    return projects_each_week


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


"""Gets all of the projects in a list"""
def get_all_projects(people):
    all_projects = []
    for person in people:
        for item in person.projects:
            all_projects.append([person.name, item])

    return all_projects


"""Gets a random project and then removes it from all of the projects"""
def get_random_project(all_projects):
    if (len(all_projects) <= 0):
        return None

    else:
        random_value = random.randrange(0, len(all_projects))
        project = all_projects[random_value]
        all_projects.remove(project)

        return project
    

main();