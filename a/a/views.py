from django.shortcuts import render
from subprocess import *
from os import system

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


    return render(request, "index.html", {"ubicacion":ubicacion, "carpetas":carpetas2, "archivos":archivos2})

def createFile(name):
    com = "touch " + name
    system(com)
    res = getoutput("ls")
    print(res)
    return res

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