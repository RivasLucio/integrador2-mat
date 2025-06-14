import datetime # Importa datetime al principio del archivo

# --- Funciones para la Parte 2.A: Operaciones con DNIs ---

def obtener_dnis():
    """
    Solicita o utiliza los DNIs de los integrantes del grupo
    y los devuelve como una lista de strings.
    """
    dnis = []
    dnis.append("43322920") # DNI del Alumno 1
    dnis.append("46351157") # DNI del Alumno 2
    return dnis

def generar_conjuntos_dnis(lista_dnis):
    """
    Recibe una lista de DNIs (strings) y devuelve una lista de conjuntos de dígitos únicos.
    """
    conjuntos = []
    for dni in lista_dnis:
        # Convierte el string del DNI a un conjunto de sus dígitos
        conjunto_digitos = set(int(digito) for digito in dni)
        conjuntos.append(conjunto_digitos)
    return conjuntos

def realizar_operaciones_conjuntos(conjunto1, conjunto2):
    """
    Realiza y muestra las operaciones de unión, intersección,
    diferencia y diferencia simétrica entre dos conjuntos.
    """
    print(f"\n--- Operaciones entre Conjunto 1 ({conjunto1}) y Conjunto 2 ({conjunto2}) ---")
    
    union = conjunto1.union(conjunto2)
    print(f"Unión: {union}")

    interseccion = conjunto1.intersection(conjunto2)
    print(f"Intersección: {interseccion}")

    diferencia1_2 = conjunto1.difference(conjunto2)
    print(f"Diferencia (Conjunto1 - Conjunto2): {diferencia1_2}")
    
    diferencia2_1 = conjunto2.difference(conjunto1)
    print(f"Diferencia (Conjunto2 - Conjunto1): {diferencia2_1}")

    diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
    print(f"Diferencia Simétrica: {diferencia_simetrica}")

def contar_frecuencia_digitos(dni):
    """
    Cuenta y muestra la frecuencia de cada dígito en un DNI dado.
    """
    frecuencia = {}
    for digito_str in dni:
        digito = int(digito_str)
        frecuencia[digito] = frecuencia.get(digito, 0) + 1
    
    print(f"\nFrecuencia de dígitos en DNI {dni}:")
    for digito, count in frecuencia.items():
        print(f"  Dígito {digito}: {count} veces")

def sumar_digitos_dni(dni):
    """
    Calcula y muestra la suma total de los dígitos de un DNI.
    """
    suma = 0
    for digito_str in dni:
        suma += int(digito_str)
    print(f"Suma total de los dígitos del DNI {dni}: {suma}")
    return suma

def evaluar_condiciones_logicas_dnis(conjuntos_dnis):
    """
    Evalúa las expresiones lógicas definidas en la Parte 1 basadas en los DNIs.
    """
    print("\n--- Evaluación de Condiciones Lógicas (basado en DNIs) ---")

    # Expresión Lógica 1: "Si el dígito 0 está presente en alguno de los conjuntos de DNI..."
    d_cero_presente = False
    for i, conjunto in enumerate(conjuntos_dnis):
        if 0 in conjunto:
            d_cero_presente = True
            print(f"  El dígito 0 está presente en el Conjunto del Alumno {i+1}.")
            break

    if d_cero_presente:
        print("Resultado: Se considera un 'grupo con cero'.")
    else:
        print("Resultado: Ningún DNI contiene el dígito 0.")

    # Expresión Lógica 2: "Si la intersección de los conjuntos de DNI tiene exactamente dos elementos..."
    if len(conjuntos_dnis) >= 2:
        # Calculamos la intersección de todos los conjuntos
        interseccion_total = conjuntos_dnis[0]
        for i in range(1, len(conjuntos_dnis)):
            interseccion_total = interseccion_total.intersection(conjuntos_dnis[i])
        
        if len(interseccion_total) == 2:
            print(f"  La intersección de los conjuntos tiene exactamente 2 elementos ({interseccion_total}).")
            print("Resultado: Hay una 'coincidencia numérica limitada'.")
        else:
            print(f"  La intersección de los conjuntos tiene {len(interseccion_total)} elementos.")
            print("Resultado: No hay una 'coincidencia numérica limitada' (la intersección no tiene exactamente 2 elementos).")
    else:
        print("No hay suficientes conjuntos para evaluar la intersección de todos los DNIs.")


# --- Operaciones con años de nacimiento --- 

def obtener_anios_nacimiento():
    """
    Solicita o utiliza los años de nacimiento de los integrantes del grupo
    y los devuelve como una lista de enteros.
    """
    anios = []
    anios.append(2001) # Año de nacimiento del Alumno 1
    anios.append(2005) # Año de nacimiento del Alumno 2
    return anios

def es_bisiesto(year):
    """
    Determina si un año es bisiesto.
    Un año es bisiesto si es divisible por 4,
    excepto si es divisible por 100,
    pero si es divisible por 400, sí es bisiesto.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def analizar_anios_nacimiento(anios_nacimiento):
    """
    Realiza el conteo de años pares/impares y evalúa condiciones como 'Grupo Z' y 'Año especial'.
    """
    print("\n--- Análisis de Años de Nacimiento ---")

    pares = 0
    impares = 0
    nacidos_despues_2000 = True 
    algun_bisiesto = False
    
    for anio in anios_nacimiento:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        if anio <= 2000: 
            nacidos_despues_2000 = False
        
        if es_bisiesto(anio):
            algun_bisiesto = True
            print(f"  El año {anio} es bisiesto.")

    print(f"Cantidad de años pares: {pares}")
    print(f"Cantidad de años impares: {impares}")

    if nacidos_despues_2000:
        print("Resultado: 'Grupo Z' (todos nacieron después del 2000).")
    else:
        print("Resultado: No es 'Grupo Z' (alguno nació en el 2000 o antes).")
    
    if algun_bisiesto:
        print("Resultado: 'Tenemos un año especial' (alguno nació en año bisiesto).")
    else:
        print("Resultado: Ninguno nació en año bisiesto.")

def calcular_producto_cartesiano(conjunto_anios, conjunto_edades):
    """
    Calcula y muestra el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.
    """
    print("\n--- Producto Cartesiano (Años x Edades Actuales) ---")
    producto = set()
    for anio in conjunto_anios:
        for edad in conjunto_edades:
            producto.add((anio, edad)) 
    
    print(f"Conjunto de Años: {conjunto_anios}")
    print(f"Conjunto de Edades Actuales: {conjunto_edades}")
    print(f"Producto Cartesiano: {producto}")
    return producto


# --- Función principal para ejecutar el programa ---
def main():
    print("--- Programa de Análisis de DNIs y Años de Nacimiento ---")

    # --- A. Operaciones con DNIs ---
    print("\n##### INICIO DE ANÁLISIS DE DNIs #####")
    dnis_str = obtener_dnis()
    conjuntos_dnis = generar_conjuntos_dnis(dnis_str)

    print("\n--- Conjuntos de Dígitos Únicos generados ---")
    for i, conjunto in enumerate(conjuntos_dnis):
        print(f"Conjunto Alumno {i+1}: {conjunto}")

    # Realizar y mostrar operaciones de conjuntos (entre los dos alumnos)
    if len(conjuntos_dnis) == 2:
        realizar_operaciones_conjuntos(conjuntos_dnis[0], conjuntos_dnis[1])
    elif len(conjuntos_dnis) > 2:
        print("\nNota: Se realizarán operaciones solo entre los dos primeros conjuntos para este ejemplo.")
        realizar_operaciones_conjuntos(conjuntos_dnis[0], conjuntos_dnis[1])
    else:
        print("\nNo hay suficientes DNIs para realizar operaciones de conjuntos entre pares.")
    
    # Conteo de frecuencia y suma de dígitos por cada DNI
    for i, dni in enumerate(dnis_str):
        contar_frecuencia_digitos(dni)
        sumar_digitos_dni(dni)
    
    # Evaluación de condiciones lógicas basadas en DNIs
    evaluar_condiciones_logicas_dnis(conjuntos_dnis)
    print("\n##### FIN DE ANÁLISIS DE DNIs #####")

    # --- B. Operaciones con años de nacimiento ---
    print("\n##### INICIO DE ANÁLISIS DE AÑOS DE NACIMIENTO #####")
    anios_nacimiento = obtener_anios_nacimiento()
    analizar_anios_nacimiento(anios_nacimiento)

    # Para el producto cartesiano, necesitamos un conjunto de años y uno de edades.
    # Usaremos los años de nacimiento como un conjunto, y calcularemos las edades aproximadas.
    conjunto_anios_nac = set(anios_nacimiento)
    
    # Calcular edades actuales aproximadas
    current_year = datetime.datetime.now().year # Obtiene el año actual del sistema
    edades_actuales = set()
    for anio in anios_nacimiento:
        edad = current_year - anio
        edades_actuales.add(edad)
    
    calcular_producto_cartesiano(conjunto_anios_nac, edades_actuales)
    print("\n##### FIN DE ANÁLISIS DE AÑOS DE NACIMIENTO #####")

# Esto asegura que main() se ejecute solo cuando el script se corre directamente.
if __name__ == "__main__":
    main()