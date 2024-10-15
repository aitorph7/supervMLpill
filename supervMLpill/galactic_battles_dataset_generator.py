import pandas as pd
import numpy as np

# Definir el número de entradas
num_entries = 250
num_entries_per_class = num_entries // 2

# Genero datos aleatorios para cada variable
rng = np.random.default_rng(seed=42)

def generate_data(num_entries, survival_value):
    # Daño sufrido por la nave: medido en una escala de 0 a 9
    damage = rng.integers(0, 10, num_entries)

    # Tamaño de la nave: pequeña = 0, mediana = 1, grande = 2
    ship_size = rng.choice([0, 1, 2], num_entries)

    # Escudos: deflectores de energía que posee la nave: 0, 1 (navegación), 2 (combate)
    shields = rng.choice([0, 1, 2], num_entries)

    # Tripulación: número de tripulantes a bordo de la nave
    crew = rng.integers(10, 1000, num_entries)

    # Experiencia del Capitán: medida en años de servicio
    captain_experience = rng.integers(0, 40, num_entries)

    # Número de Enemigos: cantidad de naves enemigas en la batalla
    num_enemies = rng.integers(1, 20, num_entries)

    # Tipo de nave enemiga: caza = 0, acorazado = 1, corbeta = 2, destructor = 3, nave insignia = 4
    enemy_type = rng.choice([0, 1, 2, 3, 4], num_entries)

    # Duración de la batalla: medida en microciclos (análogos a décimas de segundo)
    battle_duration = rng.integers(1, 10000, num_entries)

    # Sistema estelar donde ocurre la batalla: apoyo aliado remoto = 0, apoyo aliado próximo = 1
    star_system = rng.choice([0, 1], num_entries)

    # Supervivencia: si la tripulación sobrevivió (1) o no (0)
    survival = [survival_value] * num_entries

    return {
        'Daño': damage,
        'Tamaño': ship_size,
        'Escudos': shields,
        'Tripulación': crew,
        'Experiencia_Capitan': captain_experience,
        'Num_Enemigos': num_enemies,
        'Tipo_Enemigo': enemy_type,
        'Duración_Batalla': battle_duration,
        'Sistema_Estelar': star_system,
        'Supervivencia': survival
    }

# Genero datos balanceados para cada clase de supervivencia
data_survived = generate_data(num_entries_per_class, 1)
data_not_survived = generate_data(num_entries_per_class, 0)

# Combino los datos en un solo DataFrame
data_combined = {key: np.concatenate([data_survived[key], data_not_survived[key]]) for key in data_survived}
df = pd.DataFrame(data_combined)
df.to_csv('supervMLpill/galactic_battles_dataset.csv', index=False)

print("Archivo 'galactic_battles_dataset.csv' generado con éxito.")