def new_list():
    newlist = {"elementos" : [],
               "size" : 0,
               }
    return newlist

def add_last(lista, elemento):
    lista["elementos"].append(elemento)
    lista["size"] += 1
    return lista

def get_element(lista,pos):
    if lista["size"] < pos-1 < lista["size"] or isEmpty(lista) == True:
        return None
    else:
        return lista["elementos"][pos-1]          
    
def get_first(lista):
    if isEmpty(lista) == True:
        return None
    else:
        return lista["elementos"][0]

def isPresent(lista,elem):
    # Da la posición de un elemento si se encuentra dentro de la lista
    if isEmpty(lista) == True:
        return -1
    else:
        count = 1
        for i in lista["elementos"]:
            for key in i:
                llave = i[key]
                if  llave == elem:
                    return count
            count += 1
                
        return -1

def size(lista):
    return lista["size"]

def selection_sort(lista,criterio):
    for i in range (len(lista["elementos"])):
        min = i
        for j in range (i+1, len(lista)):
            if lista[j]<lista[min]:
                min = j
        temp = lista[i]
        lista[i] = lista[min]
        lista[min] = temp
    return lista

def insertion_sort(lista,criterio):
    for i in range(len(lista)):
        to_change = i
        for j in range(i-1,1,-1):
            if lista[i] < lista[j]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
                to_change = j
    return lista

def shell_sort(lista,criterio):
    n = size(lista)
    sec = 1
    while sec < n/3:
        sec = 3*sec + 1
    while (sec >= 1):
        for i in range(sec,n):
            j = i
            while (j >= sec) and criterio(get_element(lista,j+1),get_element(lista,j-sec+1)):
                exchange(lista,j+1,j-sec+1)
                j -= sec
        sec //= 3
    return lista

def delete(lista,pos):
    if isEmpty(lista) == True:
        return lista
    else:
        lista["elementos"].pop(pos)
        lista["size"] -= 1
        return lista

def isEmpty(lista):
    if lista["size"] == 0:
        return True
    else:
        return False
    
def iterator(lista):
    if not isEmpty(lista):
        ini = 0
        while ini < lista["size"]:
            resp = lista["elementos"]
            ini += 1
            return resp
        
def exchange(lista, pos1, pos2):
    info1 = get_element(lista,pos1)
    info2 = get_element(lista,pos2)
    lista["elementos"][pos1-1] = info2
    lista["elementos"][pos2-1] = info1
    return lista