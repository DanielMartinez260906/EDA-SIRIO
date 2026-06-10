# 🧬 Guía Completa de Uso

## 📚 Tabla de Contenidos
1. [Instalación Detallada](#instalación-detallada)
2. [Primeros Pasos](#primeros-pasos)
3. [Funcionalidades](#funcionalidades)
4. [Ejemplos de Uso](#ejemplos-de-uso)
5. [Personalización](#personalización)
6. [Solución de Problemas](#solución-de-problemas)

---

## Instalación Detallada

### Requisitos Previos
- Windows 10 o superior
- Conexión a Internet
- Navegador web (Chrome, Edge, Firefox)

### Pasos

#### 1. Descargar Python (si no lo tienes)
- Visita: https://www.python.org/downloads/
- Descarga Python 3.9 o superior
- **IMPORTANTE**: Marca la opción "Add Python to PATH"
- Instala normalmente

#### 2. Verificar Instalación
Abre PowerShell o CMD y escribe:
```bash
python --version
```
Debería mostrar: `Python 3.x.x`

#### 3. Instalar Dependencias
En la carpeta del proyecto, haz doble clic en `instalar.bat`

O manualmente en PowerShell:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## Primeros Pasos

### Inicio Rápido (3 pasos)

1. **Instalar** → Haz doble clic en `instalar.bat`
2. **Ejecutar** → Haz doble clic en `ejecutar.bat`
3. **Usar** → Selecciona "📁 Cargar datos de ejemplo"

### Con tu Google Sheets

1. **Preparar datos:**
   - Abre Google Sheets
   - Crea columnas: Cliente, Especie, Examen, Fecha, Resultado

2. **Compartir:**
   - Haz clic en "Compartir"
   - Selecciona "Cualquiera con el enlace"
   - Copia la URL

3. **Conectar en la app:**
   - Selecciona "📊 Usar Google Sheets"
   - Pega la URL
   - ¡Listo!

---

## Funcionalidades

### 📊 1. Análisis de Exámenes

**Muestra:**
- Todos los exámenes ordenados de MÁS a MENOS común
- Gráfico interactivo de barras
- Tabla con conteos

**Interacción:**
- Pasar mouse sobre las barras para ver valores exactos
- Hacer zoom en el gráfico
- Descargar como PNG

**Información que obtienes:**
- Cuál es el examen más solicitado
- Cuál es el menos solicitado
- Distribución general de exámenes

---

### 👥 2. Análisis de Clientes

**Muestra:**
- Desplegable para seleccionar cliente
- Métricas del cliente seleccionado
- Gráfico de pastel con sus exámenes
- Tabla con detalle

**Cómo usarlo:**
1. Selecciona un cliente del desplegable
2. Observa las métricas (total exámenes, especies, tipos)
3. Ve el gráfico de pastel
4. Revisa la tabla de detalle

**Información que obtienes:**
- Exámenes más solicitados por cliente
- Especies que atiende
- Volumen de trabajo por cliente
- Distribución de tipos de examen

---

### 🐾 3. Análisis por Especie

**Muestra:**
- Desplegable para seleccionar especie
- Métricas de la especie
- Gráfico de exámenes para esa especie
- Tabla con detalle

**Cómo usarlo:**
1. Selecciona una especie (Perro, Gato, Bovino, etc.)
2. Observa las métricas
3. Ve qué exámenes son comunes para esa especie
4. Identifica qué clientes atienden esa especie

**Información que obtienes:**
- Exámenes más comunes por especie
- Clientes que atienden esa especie
- Volumen de trabajo por especie

---

### 🔗 4. Matriz Clientes vs Exámenes

**Muestra:**
- Tabla cruzada (crosstab)
- Heatmap visual

**Cómo usarlo:**
1. Observa la tabla - filas son clientes, columnas son exámenes
2. Los números muestran cuántas veces cada cliente solicita cada examen
3. El heatmap usa colores - rojo = más solicitudes, amarillo = menos

**Información que obtienes:**
- Qué cliente solicita qué examen
- Clientes especializados vs generales
- Patrones de solicitud

---

### 📅 5. Análisis Temporal

**Muestra dos gráficos:**

#### a) Distribución de Resultados
- Gráfico de barras con colores
- Cuántos exámenes Positivos, Negativos, etc.

#### b) Tendencia en el Tiempo
- Gráfico de línea
- Cuántos exámenes se solicitan cada semana

**Información que obtienes:**
- Porcentaje de positivos
- Tendencias estacionales
- Períodos picos de trabajo

---

### 📈 6. Resumen Estadístico

Muestra métricas generales:
- Total de registros
- Total de clientes únicos
- Total de especies
- Total de tipos de examen
- Exámenes positivos
- Porcentaje de positividad

---

### 💾 7. Descargar Datos

**Opciones:**
1. **CSV** - Abre en Excel, importa a bases de datos
2. **Excel** - Descarga formato .xlsx

**Qué contiene:**
- Todos tus datos procesados y listos

---

## Ejemplos de Uso

### Ejemplo 1: "¿Cuál es mi examen más solicitado?"
1. Ve a la sección "📊 1. Análisis de Exámenes"
2. Observa la primera barra del gráfico
3. Lee el nombre en el eje X
4. Ese es tu examen más solicitado

### Ejemplo 2: "¿Qué tipos de examen solicita la Clínica X?"
1. Ve a "👥 2. Análisis de Clientes"
2. Selecciona la clínica en el desplegable
3. Observa el gráfico de pastel
4. Cada porción es un tipo de examen

### Ejemplo 3: "¿Qué exámenes son más comunes para perros?"
1. Ve a "🐾 3. Análisis por Especie"
2. Selecciona "Perro" en el desplegable
3. Observa el gráfico de barras
4. Los ordenados de mayor a menor son tus respuesta

### Ejemplo 4: "¿Cuál es mi porcentaje de positividad?"
1. Ve a "📅 5. Análisis Temporal"
2. Mira "Distribución de Resultados"
3. Busca el porcentaje de "Positivo"

### Ejemplo 5: "¿Mi volumen de exámenes está creciendo?"
1. Ve a "📅 5. Análisis Temporal"
2. Mira "Tendencia en el Tiempo"
3. Si la línea sube → crece
4. Si la línea baja → disminuye

---

## Personalización

### Cambiar Datos
**Opción 1 - Google Sheets:**
- Edita directamente tu Google Sheets
- Recarga la aplicación (F5)

**Opción 2 - CSV Local:**
- Guarda un CSV con tus datos
- Modifica `app.py` para usar ese archivo

### Agregar Más Columnas
Para agregar columnas adicionales:
1. Abre `app.py` con un editor de texto
2. Busca: `'Cliente', 'Especie', 'Examen', 'Fecha', 'Resultado'`
3. Agrega tus columnas
4. Guarda y reinicia la app

### Cambiar Colores
En `app.py`, busca `color_continuous_scale` y cambia:
- 'Blues' → paleta azul
- 'Reds' → paleta roja
- 'Viridis' → paleta verde/violeta
- 'YlOrRd' → amarillo-naranja-rojo

---

## Solución de Problemas

### Problema: "ModuleNotFoundError: No module named 'streamlit'"
**Solución:**
```bash
pip install -r requirements.txt
```

### Problema: "¿Cómo accedo a Google Sheets públicamente?"
**Solución:**
1. Abre Google Sheets
2. Click en "Compartir"
3. Selecciona "Cambiar"
4. Marca "Cualquiera con el enlace"
5. Copia la URL

### Problema: "La aplicación no carga los datos de Google Sheets"
**Solución:**
- Verifica que la URL sea correcta
- Verifica los nombres de columnas (exactos: Cliente, Especie, Examen, Fecha, Resultado)
- Verifica que las fechas estén en formato YYYY-MM-DD
- Intenta con los datos de ejemplo primero

### Problema: "El gráfico se ve extraño"
**Solución:**
- Verifica que no hay espacios en blanco adicionales en los datos
- Verifica que las fechas sean válidas
- Intenta recargar la página (F5)

### Problema: "La aplicación va muy lenta"
**Solución:**
- Probablemente tienes muchos datos (>10,000 filas)
- Intenta usar un rango menor de fechas
- Filtra datos antes de cargar

### Problema: "¿Cómo actualizó los datos sin reiniciar?"
**Solución:**
- En Google Sheets: Edita y recarga la app (F5)
- En CSV local: Modifica el archivo y recarga (F5)

---

## 🎓 Tips Avanzados

### Tip 1: Filtrar por Rango de Fechas
Para analizar solo un período:
1. Ve a la sección "Ver datos crudos"
2. Observa la tabla
3. Considera solo las filas que te interesan

### Tip 2: Exportar Análisis
1. Descarga los datos en CSV
2. Abre en Excel
3. Crea tus propios análisis adicionales

### Tip 3: Generar Reportes
1. Ve a cada sección
2. Haz screenshot con Herramientas de Captura
3. Combina en PowerPoint o Word

### Tip 4: Compartir Análisis
1. La app corre en `localhost:8501`
2. Para compartir públicamente, usa Streamlit Cloud
3. O convierte a HTML con exportaciones

---

## 📞 Necesitas Más Ayuda

- **Problema técnico:** Revisa "Solución de Problemas"
- **Configuración Google Sheets:** Abre `CONFIGURACION_GOOGLE_SHEETS.md`
- **Inicio rápido:** Abre `INICIO_RAPIDO.md`
- **Documentación completa:** Abre `README.md`

---

## ✅ Checklist de Validación

- [ ] Python está instalado
- [ ] Ejecuté `instalar.bat` sin errores
- [ ] Ejecuté `ejecutar.bat` y se abrió en navegador
- [ ] Pude ver los datos de ejemplo
- [ ] Probé el desplegable de clientes
- [ ] Probé el desplegable de especies
- [ ] Pude ver el gráfico de exámenes ordenados
- [ ] Pude ver la matriz
- [ ] Pude descargar en CSV
- [ ] Pude descargar en Excel

---

**¡Felicidades! Ya sabes usar el análisis exploratorio de datos 🧬**

---

*Documentación versión 1.0*
*Última actualización: 2024*
*Desarrollado para Laboratorio de Microbiología Veterinaria*
