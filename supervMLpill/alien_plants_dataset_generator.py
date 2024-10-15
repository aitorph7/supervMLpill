import pandas as pd
import numpy as np
rng = np.random.default_rng(42)

n_plants = 200

# Función para generar datos de plantas realistas y correlacionados
def generar_planta():
    # Hábitat: 0 = desierto, 1 = bosque, 2 = pantano, 3 = montaña
    habitat = rng.integers(0, 4)
    
    # Altura basada en hábitat
    altura_media = {0: 50, 1: 300, 2: 150, 3: 30}
    altura = np.clip(rng.normal(altura_media[habitat], altura_media[habitat]*0.2), 5, 500)
    
    # Humedad basada en hábitat
    humedad_media = {0: 15, 1: 60, 2: 85, 3: 30}
    humedad = np.clip(rng.normal(humedad_media[habitat], 10), 5, 95)
    
    # Hojas y flores basadas en hábitat
    prob_hojas = {0: 0.3, 1: 0.9, 2: 0.8, 3: 0.6}
    prob_flores = {0: 0.2, 1: 0.7, 2: 0.6, 3: 0.4}
    hojas = 1 if rng.random() < prob_hojas[habitat] else 0
    flores = 1 if rng.random() < prob_flores[habitat] else 0
    
    # Macronutrientes inversamente correlacionados con toxinas
    toxinas = np.clip(rng.normal(50, 20), 0, 100)
    macronutrientes = np.clip(rng.normal(100 - toxinas*0.5, 20), 0, 100)
    
    # Clase basada en toxinas y macronutrientes
    # 0 = comestible segura, 1 = parcialmente venenosa, 
    # 2 = no comestible venenosa, 3 = propiedades medicinales
    if toxinas < 20 and macronutrientes > 60:
        clase = 0
    elif toxinas > 80:
        clase = 2
    elif toxinas > 40:
        clase = 1
    else:
        clase = 3 if rng.random() < 0.4 else 0
    
    return [altura, macronutrientes, toxinas, humedad, hojas, flores, habitat, clase]

# Generar el dataset
datos = [generar_planta() for _ in range(n_plants)]

# Crear el DataFrame
columnas = [
    'Altura_cm', 'Macronutrientes_g', 'Toxinas_ug_g', 'Humedad_Porcentaje',
    'Hojas', 'Flores', 'Habitat', 'Clase'
]
df = pd.DataFrame(datos, columns=columnas)

# Redondear valores numéricos
df = df.round(2)

# Guardar como CSV
df.to_csv('supervMLpill/alien_plants_dataset.csv', index=False)

# Mostrar algunas estadísticas básicas
print("Resumen del dataset:")
print(f"Número total de plantas: {len(df)}")
print("\nDistribución por hábitat:")
habitat_nombres = {0: 'Desierto', 1: 'Bosque', 2: 'Pantano', 3: 'Montaña'}
print(df['Habitat'].map(habitat_nombres).value_counts())
print("\nDistribución por clase:")
clase_nombres = {0: 'Comestible segura', 1: 'Parcialmente venenosa', 
                2: 'No comestible venenosa', 3: 'Propiedades medicinales'}
print(df['Clase'].map(clase_nombres).value_counts())
print("\nEstadísticas de variables numéricas:")
print(df.describe())