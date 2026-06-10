# 🧬 ANÁLISIS EXPLORATORIO DE DATOS - LABORATORIO DE MICROBIOLOGÍA VETERINARIA

## 📦 Archivos Generados

### 🚀 Para Ejecutar la Aplicación

| Archivo | Descripción | Acción |
|---------|-------------|--------|
| **instalar.bat** | Script de instalación automática | ✅ **Haz doble clic primero** |
| **ejecutar.bat** | Inicia la aplicación | ✅ **Haz doble clic después** |
| **app.py** | Código principal de la aplicación | ⚠️ No toques (a menos que quieras personalizar) |

### 📚 Para Aprender a Usar

| Archivo | Descripción | Cuándo Leerlo |
|---------|-------------|---------------|
| **INICIO_RAPIDO.md** | Guía de primeros pasos (3 pasos) | 👈 **COMIENZA AQUÍ** |
| **GUIA_COMPLETA.md** | Documentación completa con ejemplos | Si necesitas más detalles |
| **README.md** | Información técnica y requisitos | Si tienes problemas técnicos |
| **CONFIGURACION_GOOGLE_SHEETS.md** | Cómo conectar Google Sheets | Si usarás tus propios datos |

### ⚙️ Configuración y Datos

| Archivo | Descripción | Uso |
|---------|-------------|-----|
| **requirements.txt** | Lista de dependencias Python | ✅ Se usa automáticamente |
| **generar_datos_ejemplo.py** | Script para generar datos de ejemplo | Opcional - para crear más datos |

---

## 🎯 Cómo Empezar (Lo Más Importante)

### ✅ Paso 1: Instalar
```bash
Haz doble clic en: instalar.bat
```
Espera a que termine y presiona cualquier tecla.

### ✅ Paso 2: Ejecutar
```bash
Haz doble clic en: ejecutar.bat
```
Se abrirá automáticamente en tu navegador.

### ✅ Paso 3: Usar
En la aplicación:
- Selecciona **"📁 Cargar datos de ejemplo"** para probar
- O conecta tu **Google Sheets** siguiendo las instrucciones

---

## 🎨 Funcionalidades Principales

```
┌─────────────────────────────────────────────────────┐
│  📊 ANÁLISIS EXPLORATORIO DE DATOS                  │
├─────────────────────────────────────────────────────┤
│                                                       │
│  📈 1. Exámenes Ordenados (MÁS a MENOS común)      │
│  👥 2. Análisis por Cliente (con desplegable)       │
│  🐾 3. Análisis por Especie (con desplegable)       │
│  🔗 4. Matriz Clientes vs Exámenes                  │
│  📅 5. Análisis Temporal y Resultados               │
│  📊 6. Resumen Estadístico General                  │
│  💾 7. Descargar en CSV o Excel                     │
│                                                       │
└─────────────────────────────────────────────────────┘
```

---

## 🧬 Estructura de Datos Requerida

Tu Google Sheets debe tener estas columnas:

```
┌──────────────┬─────────┬─────────────────┬───────────┬──────────┐
│   Cliente    │ Especie │     Examen      │   Fecha   │ Resultado│
├──────────────┼─────────┼─────────────────┼───────────┼──────────┤
│Clínica A     │ Perro   │Cultivo Bact.    │2024-01-15 │Positivo  │
│Clínica B     │ Gato    │Antibiograma     │2024-01-16 │Sensible  │
│Veterinaria X │ Bovino  │Coprocultivo     │2024-01-17 │Negativo  │
└──────────────┴─────────┴─────────────────┴───────────┴──────────┘
```

---

## 📊 Visualizaciones Disponibles

### 📈 Exámenes (Principal)
- **Gráfico de barras** con exámenes ordenados
- **De MÁS a MENOS común**
- Datos actualizables en tiempo real

### 👥 Clientes
- **Desplegable** para filtrar
- **Gráfico de pastel** con distribución
- **Métricas** de exámenes por cliente

### 🐾 Especies
- **Desplegable** para filtrar
- **Gráfico de barras** ordenado
- **Exámenes específicos** por animal

### 🔗 Matriz
- **Tabla cruzada** de clientes vs exámenes
- **Heatmap colorido** para visualizar patrones
- Identifica especialidades

### 📅 Temporal
- **Gráfico de línea** con tendencia
- **Distribución de resultados**
- Análisis de positividad

---

## 🔄 Flujo de Uso

```
1. INSTALAR
   ↓
   instalar.bat
   ↓
   Esperar a que termine
   ↓
2. EJECUTAR
   ↓
   ejecutar.bat
   ↓
   Se abre navegador automáticamente
   ↓
3. ELEGIR DATOS
   ↓
   ├─ Opción A: "Datos de ejemplo" (para probar)
   │  ↓
   │  ¡A explorar!
   │
   └─ Opción B: "Google Sheets" (tus datos)
      ↓
      Pegar URL de Google Sheets
      ↓
      ¡A explorar!
   ↓
4. EXPLORAR
   ↓
   Usar desplegables
   Analizar gráficos
   Ver métricas
   ↓
5. DESCARGAR (Opcional)
   ↓
   Botón "Descargar en CSV/Excel"
   ↓
   Guardar en tu computadora
```

---

## ❓ Preguntas Frecuentes Rápidas

### ¿Por dónde comienzo?
→ Lee **INICIO_RAPIDO.md** (5 minutos)

### ¿Cómo conecto Google Sheets?
→ Lee **CONFIGURACION_GOOGLE_SHEETS.md**

### ¿Qué hago si hay un error?
→ Lee **README.md** - Sección "Solución de Problemas"

### ¿Cómo personalizo los datos?
→ Lee **GUIA_COMPLETA.md** - Sección "Personalización"

### ¿Puedo usar esto sin Google Sheets?
→ Sí, hay datos de ejemplo incluidos

---

## 🎯 Objetivos Alcanzados

✅ **Análisis visual** de datos
✅ **Exámenes ordenados** de más a menos común  
✅ **Interfaz interactiva** con desplegables
✅ **Múltiples visualizaciones** (gráficos, tablas, heatmaps)
✅ **Conexión con Google Sheets**
✅ **Exportación de datos** en CSV y Excel
✅ **Datos de ejemplo** incluidos
✅ **Documentación completa** en español

---

## 📈 Tecnología Utilizada

- **Python** - Lenguaje de programación
- **Streamlit** - Framework para interfaces interactivas
- **Pandas** - Análisis y procesamiento de datos
- **Plotly** - Visualizaciones interactivas
- **Google Sheets API** - Conexión con hojas de cálculo

---

## 🚦 Estado de la Aplicación

| Componente | Estado | Detalles |
|-----------|--------|----------|
| Instalación | ✅ Listo | Automática con instalar.bat |
| Interfaz | ✅ Listo | Streamlit - moderna y responsive |
| Análisis | ✅ Listo | 7 secciones de análisis |
| Google Sheets | ✅ Listo | Conexión automática |
| Documentación | ✅ Completa | Guías en español |

---

## 💡 Próximos Pasos

1. **Inmediato:** Haz doble clic en `instalar.bat`
2. **Luego:** Haz doble clic en `ejecutar.bat`
3. **Después:** Prueba con datos de ejemplo
4. **Finalmente:** Conecta tu Google Sheets

---

## 📞 Información Técnica

- **Versión de Python:** 3.8 o superior
- **Sistema Operativo:** Windows 10+
- **Navegador:** Chrome, Edge, Firefox
- **Puerto:** 8501 (local)
- **Conexión:** Internet (para Google Sheets)

---

## 📄 Archivos de Documentación

```
📁 ANALISIS EXPLORATORIO DE DATOS SIRIO/
├── 🚀 app.py                          (Aplicación principal)
├── 📋 instalar.bat                    (Instalación)
├── 🎬 ejecutar.bat                    (Ejecutar)
│
├── 📚 INICIO_RAPIDO.md                (START HERE!)
├── 📚 GUIA_COMPLETA.md                (Todo detallado)
├── 📚 README.md                       (Información técnica)
├── 📚 CONFIGURACION_GOOGLE_SHEETS.md  (Configuración)
│
├── ⚙️  requirements.txt               (Dependencias)
├── 🔨 generar_datos_ejemplo.py       (Generador de datos)
│
└── 📄 ARCHIVOS.md                    (Este archivo)
```

---

## ✨ Características Destacadas

🌟 **Desplegables dinámicos** - Filtra por cliente y especie fácilmente
🌟 **Exámenes ordenados** - Ve de inmediato cuál es el más común
🌟 **Visualizaciones interactivas** - Zoom, hover, descarga de gráficos
🌟 **Matriz visual** - Entiende patrones con heatmaps
🌟 **Análisis temporal** - Detecta tendencias
🌟 **Exportación** - Descarga en CSV o Excel
🌟 **Documentación completa** - Todo en español
🌟 **Datos de ejemplo** - Prueba sin necesidad de datos propios

---

## 🎉 ¡Listo Para Usar!

**Tu análisis exploratorio de datos está completamente configurado.**

### Ahora:
1. Haz doble clic en `instalar.bat`
2. Haz doble clic en `ejecutar.bat`
3. ¡Explora tus datos! 🚀

---

**Desarrollado para Laboratorio de Microbiología Veterinaria 🧬**

*Última actualización: Junio 2024*
