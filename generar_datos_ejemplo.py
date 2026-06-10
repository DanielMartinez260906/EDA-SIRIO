"""
Script para generar datos de ejemplo en CSV
Útil para entender el formato requerido
"""

import pandas as pd
from datetime import datetime, timedelta

# Crear datos de ejemplo realistas para un laboratorio de microbiología veterinaria
datos = {
    'Cliente': [
        'Clínica San José', 'Veterinaria La Paz', 'Clínica San José',
        'Veterinaria Rural', 'Clínica San José', 'Veterinaria La Paz',
        'Veterinaria Rural', 'Clínica Moderna', 'Clínica San José',
        'Veterinaria La Paz', 'Clínica Moderna', 'Veterinaria Rural',
        'Clínica San José', 'Veterinaria La Paz', 'Clínica Moderna',
        'Veterinaria Rural', 'Clínica San José', 'Veterinaria La Paz',
        'Clínica Moderna', 'Veterinaria Rural', 'Clínica San José',
        'Veterinaria La Paz', 'Veterinaria Rural', 'Clínica Moderna',
        'Clínica San José', 'Veterinaria Rural', 'Clínica Moderna',
        'Veterinaria La Paz', 'Clínica San José', 'Veterinaria Rural',
    ],
    'Especie': [
        'Perro', 'Gato', 'Perro', 'Bovino', 'Gato', 'Perro',
        'Bovino', 'Equino', 'Perro', 'Gato', 'Equino', 'Bovino',
        'Perro', 'Gato', 'Bovino', 'Equino', 'Perro', 'Perro',
        'Equino', 'Bovino', 'Perro', 'Gato', 'Bovino', 'Equino',
        'Gato', 'Bovino', 'Equino', 'Perro', 'Perro', 'Bovino',
    ],
    'Examen': [
        'Cultivo Bacteriano', 'Antibiograma', 'Cultivo Bacteriano',
        'Cultivo Bacteriano', 'Coprocultivo', 'Antibiograma',
        'Cultivo Bacteriano', 'Cultivo Bacteriano', 'Análisis Fecal',
        'Coprocultivo', 'Cultivo Bacteriano', 'Análisis Fecal',
        'Cultivo Bacteriano', 'Antibiograma', 'Cultivo Bacteriano',
        'Cultivo Fúngico', 'Análisis Fecal', 'Cultivo Bacteriano',
        'Cultivo Bacteriano', 'Análisis Fecal', 'Cultivo Bacteriano',
        'Coprocultivo', 'Cultivo Fúngico', 'Análisis Fecal',
        'Antibiograma', 'Cultivo Bacteriano', 'Cultivo Fúngico',
        'Análisis Fecal', 'Cultivo Bacteriano', 'Antibiograma',
    ],
    'Fecha': [
        '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19',
        '2024-01-20', '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24',
        '2024-01-25', '2024-01-26', '2024-01-27', '2024-01-28', '2024-01-29',
        '2024-01-30', '2024-01-31', '2024-02-01', '2024-02-02', '2024-02-03',
        '2024-02-04', '2024-02-05', '2024-02-06', '2024-02-07', '2024-02-08',
        '2024-02-09', '2024-02-10', '2024-02-11', '2024-02-12', '2024-02-13',
    ],
    'Resultado': [
        'Positivo', 'Sensible', 'Positivo', 'Positivo', 'Negativo',
        'Sensible', 'Positivo', 'Positivo', 'Positivo', 'Negativo',
        'Positivo', 'Negativo', 'Positivo', 'Resistente', 'Positivo',
        'Positivo', 'Negativo', 'Positivo', 'Positivo', 'Negativo',
        'Positivo', 'Negativo', 'Positivo', 'Negativo', 'Sensible',
        'Positivo', 'Positivo', 'Positivo', 'Positivo', 'Sensible',
    ]
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Guardar en CSV
archivo_salida = 'datos_ejemplo.csv'
df.to_csv(archivo_salida, index=False)

print("✅ Archivo creado exitosamente: datos_ejemplo.csv")
print(f"\nPreview de los datos:")
print(df.head(10))
print(f"\nTotal de registros: {len(df)}")
print(f"\nExámenes por frecuencia:")
print(df['Examen'].value_counts())
