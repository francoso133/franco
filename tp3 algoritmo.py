import os
import pickle
import os.path

class usuario:
    def __init__(self):
        self.codUsuario = 0
        self.nombreUsuario = " " # mail administrador, dueño del local, del cliente
        self.claveUsuario = " " 
        self.tipoUsuario = " " # administrador, dueño local cliente


class local:
    def __init__(self):
        self.codLocal = 0
        self.nombreLocal = " "
        self.ubicacionLocal = " "
        self.rubroLocal = " " # indumentaria, perfumeria, comida
        self.codUsuario = 0 # codigo del dueño del local
        self.estado = " "

class pormociones: 
    def __init__(self):
        self.codPRomo = 0
        self.textoPromo = " "
        self.fechaDesdePromo = "aaaa - mm - dd"
        self.fechaHastaPromo = "aaaa - mm - dd"
        self.diasSemana = [0]*6 
        self.estado = " " #pendiente, aprobado rechazado
        self.codLocal = 0
    
class Uso_promociones:
    def __init__ (self):
        self.codCliente = 0
        self.codPromo = 0 
        self.fechaUsoPromo = "aaaa - mm - dd"

class novedades:
    def __init__ (self): 
        self.codNovedades = 0
        self.textoNovedades = " "
        self.fechaDesdeNovedad = " "
        self.fechaHastaNovedad =" "
        self.tipoUsuario = " " #dueño local, cliente
        self.estado = " "


### PROGRAMA PRINCIPAL ###
if not os.path.exists('c:\\tp3'):
    os.mkdir ('c:\\tp3')
else:
    print ("El directorio ya existe")
afUsuarios = "c:\\tp3\\usuarios.dat"
afLocales = "c:\\tp3\\locales.dat"
afPromos = "c:\\tp3\\promociones.dat"
afUsosPromos = "c:\\tp3\\usospromo.dat"
afNovedades= "c:\\tp3\\novedades.dat"

if not os.path.exists(afUsuarios):
    alusuarios = open(afUsuarios, "w+b")
else:
    alusuarios  = open(afUsuarios, "r+b")

if not os.path.exists(afLocales):
    alLocales = open(afLocales, "w+b")
else:
    alLocales = open(afLocales, "r+b")

if not os.path.exists(afPromos):
    alPromos = open(afPromos,"w+b")
else:
    alPromos = open(afPromos, "r+b")

if not os.path.exists(afUsosPromos):
    alUsosPromos = open(afUsosPromos ,"w+b")
else: 
    alUsosPromos = open(afUsosPromos , "r+b")

if not os.path.exists(afNovedades):
    alNovedades = open(afNovedades, 'w+b')
else:
    alNovedades = open(afNovedades,'r+b')

usuarios = usuario()
if os.path.getsize(afUsuarios) == 0:
    usuarios.codUsuario = 1
    usuarios.nombreUsuario = "admin@shopping.com"
    usuarios.claveUsuario = 12345
    usuarios.tipoUsuario = "administrador"
    alusuarios.seek(0,2)
    pickle.dump(usuarios, alusuarios)



# Crear un nuevo objeto de usuario
nuevo_usuario = usuario()
# Solicitar al usuario que ingrese los detalles del nuevo usuario
nuevo_usuario.codUsuario = usuarios.codUsuario + 1
nuevo_usuario.nombreUsuario = input('Por favor, ingresa el nombre de usuario: ')
nuevo_usuario.claveUsuario = input('Por favor, ingresa la clave de usuario: ')
nuevo_usuario.tipoUsuario = "cliente" # hacer dentro del adminsitrador la opcion para que el pueda crear dueños de clientes

# Guardar el nuevo objeto de usuario en el archivo
alusuarios.seek(0,2)
pickle.dump(nuevo_usuario, alusuarios)

