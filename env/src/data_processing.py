import pandas as pd

def load_and_clean_data(filepath):
    # Cargar datos desde archivo CSV
    data = pd.read_csv(filepath)
    
    # Limpiar datos (rellenar valores nulos, eliminar duplicados, etc.)
    data.fillna(0, inplace=True)  # Llenar valores nulos con 0
    data.drop_duplicates(inplace=True)  # Eliminar duplicados
    
    # Imprimir resumen de datos
    print(data.info())
    return data
