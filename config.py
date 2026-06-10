# Configuración de la Aplicación
# ==============================

# URL del Google Sheets del Laboratorio SIRIO
# Cambia este URL si necesitas usar un Google Sheets diferente
URL_SHEETS_SIRIO = "https://docs.google.com/spreadsheets/d/19kraxB-cEyacrZZa9wFQXcD8cJkweV0aua_k7g7SzvA/edit?usp=sharing"

# Configuración de la página
PAGE_TITLE = "Análisis Laboratorio Microbiología Veterinaria"
PAGE_ICON = "🧬"
PAGE_LAYOUT = "wide"

# Configuración de caché (en segundos)
CACHE_TTL = 300  # 5 minutos

# ================== MAPEO DE COLUMNAS ==================
# Mapea los nombres de columnas de Google Sheets a nombres internos
# Cambia estos valores si tu Google Sheets tiene nombres diferentes
COLUMN_MAPPING = {
    "cliente": "CV 1",           # Columna que identifica al cliente
    "examen": "EXÁMENES",        # Columna que tiene los exámenes solicitados
    "especie": "ESPECIE",        # Especie del animal
    "fecha": "FECHA",            # Fecha del examen
    "resultado": None            # None = no existe. Cambiar a "nombre_columna" si existe
}

# Colores predefinidos
COLOR_SCALE_EXAMS = "Blues"
COLOR_SCALE_SPECIES = "Viridis"
COLOR_SCALE_MATRIX = "YlOrRd"

# Configuración de visualización
CHART_HEIGHT = 400
CHART_FONT_SIZE = 12
