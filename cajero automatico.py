print ("Bienvenido al cajero automático")
print ("")
print ("Por favor, seleccione su banco de la lista a continuación")
print ("1: Bancolombia")
print ("2: Banco de bogotá")
print ("3: Avevilla")
print ("4: Otro")
while True:

    BANCO = int(input("Escoga el número correspondiente a la opción que desea: "))
    if BANCO == 1 or BANCO == 2 or BANCO == 3 or BANCO == 4:
        if BANCO ==1:
           print("Ha elegido Bancolombia")
           break;
        elif BANCO ==2:
           print("Ha elegido Banco de Bogotá")
           break;
        elif BANCO ==3:
           print("Ha elegido Avevilla")
           break;
        elif BANCO ==4:
           print("Ha elegido otro")
           break;
        else:
           print("Opción invalida")
           break;
    else:
        print("Opción no válida. Por favor, seleccione una opción válida del menú")
    
print ("")
print ("¿Con qué modo desea continuar?")
print ("1: Tarjeta")
print ("2: Código")

while True:

    FORMA = int(input("Escoga el número correspondiente a la opción que desea: "))
    if FORMA ==1 or FORMA ==2:
        if FORMA==1:
            print("Ha elegido tarjeta")
            break;
        elif FORMA ==2:
            print("Ha elegido código")
            break;
        else:
            print("Opción inválida")
            break;
    else:
        print("Opción no válida. Por favor, seleccione una opción válida del menú")

SALDO = 1462000
CONTRASEÑA = 2024
CONTADOR = 1
while CONTADOR <= 3:
    print ("")
    SIONO = input("¿Desea continuar? Responda con si/no: ")
    if SIONO.lower() == "si":
        if FORMA ==1:
           C = int(input("Ingrese su contraseña: "))
        elif FORMA ==2:
            C = int(input("Ingrese su código: "))
        if C == CONTRASEÑA:
                print ("")
                print("Menú")
                print("1: Consultar saldo")
                print("2: Depositar")
                print("3: Retirar")
                print("4: Salir")
                RES = int(input("Seleccione una opción: "))
                if RES == 1:
                   print ("")
                   print(f"Consulta de saldo exitosa. Tu saldo actual es de ${SALDO}")
                   print ("¡Gracias por utilizar nuestros servicios!")
                elif RES == 2:
                    DEPO = int(input("Por favor, ingrese la cantidad que desea depositar "))
                    SALDO += DEPO
                    print("")
                    print (f"Depósito exitoso. Se ha acreditado ${DEPO}, a tu cuenta")
                    print(f"Tu saldo actual es de ${SALDO}")
                    print ("¡Gracias por utilizar nuestros servicios!")
                elif RES == 3:
                    DEPO = int(input("Por favor, ingrese la cantidad que desea retirar "))
                    if DEPO <= SALDO:
                       SALDO -= DEPO
                       print ("")
                       print (f"Retiro exitoso. Se ha dispensado ${DEPO}, de tu cuenta")
                       print(f"Tu saldo actual es de ${SALDO}")
                       print ("¡Gracias por utilizar nuestros servicios!")
                    else:
                       print("Fondos insuficientes. Por favor, intentente con una cantidad menor")
                elif RES == 4:
                     print ("")
                     print("Ha salido del sistema")
                     print ("¡Gracias por utilizar nuestros servicios!")
                     break;
                else:
                     print("Opción no válida. Por favor, seleccione una opción válida del menú")
        else:
               print("Contraseña incorrecta")
               CONTADOR += 1
               if CONTADOR == 4:
                  print("Demasiados intentos fallidos")
                  break;
    elif SIONO.lower() == "no":
        print("Ha salido del sistema")
        print ("¡Gracias por utilizar nuestros servicios!")
        break;
    else:
        print("Opción inválida")
        break;

     
        
    
    
    
    

