from django.shortcuts import render
from subprocess import *
from os import system
from django import forms

def inicio(request):

    system("cd /home")

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

    lArchivos = []
    rArchivos = [[]]
    lCarpetas = []
    rCarpetas = [[]]

    for i in range(len(archivos2) // 6):
        lArchivos.append([])
        for j in range(6):
            lArchivos[i].append(archivos2[i * 6 + j])

    for i in range(-1, -(len(archivos2) % 6) - 1, -1):
        rArchivos[0].append(archivos2[i])

    for i in range(len(carpetas2) // 6):
        lCarpetas.append([])
        for j in range(6):
            lCarpetas[i].append(carpetas2[i * 6 + j])

    for i in range(-1, -(len(carpetas2) % 6) - 1, -1):
        rCarpetas[0].append(carpetas2[i])

    return render(request, "index2.html",
                  {"ubicacion": ubicacion, "carpetas": carpetas2, "archivos": archivos2,
                   "lArchivos": lArchivos, "rArchivos": rArchivos, "lCarpetas": lCarpetas, "rCarpetas": rCarpetas,
                   "numeros": [1, 2, 3, 4, 5, 6, 7, 8]})


def buscar(request):

    busqueda = request.GET["aBuscar"]
    ubicacion = getoutput("pwd")
    carpetas = getoutput(f"find . -maxdepth 1 -type d | grep {busqueda} -i")
    carpetas = carpetas.split("\n")
    carpetas2 = []
    for i in range(1, len(carpetas)):
        carpetas2.append(carpetas[i][2:])


    archivos = getoutput(f"find . -maxdepth 1 -type f | grep {busqueda} -i")
    archivos = archivos.split("\n")
    archivos2 = []
    for i in range(len(archivos)):
        archivos2.append(archivos[i][2:])

    lArchivos = []
    rArchivos = [[]]
    lCarpetas = []
    rCarpetas = [[]]

    for i in range(len(archivos2) // 6):
        lArchivos.append([])
        for j in range(6):
            lArchivos[i].append(archivos2[i * 6 + j])

    for i in range(-1, -(len(archivos2) % 6) - 1, -1):
        rArchivos[0].append(archivos2[i])

    for i in range(len(carpetas2) // 6):
        lCarpetas.append([])
        for j in range(6):
            lCarpetas[i].append(carpetas2[i * 6 + j])

    for i in range(-1, -(len(carpetas2) % 6) - 1, -1):
        rCarpetas[0].append(carpetas2[i])

    return render(request, "index2.html",
                  {"ubicacion": ubicacion, "carpetas": carpetas2, "archivos": archivos2,
                   "lArchivos": lArchivos, "rArchivos": rArchivos, "lCarpetas": lCarpetas, "rCarpetas": rCarpetas,
                   "numeros": [1, 2, 3, 4, 5, 6, 7, 8]})


def crearA(request):

    try:
        name = request.GET["creado"]
        system(f"touch {name}")
        mensaje = "El archivo fue creado con exito"
    except:
        mensaje = ""

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
    lArchivos = []
    rArchivos = [[]]
    lCarpetas = []
    rCarpetas = [[]]


    for i in range(len(archivos2)//6):
        lArchivos.append([])
        for j in range(6):
            lArchivos[i].append(archivos2[i*6+j])

    for i in range(-1,-(len(archivos2)%6)-1,-1):
        rArchivos[0].append(archivos2[i])

    for i in range(len(carpetas2)//6):
        lCarpetas.append([])
        for j in range(6):
            lCarpetas[i].append(carpetas2[i*6+j])

    for i in range(-1,-(len(carpetas2)%6)-1,-1):
        rCarpetas[0].append(carpetas2[i])


    return render(request, "crearA.html", {"ubicacion":ubicacion, "carpetas":carpetas2, "archivos":archivos2, "mensaje":mensaje, "lArchivos":lArchivos, "rArchivos":rArchivos, "lCarpetas":lCarpetas, "rCarpetas":rCarpetas, "numeros":[1,2,3,4,5,6,7,8]})

def crearC(request):

    try:
        name = request.GET["creado"]
        system(f"mkdir {name}")
        mensaje = "La carpeta fue creada con exito"
    except:
        mensaje = ""

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

    lArchivos = []
    rArchivos = [[]]
    lCarpetas = []
    rCarpetas = [[]]

    for i in range(len(archivos2) // 6):
        lArchivos.append([])
        for j in range(6):
            lArchivos[i].append(archivos2[i * 6 + j])

    for i in range(-1, -(len(archivos2) % 6) - 1, -1):
        rArchivos[0].append(archivos2[i])

    for i in range(len(carpetas2) // 6):
        lCarpetas.append([])
        for j in range(6):
            lCarpetas[i].append(carpetas2[i * 6 + j])

    for i in range(-1, -(len(carpetas2) % 6) - 1, -1):
        rCarpetas[0].append(carpetas2[i])

    return render(request, "crearC.html",
                  {"ubicacion": ubicacion, "carpetas": carpetas2, "archivos": archivos2, "mensaje": mensaje,
                   "lArchivos": lArchivos, "rArchivos": rArchivos, "lCarpetas": lCarpetas, "rCarpetas": rCarpetas,
                   "numeros": [1, 2, 3, 4, 5, 6, 7, 8]})


def cambiarN(request):

    try:
        nombreV = request.POST["viejo"]
        nombreN = request.POST["nuevo"]
        system(f"mv {nombreV} {nombreN}")
        mensaje = "El nombre del archivo fue cambiado con exito"
    except:
        mensaje = ""

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

    lArchivos = []
    rArchivos = [[]]
    lCarpetas = []
    rCarpetas = [[]]

    for i in range(len(archivos2) // 6):
        lArchivos.append([])
        for j in range(6):
            lArchivos[i].append(archivos2[i * 6 + j])

    for i in range(-1, -(len(archivos2) % 6) - 1, -1):
        rArchivos[0].append(archivos2[i])

    for i in range(len(carpetas2) // 6):
        lCarpetas.append([])
        for j in range(6):
            lCarpetas[i].append(carpetas2[i * 6 + j])

    for i in range(-1, -(len(carpetas2) % 6) - 1, -1):
        rCarpetas[0].append(carpetas2[i])

    return render(request, "cambiarN.html",
                  {"ubicacion": ubicacion, "carpetas": carpetas2, "archivos": archivos2, "mensaje": mensaje,
                   "lArchivos": lArchivos, "rArchivos": rArchivos, "lCarpetas": lCarpetas, "rCarpetas": rCarpetas,
                   "numeros": [1, 2, 3, 4, 5, 6, 7, 8]})

def eliminar(request):

    try:
        eliminar = request.GET["eliminar"]
        system(f"rm -rf {eliminar}")
        mensaje = "El archivo fue eliminado con exito"
    except:
        mensaje = ""

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

    lArchivos = []
    rArchivos = [[]]
    lCarpetas = []
    rCarpetas = [[]]

    for i in range(len(archivos2) // 6):
        lArchivos.append([])
        for j in range(6):
            lArchivos[i].append(archivos2[i * 6 + j])

    for i in range(-1, -(len(archivos2) % 6) - 1, -1):
        rArchivos[0].append(archivos2[i])

    for i in range(len(carpetas2) // 6):
        lCarpetas.append([])
        for j in range(6):
            lCarpetas[i].append(carpetas2[i * 6 + j])

    for i in range(-1, -(len(carpetas2) % 6) - 1, -1):
        rCarpetas[0].append(carpetas2[i])

    return render(request, "eliminar.html",
                  {"ubicacion": ubicacion, "carpetas": carpetas2, "archivos": archivos2, "mensaje": mensaje,
                   "lArchivos": lArchivos, "rArchivos": rArchivos, "lCarpetas": lCarpetas, "rCarpetas": rCarpetas,
                   "numeros": [1, 2, 3, 4, 5, 6, 7, 8]})


def copiar(request):

    try:
        inicio = request.POST["inicio"]
        destino = request.POST["destino"]
        system(f"cp -r {inicio} {destino}")
        mensaje = "El archivo fue copiado con exito"
    except:
        mensaje = ""

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

    lArchivos = []
    rArchivos = [[]]
    lCarpetas = []
    rCarpetas = [[]]

    for i in range(len(archivos2) // 6):
        lArchivos.append([])
        for j in range(6):
            lArchivos[i].append(archivos2[i * 6 + j])

    for i in range(-1, -(len(archivos2) % 6) - 1, -1):
        rArchivos[0].append(archivos2[i])

    for i in range(len(carpetas2) // 6):
        lCarpetas.append([])
        for j in range(6):
            lCarpetas[i].append(carpetas2[i * 6 + j])

    for i in range(-1, -(len(carpetas2) % 6) - 1, -1):
        rCarpetas[0].append(carpetas2[i])

    return render(request, "copiar.html",
                  {"ubicacion": ubicacion, "carpetas": carpetas2, "archivos": archivos2, "mensaje": mensaje,
                   "lArchivos": lArchivos, "rArchivos": rArchivos, "lCarpetas": lCarpetas, "rCarpetas": rCarpetas,
                   "numeros": [1, 2, 3, 4, 5, 6, 7, 8]})


def mover(request):

    try:
        nombreV = request.POST["viejo"]
        nombreN = request.POST["nuevo"]
        system(f"mv -r {nombreV} {nombreN}")
        mensaje = "El archivo se movio con exito"
    except:
        mensaje = ""

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

    lArchivos = []
    rArchivos = [[]]
    lCarpetas = []
    rCarpetas = [[]]

    for i in range(len(archivos2) // 6):
        lArchivos.append([])
        for j in range(6):
            lArchivos[i].append(archivos2[i * 6 + j])

    for i in range(-1, -(len(archivos2) % 6) - 1, -1):
        rArchivos[0].append(archivos2[i])

    for i in range(len(carpetas2) // 6):
        lCarpetas.append([])
        for j in range(6):
            lCarpetas[i].append(carpetas2[i * 6 + j])

    for i in range(-1, -(len(carpetas2) % 6) - 1, -1):
        rCarpetas[0].append(carpetas2[i])

    return render(request, "mover.html",
                  {"ubicacion": ubicacion, "carpetas": carpetas2, "archivos": archivos2, "mensaje": mensaje,
                   "lArchivos": lArchivos, "rArchivos": rArchivos, "lCarpetas": lCarpetas, "rCarpetas": rCarpetas,
                   "numeros": [1, 2, 3, 4, 5, 6, 7, 8]})


def verPermisos(request):

    try:
        nombre = request.GET["nombre"]
        mensaje=getoutput(f"ls -l {nombre}")
        nombre = f"La informacion del objeto {nombre} es:"
    except:
        mensaje = ""
        nombre = ""


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

    lArchivos = []
    rArchivos = [[]]
    lCarpetas = []
    rCarpetas = [[]]

    for i in range(len(archivos2) // 6):
        lArchivos.append([])
        for j in range(6):
            lArchivos[i].append(archivos2[i * 6 + j])

    for i in range(-1, -(len(archivos2) % 6) - 1, -1):
        rArchivos[0].append(archivos2[i])

    for i in range(len(carpetas2) // 6):
        lCarpetas.append([])
        for j in range(6):
            lCarpetas[i].append(carpetas2[i * 6 + j])

    for i in range(-1, -(len(carpetas2) % 6) - 1, -1):
        rCarpetas[0].append(carpetas2[i])

    return render(request, "verPermisos.html",
                  {"ubicacion": ubicacion, "carpetas": carpetas2, "archivos": archivos2, "mensaje": mensaje,
                   "lArchivos": lArchivos, "rArchivos": rArchivos, "lCarpetas": lCarpetas, "rCarpetas": rCarpetas,
                   "numeros": [1, 2, 3, 4, 5, 6, 7, 8], "archivo":nombre})


def modificarPermisos(request):

    try:
        nombre = request.POST["nombre"]
        numero = str(request.POST["numero"])
        system(f"chmod -R {numero} {nombre}")
        mensaje=getoutput(f"ls -l {nombre}")
        nombre = f"La nueva informacion del objeto {nombre} es:"
    except:
        mensaje = ""
        nombre = ""


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

    lArchivos = []
    rArchivos = [[]]
    lCarpetas = []
    rCarpetas = [[]]

    for i in range(len(archivos2) // 6):
        lArchivos.append([])
        for j in range(6):
            lArchivos[i].append(archivos2[i * 6 + j])

    for i in range(-1, -(len(archivos2) % 6) - 1, -1):
        rArchivos[0].append(archivos2[i])

    for i in range(len(carpetas2) // 6):
        lCarpetas.append([])
        for j in range(6):
            lCarpetas[i].append(carpetas2[i * 6 + j])

    for i in range(-1, -(len(carpetas2) % 6) - 1, -1):
        rCarpetas[0].append(carpetas2[i])

    return render(request, "modificarPermisos.html",
                  {"ubicacion": ubicacion, "carpetas": carpetas2, "archivos": archivos2, "mensaje": mensaje,
                   "lArchivos": lArchivos, "rArchivos": rArchivos, "lCarpetas": lCarpetas, "rCarpetas": rCarpetas,
                   "numeros": [1, 2, 3, 4, 5, 6, 7, 8], "archivo":nombre})

def modificarPropietario(request):

    try:
        nombre = request.POST["nombre"]
        propietario = str(request.POST["propietario"])
        system(f"chown -R {propietario} {nombre}")
        mensaje=getoutput(f"ls -l {nombre}")
        nombre = f"La nueva informacion del objeto {nombre} es:"
    except:
        mensaje = ""
        nombre = ""


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

    lArchivos = []
    rArchivos = [[]]
    lCarpetas = []
    rCarpetas = [[]]

    for i in range(len(archivos2) // 6):
        lArchivos.append([])
        for j in range(6):
            lArchivos[i].append(archivos2[i * 6 + j])

    for i in range(-1, -(len(archivos2) % 6) - 1, -1):
        rArchivos[0].append(archivos2[i])

    for i in range(len(carpetas2) // 6):
        lCarpetas.append([])
        for j in range(6):
            lCarpetas[i].append(carpetas2[i * 6 + j])

    for i in range(-1, -(len(carpetas2) % 6) - 1, -1):
        rCarpetas[0].append(carpetas2[i])

    return render(request, "modificarPropietario.html",
                  {"ubicacion": ubicacion, "carpetas": carpetas2, "archivos": archivos2, "mensaje": mensaje,
                   "lArchivos": lArchivos, "rArchivos": rArchivos, "lCarpetas": lCarpetas, "rCarpetas": rCarpetas,
                   "numeros": [1, 2, 3, 4, 5, 6, 7, 8], "archivo":nombre})


