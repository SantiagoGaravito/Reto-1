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
    input_file = csv.DictReader(open(employments_typesfile, encoding="utf-8"), delimiter=';', fieldnames=["type", "title", "currency_salary", "salary_from", "salary_to"])
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

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass



def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


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
