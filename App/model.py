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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
#from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
import csv
from datetime import datetime


"""
Se define la estructura de los jobs
"""

# Construccion de modelos
import array_list as lt

def new_Offers():
    """
    Inicializa Jobs. Crea una lista vacia para guardar
    todos los jobs
    """
    offers = {"jobs": None,
              "skills": None,
              "multilocations": None,
              "employments_types": None}

    offers["jobs"] = lt.new_list()
    offers["skills"] = lt.new_list()
    offers["multilocations"] = lt.new_list()
    offers["employments_types"] = lt.new_list()

    return offers

# Funciones para agregar informacion al modelo
def newJob(published_at, title, company_name, experience_level, country_code, city ):
   """
   Esta estructura almancena los jobs.
   """
   job = {"published_at": "", "title": "", "company_name": "", "experience_level": "", "country_code": "", "city": ""}
   job["published_at"] = published_at
   job["title"] = title
   job["company_name"] = company_name
   job["experience_level"] = experience_level
   job["country_code"] = country_code
   job["city"] = city
   return job

def newSkill(name, level, title):
   """
   Esta estructura almancena los jobs.
   """
   skill = {"name": "", "level": "", "title": ""}
   skill["name"] = name
   skill["level"] = level
   skill["title"] = title
   return skill

def newEmployment_type(type, title, currency_salary, salary_from, salary_to):
   """
   Esta estructura almancena los jobs. "type", "title", "currency_salary", "salary_from", "salary_to"
   """
   employment_type = {"type": "", "title": "", "currency_salary": "", "salary_from": "", "salary_to": ""}
   employment_type["type"] = type
   employment_type["title"] = title
   employment_type["currency_salary"] = currency_salary
   employment_type["salary_from"] = salary_from
   employment_type["salary_to"] = salary_to
   return employment_type


def newMultilocation(city, street, title):
   """
   Esta estructura almancena los "city", "street", "title"
   """
   multilocation = {"city": "", "street": "", "title": ""}
   multilocation["city"] = city
   multilocation["street"] = street
   multilocation["title"] = title
   return multilocation

def addJob(offers, job):
   """
   Adiciona un job a la lista de jobs
   """
   t = newJob(job["published_at"], job["title"], job["company_name"], job["experience_level"], job["country_code"], job["city"])
   lt.add_last(offers["jobs"], t)
   return offers

def addSkill(offers, skill):
   """
   Adiciona un skill a la lista de skills  "name", "level", "title"
   """
   t = newSkill(skill["name"], skill["level"], skill["title"])
   lt.add_last(offers["skills"], t)
   return offers


def addEmployment_type(offers, employment_type):
   """
   Adiciona un employment_type "type", "title", "currency_salary", "salary_from", "salary_to"
   """
   t = newEmployment_type(employment_type["type"], employment_type["title"], employment_type["currency_salary"], employment_type["salary_from"], employment_type["salary_to"])
   lt.add_last(offers["employments_types"], t)
   return offers


def addMultilocation(offers, multilocation):
   """
   Adiciona un skill a la lista de "city", "street", "title"
   """
   t = newMultilocation(multilocation["city"], multilocation["street"], multilocation["title"])
   lt.add_last(offers["multilocations"], t)
   return offers

def jobSize(offers):
    return lt.size(offers["jobs"])

def skillSize(offers):
    return lt.size(offers["skills"])

def employment_typeSize(offers):
    return lt.size(offers["employments_types"])

def multilocationSize(offers):
    return lt.size(offers["multilocations"])


# Funciones de ordenamiento

def sortJobs(offers):
    """
    Ordena los Jobs
    """
    # toma la lista jobs
    jobs = offers["jobs"]
    # ordena la lista de libros
    sorted_list = lt.shell_sort(jobs, compareValue)
    # actualiza la lista de libros del catalogo
    offers["jobs"] = sorted_list
    return sorted_list

def compareValue(job1, job2):
    """
    compara dos jobs por title
    """
    return (str(job1["title"]) > str(job2["title"]))

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
