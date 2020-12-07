from django.shortcuts import render
from subprocess import *
from os import system
from django import forms

def inicio(request):


    ubicacion = getoutput("pwd")
    carpetas = getoutput("find . -maxdepth 1 -type d")
    carpetas = carpetas.split("\n")
    carpetas2 = []
    for i in range(1, len(carpetas)):
        carpetas2.append(carpetas[i][2:])


    archivos = getoutput("find . -maxdepth 1 -type f")
    archivos = archivos.split("\n")
    archivos2 = []
    for i in range(len(archivos)):
        archivos2.append(archivos[i][2:])


    return render(request, "index2.html", {"ubicacion":ubicacion, "carpetas":carpetas2, "archivos":archivos2})

def buscar(request):

    busqueda = request.GET["aBuscar"]
    ubicacion = getoutput("pwd")
    carpetas = getoutput(f"find . -maxdepth 1 -type d | grep {busqueda}")
    carpetas = carpetas.split("\n")
    carpetas2 = []
    for i in range(1, len(carpetas)):
        carpetas2.append(carpetas[i][2:])


    archivos = getoutput(f"find . -maxdepth 1 -type f | grep {busqueda}")
    archivos = archivos.split("\n")
    archivos2 = []
    for i in range(len(archivos)):
        archivos2.append(archivos[i][2:])


    return render(request, "index2.html", {"ubicacion":ubicacion, "carpetas":carpetas2, "archivos":archivos2, "busqueda":busqueda})

def crearA(request):
    if (request.GET["opcion1"])[0] in ["A", "a"]:
        try:
            name = request.GET["creado"]
            system(f"touch {name}")
            mensaje = "El archivo fue creado con exito"
        except:
            mensaje = ""

    elif (request.get["opcion1"])[0] in ["C", "c"]:
        try:
            name = request.GET["creado"]
            system(f"mkdir {name}")
            mensaje = "La carpeta fue creada con exito"
        except:
            mensaje = ""

    else:
        mensaje = "Por favor ingrese 'Carpeta' o 'Archivo'"

    ubicacion = getoutput("pwd")
    carpetas = getoutput("find . -maxdepth 1 -type d")
    carpetas = carpetas.split("\n")
    carpetas2 = []
    for i in range(1, len(carpetas)):
        carpetas2.append(carpetas[i][2:])

    archivos = getoutput("find . -maxdepth 1 -type f")
    archivos = archivos.split("\n")
    archivos2 = []
    for i in range(len(archivos)):
        archivos2.append(archivos[i][2:])

    return render(request, "crear.html", {"ubicacion":ubicacion, "carpetas":carpetas2, "archivos":archivos2, "mensaje":mensaje})

def createFolder(name):
    com = "mkdir " + name
    system(com)
    res = getoutput("ls")
    print(res)
    return res

def changeName(oldName, newName):
    com = "mv " + oldName + " " + newName
    system(com)
    res = getoutput("ls")
    print(res)
    return res

def delete(name):
    com = "rm -r " + name
    system(com)
    res = getoutput("ls")
    print(res)
    return res

def copyAndPaste(name, location):
    com = "cp -r " + name + " " + location
    system(com)
    res = getoutput("ls")
    print(res)
    return res

def seeInfo(name):
    com = "ls -l " + name
    system(com)
    res = getoutput(com)
    print(res)
    return res

def changeInfo(name, number):
    com = "chmod " + number + " " + name
    system(com)
    res = getoutput(seeInfo(name))
    print(res)
    return res

def changeOwner(name, newOwner):
    com = "chown " + newOwner + " " + name
    system(com)
    res = getoutput(seeInfo(name))
    print(res)
    return res

def move(name, location):
    changeName(name, location)
    return "Success"

def cut(name, location):
    copyAndPaste(name, location)
    com = "rm -r " + name
    system(com)
    return "Success"

cut("Nuevo", "./Final")