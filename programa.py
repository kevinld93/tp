productos=[]

class producto:
    def __init__(self, marca, modelo, velocidadprocesadora, ram, memoriavideo, ssd, puertousb, rj45, wifi, so, cantidadadqui,cantbmin,cantmax,):
        self.marca = marca
        self.modelo = modelo
        self.velocidadprocesadora = velocidadprocesadora
        self.ram = ram
        self.memoriavideo = memoriavideo
        self.ssd,= ssd,
        self.puertousb = puertousb
        self.rj45 = rj45
        self.wifi = wifi
        self.so = so
        self.cantidadadqui = cantidadadqui
        self.cantbmin = cantbmin
        self.cantmax = cantmax
#Se crea una funcion para contar los caracteres en la variable marca
def caracteres(marca):
    
    while len(marca)>20:
        print("Error tiene que ser menor a 20")
        marca=input("Ingrese la marca\n")
    return marca 
#Se crea una funcion para contar los caracteres en la variable modelo
def caracteres2(modelo):
    
    while len(modelo)>20:
        print("Error tiene que ser menor a 20")
        modelo=input("Ingrese el modelo\n")
    return modelo

# Función para agregar un nuevo producto a la lista de productos
def agregar_producto():
    print("Ingrese las caracteristicas de la notebook:")
    marca=caracteres(input("Ingrese marca\n"))
    modelo=caracteres2(input("Ingrese el modelo\n"))
    velocidadprocesadora = input("Ingrese procesador\n")
    ram = input("Ingrese la ram\n")
    memoriavideo =input("Ingrese la memoria de video\n")
    ssd= input("Ingrese el ssd\n")
    puertousb=input("Ingrese la cantidad de puertos usb\n")
    rj45 = input("Ingrese si tiene rj45 si/no \n")
    wifi = input("Ingrese si tiene wifi si/no\n")
    so=input("Ingrese el sistema operativo\n")
    cantidadadqui=input("Ingrese la cantidad adquirida\n")
    cantbmin = input("Ingrese la cantidad minima\n")
    cantmax = input("Ingrese la cantidad maxima\n")
    
    #Se crea objeto
    nuevo_producto = producto(marca, modelo, velocidadprocesadora, ram, memoriavideo, ssd, puertousb, rj45, wifi, so, cantidadadqui,cantbmin,cantmax)
    productos.append(nuevo_producto)
    print("Producto agregado exitosamente.")
    


# Función para mostrar la información de todos los productos
def mostrar_productos():
    for producto in productos:
     print("-" * 40) #Se usa para separar los productos
     print("marca:", producto.marca)
     print("modelo:", producto.modelo)
     print("Velocidad del procesador:", producto.velocidadprocesadora)
     print("memoria ram:", producto.ram)
     print("memoria de video:", producto.memoriavideo)
     print("ssd:", producto.ssd)
     print("cantidad de puerto usb", producto.puertousb)
     print("Puerto rj 45:", producto.rj45)
     print("Tiene wifi:", producto.wifi)
     print("Sistema operativo:", producto.so)
     print("cantidad de notebooks adquiridas:", producto.cantidadadqui)
     print("Cantidad minima:", producto.cantbmin)
     print("Cantidad maxima",producto.cantmax)

#Funcion para eliminar objeto         
def eliminar_objetos():
    delobj=input("Ingrese el modelo a eliminar\n")
    for producto in productos: #recorre la lista 
        if producto.modelo == delobj: #si hay algun objeto con el nombre ingresado en la variable lo elimina
            productos.remove(producto)
            print("El producto con modelo", delobj, "fue eliminado.")
            return

    print("No se encontró ningún producto con el modelo", delobj)
        
# Función que muestra el menu con las opciones
def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Agregar nuevo producto")
    print("2. Mostrar productos")
    print("3. Eliminar productos")
    print("4. Salir")


# Menu principal donde se ingresa el numero y se llama a la funcion
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de opción que desee: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_productos()
        elif opcion=="3":
            eliminar_objetos()
        elif opcion == '4':
            print("Salió del programa")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")
        

if __name__ == "__main__":
    main()

