""" 
This program randomly assigns each specific project from a specific person to a
random week using a custom .csv. For the format refer to the readme.md in the
repository which can be found here: 

https://github.com/Koltonix/random-task-sorter
"""

__author___ = "Christopher Robertson"
__copyright___ = "MIT License Copyright (c) 2020"

import csv
import math
import random
from person import *

weeks = 0
projects_per_week = 0

global people, all_projects

def main():
    global people, all_projects

    all_projects = []

    weeks = int(input("How many weeks will this be over the course of?\n"))
    projects_per_week = int(input("Amount of Projects Each Week?\n"))
    people = get_data()
    
    while(get_projects_length(people) > 0):
        all_projects += get_projects_in_random(people)


    projects = sort_per_week(weeks, projects_per_week, all_projects)
    nested_projects = get_nested_remaining_projects(projects_per_week, all_projects)

    save_schedule(projects, nested_projects)


def save_schedule(projects_per_week, remaining_projects):
    with open('data/schedule.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        for week in projects_per_week:
            csv_writer.writerow(week)

        for extra in remaining_projects:
            csv_writer.writerow(extra)    

    print("Saved Schedule to:\ndata/schedule.csv")


def print_schedule(projects_each_week):
    for projects in projects_each_week:
        print(projects)


def sort_per_week(weeks, projects_per_week, projects_in_order):
    projects_each_week = []

    global people_used
    people_used = []

    for i in range(0, weeks):
        projects = []
        projects.append("WEEK " + str(i + 1))

        for j in range(0, projects_per_week):
            projects.append(projects_in_order[0])
            projects_in_order.pop(0)

        projects_each_week.append(projects)

    return projects_each_week


def get_nested_remaining_projects(projects_per_week, remaining_projects):
    nested_projects = []

    for i in range(0, round(len(remaining_projects) % projects_per_week)):
        projects = []
        projects.append("REMAINDER " + str(i + 1))

        for j in range(0, projects_per_week):
            projects.append(remaining_projects[0])
            remaining_projects.pop(0)

        nested_projects.append(projects)
    return nested_projects


"""Example of a Line: ['Christopher R.', 'Lego Mindstorm BS', 'COMP110 - SPACECHEM']"""
def get_data():
    global people
    people = {}

    with open ('data/test-data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            projects = []
            name = line[0]

            for cel in line:
                if (cel != name and cel != ""):
                    projects.append(cel)

            people[name] = projects

    return people


"""Returns the total amount of projects from everyone"""
def get_projects_length(people):
    amount = 0;
    for person in people:
        amount += len(people.get(person))

    return amount


"""Gets a random project and then removes it from all of the projects"""
def get_random_project():
    if (len(people) <= 0):
        return None

    randomise_order(people)


    return project


def get_projects_in_random(people):
    randomise_order(people)

    all_projects = []
    keys = randomise_dictionary_keys(people)

    for person in keys:
        if (len(people.get(person)) > 0):
            project = get_random_person_project(people.get(person))
            people.get(person).remove(project)
            all_projects.append(person + ": " + project)

    return all_projects

def randomise_dictionary_keys(dictionary):
    keys = list(dictionary.keys())
    random.shuffle(keys)
    return keys


def get_random_person_project(person):
    random_value = random.randrange(0, len(person))
    return person[random_value]

def randomise_order(people):
    for person in people:
        projects = people.get(person)
        random.shuffle(projects)
        people[person] = projects
    
main();