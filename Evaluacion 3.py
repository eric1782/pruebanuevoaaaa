import json

def cargar_cosa(archivo):
    """
    abrir archivo con proposito de verificacion:
    abre el archivo json y lo lee.
    en caso de no encontrarse info, devuelve una lista vacia.
    """
    try:
        with open(archivo,"r") as leer:
            return json.load(leer)
    except FileNotFoundError:
        return []

def guardar_pedidos(archivo,pedidos):
    """
    Funcion para guardar pedido:
    abrimos el archivo y escribimos en este.
    lo guardamos con un json.dump, ocupando el index 4 para que quede visible de forma legible."""
    with open(archivo,"w") as guardar:
        json.dump(pedidos,guardar,indent=4)

def registrar_pedidos(pedidos,nombre,numero,tipo,fecha,direccion,menu):
    """
    registrar pedido:
    incluye info a guardar: nombre, numero, tipo, fecha, direccion y menu.
    siendo esto guardado en la biblioteca con un pedidos.append.
    """
    pedido = {"nombre" : nombre,
                    "numero" : numero,
                    "tipo" : tipo,
                    "fecha": fecha,
                    "direccion": direccion,
                    "menu": menu}
    pedidos.append(pedido)
    

def listar_pedidos(pedidos):
    """
    lista de pedidos ya registrados:
    ocupamos un try para que cada pedido sea impreso con su info correspondiente.
    si no se encuentra un pedido, se entrega un mensaje donde dice q no hay pedidos que puedan mostarse (porque no hay pedidos registrados)
    """
    for pedido in pedidos:
        print (f"pedido: {pedido["nombre"]}, numero telefonico: {pedido["numero"]}, tipo evento: {pedido["tipo"]}, fecha: {pedido["fecha"]}, direccion: {pedido["direccion"]}, tipo menu: {pedido["menu"]}\n")

def buscar_tipo(pedidos,menu):
    resultados = [pedido for pedido in pedidos if pedido["menu"].lower() == menu.lower()]
    if resultados:
        print("pedidos encontrados: ")
        for pedido in resultados:
            print(f"pedido: {pedido["nombre"]}, numero telefonico: {pedido["numero"]}, tipo evento: {pedido["tipo"]}, fecha: {pedido["fecha"]}, direccion: {pedido["direccion"]}, tipo menu: {pedido["menu"]}\n")
        else:
            print("no hay pedidos con este tipo de menu registrados")
def main():
    correr = 1
    archivo = "pedidos.json"
    pedidos = cargar_cosa(archivo)
    while correr == 1:
        print("bienvenido, escoge una opcion: ")
        print("1.-Listar pedidos hechos")
        print("2.- Registrar un pedido")
        print("3.- Ver detalle de pedidos por tipo de menu")
        print("4.- Salir")
        opcion = input("Ingrese el numero de opcion que desea realizar: ")

        if opcion == "1":
            listar_pedidos(pedidos)
        elif opcion == "2":
            nombre = input("Nombre: ")
            numero = input("Numero telefonico: ")
            tipo = input("Tipo de evento: ")
            fecha = input("Fecha de pedido: ")
            direccion = input("Direccion: ")
            menu = input("Tipo de menu (comida italiana, comida japonesa o BBQ): ")
            registrar_pedidos(pedidos,nombre,numero,tipo,fecha,direccion,menu)
            guardar_pedidos(archivo,pedidos)
        elif opcion == "3":
           menu= input("genero a buscar (comida italiana, comida japonesa o BBQ): ")
           buscar_tipo(pedidos,menu)
        elif opcion == "4":
            break
        else:
            print("imprime una opcion valida ")
    
if __name__ == "__main__":
    main()



