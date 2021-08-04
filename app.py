import pandas as pd
import csv

rows = []

df = pd.read_csv('final_data.csv')

planet_data_rows = rows[1:]

temp_planet_data_rows = list(planet_data_rows)

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity =[]

def convert_to_si(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = mass[i]*1.989e+30
        
convert_to_si(radius,mass)

def gravity_calculation(radius,mass):
    g = 6.674e-11
    for index in range(0,len(mass)):
        grav= (mass[index]*g)/((radius[index])**2)
        gravity.append(grav)
        
gravity_calculation(radius,mass)
