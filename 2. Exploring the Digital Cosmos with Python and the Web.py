#Task 1:Set up a Python Virtual Environment and Install Required Packages
import requests
import json

#Task 2:Fetch Data from a Space API

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet'] == True:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name} ")
            print(f'\tMass: {mass}')
            print(f'\tOrbit Period: {orbit_period} days')

fetch_planet_data()


#Task 3:Data Presentation and Analysis

planet_data = []

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet'] == True:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']

            planet_data.append({
                'name': name,
                'mass': mass,
                'orbit period': orbit_period
            })

    return planet_data

        

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda x: x['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']


planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")