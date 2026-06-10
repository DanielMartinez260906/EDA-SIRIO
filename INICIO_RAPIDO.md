# 🚀 GUÍA RÁPIDA - Primeros Pasos

## Paso 1️⃣: Instalación (Primera Vez)

**En Windows:**

1. Abre `PowerShell` o `CMD` en esta carpeta
2. Haz doble clic en el archivo `instalar.bat`
3. Espera a que termine la instalación
4. Presiona cualquier tecla cuando veas el mensaje

---

## Paso 2️⃣: Ejecutar la Aplicación

1. Haz doble clic en el archivo `ejecutar.bat`
2. Espera a que se abra tu navegador
3. Verás la interfaz de la aplicación

---

## Paso 3️⃣: Conectar Google Sheets

### Opción A: Usar Datos de Ejemplo (Recomendado para Probar)

1. En la aplicación, selecciona: **"📁 Cargar datos de ejemplo"**
2. ¡Listo! Ahora puedes explorar todas las funcionalidades

### Opción B: Usar tu Propio Google Sheets

1. Prepara tu Google Sheets con este formato:

| Cliente | Especie | Examen | Fecha | Resultado |
|---------|---------|--------|-------|-----------|
| Tu Clínica | Perro | Cultivo Bacteriano | 2024-01-15 | Positivo |
| ... | ... | ... | ... | ... |

2. **Haz clic en "Compartir"** (arriba a la derecha)
3. Selecciona **"Cambiar"** → **"Cualquiera con el enlace"**
4. Copia la URL completa
5. En la aplicación, selecciona: **"📊 Usar Google Sheets"**
6. **Pega la URL** en el campo de texto
7. ¡Listo! Los datos se cargarán automáticamente

---

## 📊 Explorando los Datos

Una vez cargados los datos, verás:

### 📈 Exámenes (Principal)
- Los exámenes ordenados de **MÁS COMÚN a MENOS COMÚN**
- Gráfico interactivo con barras
- Tabla con números exactos

### 👥 Clientes
- **Desplegable** para seleccionar un cliente
- Información de exámenes de ese cliente
- Gráfico de pastel

### 🐾 Especies
- **Desplegable** para filtrar por animal
- Exámenes más solicitados para esa especie
- Estadísticas específicas

### 🔗 Matriz
- Relación entre clientes y tipos de examen
- Heatmap visual

### 📅 Temporal
- Gráfico de tendencia en el tiempo
- Distribución de resultados

### 💾 Descargar
- Exporta los datos en **CSV** o **Excel**

---

## ⚙️ Opciones Interactivas

### Desplegables Disponibles

#### 1️⃣ Selecciona un Cliente
```
Clínica San José
Veterinaria La Paz
Clínica Moderna
... (y más)
```

#### 2️⃣ Selecciona una Especie
```
Perro
Gato
Bovino
Equino
... (y más)
```

---

## 🎨 Interacción con Gráficos

- **Pasar el mouse** sobre un elemento para ver detalles
- **Hacer clic en la leyenda** para mostrar/ocultar categorías
- **Hacer clic y arrastrar** para hacer zoom
- **Doble clic** para restaurar la vista original
- **Botón descarga** (arriba a la derecha) para guardar el gráfico

---

## ❓ Preguntas Frecuentes

### ¿Puedo usar mis datos sin Google Sheets?
Sí, la aplicación incluye datos de ejemplo. Selecciona "📁 Cargar datos de ejemplo" para probar todas las funciones.

### ¿Cómo agrego más datos?
Edita tu Google Sheets directamente, y la aplicación actualizará automáticamente cuando recargues.

### ¿Dónde descargo los datos procesados?
En la sección "💾 Descargar Datos" puedes exportar en CSV o Excel.

### ¿Qué formatos acepta?
Las fechas deben ser: **YYYY-MM-DD** (2024-01-15)
Las columnas deben llamarse exactamente: Cliente, Especie, Examen, Fecha, Resultado

### ¿Puedo personalizar los colores?
Sí, los colores se generan automáticamente. Para cambiarlos, edita el archivo `app.py`

---

## 🆘 Solucionar Problemas

### La aplicación no inicia
```bash
# Intenta instalar nuevamente
instalar.bat

# Luego ejecuta
ejecutar.bat
```

### Error: "No se puede acceder al Google Sheets"
- Verifica que el enlace esté compartido públicamente
- Copia nuevamente la URL
- Intenta con los datos de ejemplo primero

### Los datos no aparecen
- Verifica el formato de las fechas (YYYY-MM-DD)
- Verifica que los nombres de columnas sean exactos: Cliente, Especie, Examen, Fecha, Resultado

### La aplicación va lenta
- Esto puede suceder con muchos datos
- Intenta reducir el rango de fechas en tu Google Sheets

---

## 📞 Necesitas Ayuda Adicional

Revisa estos archivos:
- `README.md` - Documentación completa
- `CONFIGURACION_GOOGLE_SHEETS.md` - Cómo configurar Google Sheets

---

## ✅ Checklist Inicial

- [ ] Ejecuté `instalar.bat` sin errores
- [ ] Ejecuté `ejecutar.bat` y se abrió en el navegador
- [ ] Seleccioné los datos de ejemplo y vi los gráficos
- [ ] Entré en la sección de exámenes
- [ ] Probé los desplegables de cliente y especie
- [ ] Vi la matriz de relación
- [ ] Descargué los datos en CSV

---

## 🎉 ¡Listo!

Ya tienes tu análisis exploratorio de datos funcionando. 

**Próximos pasos:**
1. Prepara tu Google Sheets con tus datos
2. Conecta el enlace en la aplicación
3. ¡Explora y descubre insights de tus datos! 📊

---

**Desarrollado para Laboratorio de Microbiología Veterinaria 🧬**
