
# TODO: Sistema de Gestión de Tiendas en Línea

def mostrar_menu_productos(productos):

    """ Función para mostrar el menú de productos. """

    print("\nProductos                                    Precio")
    print("-" * 55)
    for i, (producto, precio) in enumerate(productos.items(), start=1):
        print(f"{i}. {producto:<40} ${precio:>10.2f}")

def main():
    # Productos y precios
    productos = {
        "RTX 4090 SUPER OC 12GB": 40000,
        "RTX 4060 Ti 8GB": 13000,
        "Intel Core i9 14900K": 15000,
        "Memoria RAM 16GB": 800,
        "Disco Duro SSD 1TB": 1200,
        "Fuente de Poder 750W": 1000,
        "Gabinete RGB": 700,
        "Refrigeración Líquida": 1200
    }
    
    # Para que el título del menú se vea centrado.
    titulo = "Rupi PC Componentes"
    print(f"\n{'> ' + titulo + ' <':^50}")

    mostrar_menu_productos(productos)
    print("\n")

    total_compra = 0
    while True:
        seleccion = input(" > Selecciona un producto por su número (o escribe 'fin' para terminar): ")
        if seleccion.lower() == 'fin':
            break
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(productos):
            total_compra += list(productos.values())[int(seleccion) - 1]
        else:
            print(" > Selección no válida. Intenta nuevamente.")

    # Pregunta si el usuario es VIP o no
    vip = input("\n > ¿Eres miembro VIP? (si/no): ").lower() == 'si'

    # Aplica un decuento dependiendo el total de la compra
    descuento = 0

    if total_compra < 50: descuento = 0
    elif total_compra <= 100: descuento = total_compra * 0.1
    
    # Aplica un descuento si es VIP
    if vip: descuento += total_compra * 0.05

    # Calcula el total de la compra con descuento
    total_con_descuento = total_compra - descuento

    # Pregunta el método de pago
    metodo_pago = input(" > Método de pago (tarjeta/efectivo): ").lower()

    # Aplica el recargo si el insolente paga en efectivo
    if metodo_pago == 'efectivo': total_con_descuento *= 1.05

    # Muestra el total de la compra
    print(f"\n > Subtotal: {total_compra}")
    print(f" > Descuento: {descuento}")
    print(f" > Total de la compra: ${total_con_descuento:.2f}")
    print(" > ¡Gracias por tu compra!")

main()
