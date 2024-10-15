import pandas as pd
import numpy as np
rng = np.random.default_rng(42)

# Definir constantes y listas de valores posibles
n_ships = 200
especies = {
    'Federacion': 0, 'Klingon': 1, 'Romulano': 2, 'Borg': 3, 'Vulcano': 4,
    'Andoriano': 5, 'Llyriano': 6, 'Ba`ul': 7, 'Ferengi': 8, 'Gorn': 9, 'Xindi': 10
}
escudos = ['Navegación', 'Combate', 'Sin escudos']
especies_amistosas = [0, 4, 5, 8]  # Federación, Vulcano, Andoriano, Ferengi

# Función para generar datos realistas y correlacionados
def generar_nave():
    origen = rng.choice(list(especies.values()))
    
    # La velocidad Warp depende del origen
    warp_base = {
        3: 9, 0: 8, 4: 7, 2: 7, 1: 7,
        10: 6, 5: 6, 6: 5, 7: 5, 8: 5, 9: 4
    }
    velocidad_warp = np.clip(rng.normal(warp_base[origen], 0.5), 1, 10)
    
    # La potencia del phaser depende del origen y si es amistosa
    amistosa = 1 if origen in especies_amistosas else 0
    potencia_base = 500 if amistosa else 800
    potencia_phaser = np.clip(rng.normal(potencia_base, 100), 100, 1000)
    
    # El número de tripulantes depende del origen
    tripulantes_base = {
        3: 5000, 0: 1000, 4: 400, 2: 800, 1: 600,
        10: 300, 5: 200, 6: 150, 7: 100, 8: 50, 9: 30
    }
    tripulantes = int(np.clip(rng.normal(tripulantes_base[origen], tripulantes_base[origen]*0.1), 10, 10000))
    
    # La capacidad de carga depende del número de tripulantes
    capacidad_carga = int(np.clip(tripulantes * rng.normal(2, 0.5), 20, 20000))
    
    # Los escudos dependen del origen
    if origen in [3, 1, 2]:  # Borg, Klingon, Romulano
        escudo = 2  # Combate
    elif origen in [0, 4, 5]:  # Federación, Vulcano, Andoriano
        escudo = rng.choice([1, 2, 0], p=[0.4, 0.4, 0.2])
    else:
        escudo = rng.choice([1, 0, 2], p=[0.4, 0.2, 0.4])

    # La tecnología de camuflaje depende del origen
    camuflaje_prob = {
        2: 0.9, 1: 0.7, 0: 0.3, 3: 0.1,
        4: 0.2, 5: 0.2, 6: 0.4, 7: 0.5,
        8: 0.3, 9: 0.2, 10: 0.4
    }
    camuflaje = 1 if rng.random() < camuflaje_prob[origen] else 0
    
    return [velocidad_warp, potencia_phaser, tripulantes, capacidad_carga, escudo, camuflaje, origen, amistosa]

# Generar el dataset
datos = [generar_nave() for _ in range(n_ships)]

# Crear el DataFrame
df = pd.DataFrame(datos, columns=[
    'Velocidad_Warp', 'Potencia_Phaser', 'Tripulantes', 'Capacidad_Carga',
    'Escudos', 'Camuflaje', 'Origen', 'Amistosa'
])

# Redondear valores numéricos
df['Velocidad_Warp'] = df['Velocidad_Warp'].round(2)
df['Potencia_Phaser'] = df['Potencia_Phaser'].round(2)

# Guardar como CSV
df.to_csv('supervMLpill/complex_starship_dataset.csv', index=False)

# Mostrar algunas estadísticas básicas
print("Resumen del dataset:")
print(f"Número total de naves: {len(df)}")
print("\nDistribución por origen:")
print(df['Origen'].value_counts())
print("\nDistribución por tipo de escudos:")
print(df['Escudos'].value_counts())
print("\nEstadísticas de variables numéricas:")
print(df.describe())