"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import time
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.new_Offers()
    return control


# Funciones para la carga de datos

def load_data(control):
    """
    Carga los datos del reto
    """
    offers = control["model"]
    jobs = loadJobs(offers)
    skills = loadSkills(offers)
    employments_types = loadEmployments_types(offers)
    multilocations = loadMultilocations(offers)
    return jobs, skills, employments_types, multilocations

def loadJobs(offers):
    """
    Carga los jobs archivo.  
    """
    jobsfile = cf.data_dir + "small-jobs.csv"
    input_file = csv.DictReader(open(jobsfile, encoding="utf-8"), delimiter=';')
    for job in input_file:
        model.addJob(offers, job)
    return model.jobSize(offers)

def loadSkills(offers):
    skillsfile = cf.data_dir + "small-skills.csv"
    input_file = csv.DictReader(open(skillsfile, encoding="utf-8"), delimiter=';', fieldnames=["name", "level", "title"])
    for skill in input_file:
        model.addSkill(offers, skill)
    return model.skillSize(offers)

def loadEmployments_types(offers):
    employments_typesfile = cf.data_dir + "small-employments_types.csv"
    input_file = csv.DictReader(open(employments_typesfile, encoding="utf-8"), delimiter=';', fieldnames=["type", "id", "currency_salary", "salary_from", "salary_to"])
    for employment_type in input_file:
        model.addEmployment_type(offers, employment_type)
    return model.employment_typeSize(offers)


def loadMultilocations(offers):
    multilocationsfile = cf.data_dir + "small-multilocations.csv"
    input_file = csv.DictReader(open(multilocationsfile, encoding="utf-8"), delimiter=';', fieldnames=["city", "street", "title"])
    for multilocatio in input_file:
        model.addMultilocation(offers, multilocatio)
    return model.multilocationSize(offers)


# Funciones de ordenamiento

def sortJobs(control):
    """
    Ordena los JOBS
    """
    sorted_list = model.sortJobs(control["model"])
    
    return  sorted_list

def sortJobsF(control):
    """
    Ordena los JOBS
    """
    sorted_list = model.sortJobsF(control["model"])
    
    return  sorted_list

def ordenar_por_ofertas_y_nombre(control,lista):
    lista_ordenada = model.ordenar_por_ofertas_y_nombre(control["model"],lista)
    
    return  lista_ordenada
def merge_lists(control, list1, key):
    
    merge_lists = model.unir_listas_por_llave(control["model"],list1, key)
    return merge_lists

def filterbyCountryLevel(control, country, level):
    """
    Filtra los JOBS
    """
    filtered_list = model.filterbyCountryLevel(control["model"], country, level)
    
    return  filtered_list

def filterbyCountry(control, country):
    """
    Filtra los JOBS
    """
    filtered_list = model.filterbyCountry(control["model"], country)
    
    return  filtered_list


def filterbyDateRange(control, filter, fecha_inicial, fecha_final):
    """
    Filtra los JOBS by Date
    """
    filtered_list = model.filterbyDateRange(control["model"], filter, fecha_inicial, fecha_final)
    
    return  filtered_list


def filter_unique_by_attribute(control, filter):
    """
    Filtra los JOBS by country
    """
    filtered_list = model.filter_unique_by_attribute(control["model"], filter)
    
    return  filtered_list

def filter_unique_by_city(control, filter):
    """
    Filtra los JOBS by city
    """
    filtered_list = model.filter_unique_by_city(control["model"], filter)
    
    return  filtered_list


def Count_city(control, filter):
    """
    Filtra los JOBS by city
    """
    filtered_list = model.Count_city(control["model"], filter)
    
    return  filtered_list


def ciudad_con_mas_conteos_control(count_city):
    if not count_city["elementos"]:
        return None
    ciudad_max = max(count_city["elementos"], key=lambda x: x["conteo"])
    return ciudad_max["ciudad"], ciudad_max["conteo"]


def ciudad_con_menos_conteos_control(count_city):
    if not count_city["elementos"]:
        return None
    ciudad_min = min(count_city["elementos"], key=lambda x: x["conteo"])
    return ciudad_min["ciudad"], ciudad_min["conteo"]


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
