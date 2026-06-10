# 🧬 Análisis Exploratorio de Datos - Laboratorio de Microbiología Veterinaria

## Descripción
Esta aplicación interactiva permite analizar datos de clientes y exámenes de un laboratorio de microbiología veterinaria. Incluye visualizaciones dinámicas, desplegables interactivos y análisis de frecuencia de exámenes.

---

## 🚀 Instalación y Configuración

### 1. Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### 2. Pasos de Instalación

#### Opción A: Instalación Manual

```bash
# Navega a la carpeta del proyecto
cd "c:\Users\mdani\OneDrive\Desktop\ANALISIS EXPLORATORIO DE DATOS SIRIO"

# Instala las dependencias
pip install -r requirements.txt
```

#### Opción B: Instalación con Virtual Environment (Recomendado)

```bash
# Crea un entorno virtual
python -m venv venv

# Activa el entorno virtual
# En Windows:
venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt
```

---

## 📊 Configurar Google Sheets

### Paso 1: Preparar tu Google Sheets

1. **Crea o abre tu Google Sheets** con los datos en este formato:

| Cliente | Especie | Examen | Fecha | Resultado |
|---------|---------|--------|-------|-----------|
| Clínica San José | Perro | Cultivo Bacteriano | 2024-01-15 | Positivo |
| Veterinaria La Paz | Gato | Antibiograma | 2024-01-16 | Sensible |
| ... | ... | ... | ... | ... |

2. **Columnas necesarias:**
   - **Cliente**: Nombre del cliente/clínica
   - **Especie**: Tipo de animal (Perro, Gato, Bovino, etc.)
   - **Examen**: Tipo de examen solicitado
   - **Fecha**: Fecha del examen
   - **Resultado**: Resultado del examen

3. **Comparte el Google Sheets:**
   - Click en "Compartir" (arriba a la derecha)
   - Selecciona "Cambiar" en los permisos
   - Selecciona "Cualquiera con el enlace"
   - Cambia a "Visualizador" (o "Editor")
   - Copia el enlace

### Paso 2: Obtener la URL

La URL debe verse así:
```
https://docs.google.com/spreadsheets/d/1A2B3C4D5E6F7G8H9I0J1K2L3M4N5O6P7Q8R9S0T/edit#gid=0
```

---

## 🎯 Ejecutar la Aplicación

```bash
# Ejecuta la aplicación con Streamlit
streamlit run app.py
```

Esto abrirá automáticamente una ventana en tu navegador en `http://localhost:8501`

---

## 📋 Funcionalidades

### 1. **Análisis de Exámenes** 📊
   - Visualiza todos los exámenes ordenados de mayor a menor frecuencia
   - Gráfico interactivo con barras de colores
   - Tabla con cantidades exactas

### 2. **Análisis de Clientes** 👥
   - Desplegable para seleccionar cualquier cliente
   - Métricas de exámenes solicitados, especies atendidas y tipos de examen
   - Gráfico de pastel con distribución de exámenes del cliente

### 3. **Análisis por Especie** 🐾
   - Desplegable para filtrar por especie animal
   - Estadísticas específicas para cada especie
   - Exámenes más solicitados para cada animal

### 4. **Matriz Interactiva** 🔗
   - Tabla cruzada de clientes vs exámenes
   - Heatmap visual que muestra la relación entre clientes y tipos de examen

### 5. **Análisis Temporal** 📅
   - Gráfico de tendencia a lo largo del tiempo
   - Distribución de resultados (Positivo, Negativo, etc.)

### 6. **Resumen Estadístico** 📈
   - Métricas generales del laboratorio
   - Total de registros, clientes, especies y exámenes
   - Porcentaje de exámenes positivos

### 7. **Descargar Datos** 💾
   - Exporta los datos en formato CSV
   - Exporta los datos en formato Excel

---

## 🎨 Características Interactivas

- ✅ **Desplegables dinámicos** para filtrar por cliente y especie
- ✅ **Gráficos interactivos** con Plotly (puedes hacer zoom, hover, etc.)
- ✅ **Datos de ejemplo** incluidos para pruebas
- ✅ **Conexión directa** a Google Sheets (sin necesidad de descargar manualmente)
- ✅ **Interfaz moderna** y fácil de usar
- ✅ **Descarga de datos** en múltiples formatos

---

## 📌 Notas Importantes

1. **Formato de Columnas:**
   - La fecha debe estar en formato `YYYY-MM-DD` (2024-01-15)
   - Los nombres de columnas deben ser exactos: Cliente, Especie, Examen, Fecha, Resultado

2. **Datos Iniciales:**
   - La aplicación incluye datos de ejemplo para que pruebes todas las funciones
   - Puedes cambiar a Google Sheets en cualquier momento

3. **Rendimiento:**
   - Para hojas con más de 10,000 filas, considera hacer un filtro previo

---

## 🔧 Solución de Problemas

### Error: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Error al conectar con Google Sheets
- Verifica que la URL sea pública o compartida
- Asegúrate que el formato de la URL sea correcto

### La aplicación se ejecuta lentamente
- Esto es normal con muchos datos
- Intenta reducir el rango de datos en la hoja de cálculo

---

## 📧 Contacto y Soporte

Si necesitas ayuda o quieres personalizar la aplicación, contacta al desarrollador.

---

**Desarrollado para Laboratorio de Microbiología Veterinaria 🧬**
"# EDA-SIRIO" 
