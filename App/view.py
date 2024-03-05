"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
#from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback
import array_list as lt

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller()
    return control

# Se crea el controlador asociado a la vista
control = new_controller()

def print_menu():
    print("==========================================")
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")
    print("==========================================")


def load_data():
    """
    Carga los datos
    """
    jobs, skills, employments_types, multilocations = controller.load_data(control)
    return jobs, skills, employments_types, multilocations

# Imprimir Resultados published_at, title, company_name, experience_level, country_code, city
def printSortResults(sort_jobs, sample=3):
    if lt.isEmpty(sort_jobs):
        print("La lista esta vacia!!!...")
    else:
        size = lt.size(sort_jobs)
        if size <= sample*2:
            print("\n")
            print("Los", size, "Jobs ordenados son: ==========================================")
            for job in lt.iterator(sort_jobs):
                print("Título de la oferta:", job["title"], "Fecha de publicación:", job["published_at"],
                      "Nombre de la empresa que publica:", job["company_name"], "Nivel de experticia de la oferta:", job["experience_level"],
                      "País de la oferta:", job["country_code"], "Ciudad de la oferta:", job["city"])
        else:
            print("\n")
            print("Los", sample, "primeros jobs ordenados son: ==========================================")
            i = 1
            while i <= sample:
                job = lt.get_element(sort_jobs, i)
                print("Título de la oferta:", job["title"], "Fecha de publicación:", job["published_at"],
                      "Nombre de la empresa que publica:", job["company_name"], "Nivel de experticia de la oferta:", job["experience_level"],
                      "País de la oferta:", job["country_code"], "Ciudad de la oferta:", job["city"])
                i += 1

            print("\n")
            print("Los", sample, "últimos jobs ordenados son: ==========================================")
            i = size
            while i >= size - sample + 1 and i > 0:
                job = lt.get_element(sort_jobs, i)
                print("Título de la oferta:", job["title"], "Fecha de publicación:", job["published_at"],
                      "Nombre de la empresa que publica:", job["company_name"], "Nivel de experticia de la oferta:", job["experience_level"], 
                      "País de la oferta:", job["country_code"], "Ciudad de la oferta:", job["city"])
                i -= 1
        
       
# Imprimir Resultados published_at, title, company_name, experience_level, country_code, city
def printSortResultsN(sort_jobs, sample):
    if lt.isEmpty(sort_jobs):
        print("La lista esta vacia!!!...")
    else:
        size = lt.size(sort_jobs)
        if size <= sample*2:
            print("\n")
            print("Los", size, "Jobs ordenados son: ==========================================")
            for job in lt.iterator(sort_jobs):
                print("Título de la oferta:", job["title"], "Fecha de publicación:", job["published_at"],
                      "Nombre de la empresa que publica:", job["company_name"], "Nivel de experticia de la oferta:", job["experience_level"],
                      "País de la oferta:", job["country_code"], "Ciudad de la oferta:", job["city"])
        else:
            print("\n")
            print("Los", sample, "últimos jobs ordenados son: ==========================================")
            
            i = size
            while i >= size - sample + 1 and i > 0:
                job = lt.get_element(sort_jobs, i)
                print("Título de la oferta:", job["title"], "Fecha de publicación:", job["published_at"],
                      "Nombre de la empresa que publica:", job["company_name"], "Nivel de experticia de la oferta:", job["experience_level"], 
                      "País de la oferta:", job["country_code"], "Ciudad de la oferta:", job["city"])
                i -= 1

        
                
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass




# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            job_print, skill_print, employments_types_print, multilocations_print= load_data()
            print("==========================================")
            print("Jobs cargados: " + str(job_print))
            print("Skills cargados: " + str(skill_print))
            print("Employments Types cargados: " + str(employments_types_print))
            print("Multilocations cargados: " + str(multilocations_print))
            print("==========================================")
            result = controller.sortJobs(control)
            size = lt.size(result)
            printSortResults(result)
            
        elif int(inputs) == 2:
            num_ofertas = input("Ingrese el numero de ofertas: ")
            num_ofertas = int(num_ofertas)
            cod_pais = input("Ingrese el codigo del pais: ")
            nivel = input("Ingrese el nivel de experticia entre (junior, mid, o senior): ")
            
            result = controller.sortJobs(control)
            size = lt.size(result)
            printSortResultsN(result, num_ofertas)
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)


