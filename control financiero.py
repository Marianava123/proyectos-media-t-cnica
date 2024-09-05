print("¡Bienvenido a la tienda online!")
print("")

#Información del cliente

NOMBRE = input("Ingresa tu nombre completo: ")
DOCUMENTO = int(input("Ingresa tu documento de identidad sin puntos ni comas: "))
EMPRESA = input("Ingresa el nombre de la empresa a la que perteneces: ")
DIREC = input("Ingresa la dirección de la empresas: ")

#Selección del mercado

print("")
print("Opciones de mercado")
print("1. Homcenter")
print("2. El Euro")
print("3. Salir del sistema")

while True:
    mer = int(input("Seleccione el número correspondiente a la opción que desea: "))
    if mer == 1:
        print("Has elegido Homcenter")
        print("")
        H = "Homcenter"
        break;
    elif mer == 2:
        print("Has elegido El Euro")
        print("")
        H = "El Euro"
        break;
    elif mer == 3:
        print("Has salido del sistema")
        exit()
        break;
    else:
        print("Opción inválida")
        
#cotización
TV1 = "Televisor pantalla plana "
TV = 2000000
PC1 = "Computador portátil "
PC = 1600000
CEL1 = "Motorola one fusion "
CEL = 750000
BF1 = "Equipo de sonido "
BF = 1200000
IM1 = "Impresora "
IM = 1000000

VALOR = 0
PRODUCTOS = ""

print("Productos")
print("")
print(f"1. {TV1} ${TV}")
print(f"2. {PC1} ${PC}")
print(f"3. {CEL1} ${CEL}")
print(f"4. {BF1} ${BF}")
print(f"5. {IM1} ${IM}")

while True:
    RES = input("¿Desea agregar algún producto al carrito? si/no ")
    if RES.lower() == "si":
        COMPRA = int(input("Seleccione el número del producto que desea comprar: "))
        if COMPRA == 1:
            print(f" Has elegido el {TV1} ${TV}")
            VALOR += TV
            PRODUCTOS += TV1
            print(f"El valor a pagar es ${VALOR}")
        elif COMPRA == 2:
            print(f"Has elegido el {PC1} ${PC}")
            VALOR += PC
            PRODUCTOS += PC1
            print(f"El valor a pagar es ${VALOR}")
        elif COMPRA == 3:
            print(f"Has elegido el {CEL1} ${CEL}")
            VALOR += CEL
            PRODUCTOS += CEL1
            print(f"El valor a pagar es ${VALOR}")
        elif COMPRA == 4:
            print(f"Has elegido el {BF1} ${BF}")
            VALOR += BF
            PRODUCTOS += BF1
            print(f"El valor a pagar es ${VALOR}")
        elif COMPRA == 5:
            print(f"Has elegido el {IM1} ${IM}")
            VALOR += IM
            PRODUCTOS += IM1
            print (f"El valor a pagar es ${VALOR}")
        else:
            print("Opción inválida, seleccione el número correspondiente al producto que desea comprar")
    elif RES.lower() == "no" and VALOR == 0:
        print("Has salido del sistema")
        print("Gracias por utilizar nuestros servicios :)")
        break;
    elif RES.lower() != "si" and RES.lower() != "no":
        print("Opción inválida")
        print("Recuerda que la respuesta solo es de si o no")
        
    else:
        RES1 = input("Antes de continuar, ¿desea eliminar algún producto del carrito? si/no ")
        if RES1.lower() == "si":
            print(PRODUCTOS)
            ELI = int(input("Seleccione el número correspondiente del producto que desea eliminar: "))
            if ELI == 1:
                if TV1 in PRODUCTOS:
                    print(f" Has elminado el {TV1} ${TV}")
                    VALOR -= TV
                    PRODUCTOS = PRODUCTOS.replace(TV1, "")
                    print(f"El valor a pagar es ${VALOR}")
                else:
                    print(f"El {TV1} no se encuentra en su compra, intente nuevamente con otro producto") 
            elif ELI == 2:
                if PC1 in PRODUCTOS:
                    print(f"Has eliminado el {PC1} ${PC}")
                    VALOR -= PC
                    PRODUCTOS = PRODUCTOS.replace(PC1, "")
                    print(f"El valor a pagar es ${VALOR}")
                else:
                    print(f"El {PC1} no se encuentra en su compra, intente nuevamente con otro producto")
            elif ELI == 3:
                if CEL1 in PRODUCTOS:
                    print(f"Has eliminado el {CEL1} ${CEL}")
                    VALOR -= CEL
                    PRODUCTOS = PRODUCTOS.replace(CEL1, "")
                    print(f"El valor a pagar es ${VALOR}")
                else:
                    print(f"El {CEL1} no se encuentra en su compra, intente nuevamente con otro producto")                   
            elif ELI == 4:
                if BF1 in PRODUCTOS:
                    print(f"Has eliminado el {BF1} ${BF}")
                    VALOR -= BF
                    PRODUCTOS = PRODUCTOS.replace(BF1, "")
                    print(f"El valor a pagar es ${VALOR}")
                else:
                    print(f"El {BF1} no se encuentra en su compra, intente nuevamente con otro producto")
            elif COMPRA == 5:
                if IM1 in PRODUCTOS:
                    print(f"Has eliminado la {IM1} ${IM}")
                    VALOR -= IM
                    PRODUCTOS = PRODUCTOS.replace(IM1, "")
                    print (f"El valor a pagar es ${VALOR}")
                else:
                    print(f"La {IM1} no se encuentra en su compra, intente nuevamente con otro producto")
            else:
               print("Opción inválida, seleccione el número correspondiente al producto que desea eliminar")
        elif RES.lower() == "no" and VALOR == 0:
            print("Has salido del sistema")
            print("Gracias por utilizar nuestros servicios :)")
            break;
        elif RES.lower() != "si" and RES.lower() != "no":
            print("Opción inválida")
            print("Recuerda que la respuesta solo es de si o no")
        else:
                print(f"El total a pagar es de ${VALOR}")
                PAGAR = int(input("Ingrese la cantidad con la que desea pagar: "))
                if PAGAR >= VALOR:
                    DEVOL = PAGAR - VALOR
                    break;
                else:
                    print("Saldo insuficiente, intente con una cantidad mayor")
                    print(f"Recuerde que el valor total es de ${VALOR}")
                    
#FACTURA
print("")
print(f"Factura {H}")
print("")
print(f"Nombre del cliente: {NOMBRE}")
print(f"Número de documento: {DOCUMENTO}")
print(f"Empresa: {EMPRESA}")
print(f"Dirección: {DIREC}")
print("")
print("Productos")
print(PRODUCTOS)
print("")
print(f"Total a pagar ${VALOR}")
print(f"Cantidad recibida ${PAGAR}")
print(f"Cambio ${DEVOL}")
print("")
print("¡Gracias por su compra!")
