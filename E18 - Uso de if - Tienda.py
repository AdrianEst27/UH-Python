import pandas as pd

def mostrar_menu(productos):
    df = pd.DataFrame(productos.items(), columns=['Producto', 'Precio'])
    df['Precio'] = df['Precio'].apply(lambda x: f"${x:.2f}")

    print("\n > CybeRupi Tienda en Línea <\n")
    print(f"{'Productos':<40} {'Precio':>10}")
    print('-' * 54)

    for idx, row in df.iterrows():
        print(f"{idx + 1}. {row['Producto']:<40} {row['Precio']:>10}")

    return df

def seleccionar_productos(df):
    seleccion = []
    while True:
        try:
            eleccion = input("Selecciona un producto por su número (o escribe 'fin' para terminar): ")
            if eleccion.lower() == 'fin':
                break
            
            index = int(eleccion) - 1  # Convertir a índice (0 basado)
            if 0 <= index < len(df):
                seleccion.append(df.iloc[index])  # Agregar el producto completo
                print(f"Producto agregado: {df.iloc[index]['Producto']}")
            else:
                print("Número no válido. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Debes ingresar un número o 'fin'.")

    return seleccion

def calcular_total(seleccion, es_vip):
    if not seleccion:
        print("No se han seleccionado productos.")
        return 0, 0  # Retornar 0 si no hay selección
    
    # Sumar los precios originales (sin formatear)
    total = sum(producto['Precio'] for producto in seleccion)
    
    # Aplicar descuentos
    if total < 50:
        descuento = 0
    elif 50 <= total < 100:
        descuento = total * 0.10
    else:
        descuento = total * 0.20
    
    if es_vip:
        descuento += total * 0.05  # Descuento adicional VIP
    
    total_con_descuento = total - descuento
    return total, total_con_descuento

def aplicar_recargo(total_con_descuento, metodo_pago):
    if metodo_pago.lower() == "efectivo":
        recargo = total_con_descuento * 0.05  # 5% de recargo
        total_final = total_con_descuento + recargo
    else:
        total_final = total_con_descuento
    
    return total_final

#main():
productos = {
        "RTX 4090 SUPER OC 12GB": 40000.0,
        "RTX 4060 Ti 8GB": 13000.0,
        "Intel Core i9 14900K": 15000.0,
        "Memoria RAM 16GB": 800.0,
        "Disco Duro SSD 1TB": 1200.0,
        "Fuente de Poder 750W": 1000.0,
        "Gabinete RGB": 700.0,
        "Refrigeración Líquida": 1200.0,
    }

    df = mostrar_menu(productos)
    seleccion = seleccionar_productos(df)

    # Verificar que se seleccionaron productos
    if not seleccion:
        print("No has seleccionado ningún producto. El programa se cerrará.")
        return

    # Preguntar si es VIP
    es_vip = input("¿Eres miembro VIP? (sí/no): ").strip().lower() == "sí"

    total, total_con_descuento = calcular_total(seleccion, es_vip)

    # Preguntar método de pago
    metodo_pago = input("Ingresa el método de pago (efectivo/tarjeta): ").strip().lower()
    total_final = aplicar_recargo(total_con_descuento, metodo_pago)

    # Mostrar resultados
    print(f"\nTotal sin descuento: ${total:.2f}")
    print(f"Total con descuento: ${total_con_descuento:.2f}")
    print(f"Total final (con recargo si es efectivo): ${total_final:.2f}")
    print("¡Gracias por tu compra!")
