# Configuración de Google Sheets

## 📋 Estructura de Datos Requerida

Tu Google Sheets debe tener las siguientes columnas (en este orden):

| Cliente | Especie | Examen | Fecha | Resultado |
|---------|---------|--------|-------|-----------|

## 📝 Ejemplos de Datos

### Row 1 (Encabezados - OBLIGATORIO)
```
Cliente | Especie | Examen | Fecha | Resultado
```

### Row 2 y siguientes (Datos)
```
Clínica San José | Perro | Cultivo Bacteriano | 2024-01-15 | Positivo
Veterinaria La Paz | Gato | Antibiograma | 2024-01-16 | Sensible
Clínica San José | Perro | Cultivo Bacteriano | 2024-01-17 | Positivo
Veterinaria Rural | Bovino | Cultivo Bacteriano | 2024-01-18 | Positivo
Clínica San José | Gato | Coprocultivo | 2024-01-19 | Negativo
Veterinaria La Paz | Perro | Antibiograma | 2024-01-20 | Sensible
Veterinaria Rural | Bovino | Cultivo Bacteriano | 2024-01-21 | Positivo
Clínica Moderna | Equino | Cultivo Bacteriano | 2024-01-22 | Positivo
```

## 🎯 Campos Explicados

### 1. **Cliente**
- Nombre de la clínica, veterinaria o institución que solicita el examen
- Ejemplos: "Clínica San José", "Veterinaria La Paz", "Hospital Veterinario Moderno"

### 2. **Especie**
- Tipo de animal para el cual se realiza el examen
- Ejemplos comunes: Perro, Gato, Bovino, Equino, Ovino, Caprino, Porcino, Ave, Conejo

### 3. **Examen**
- Tipo de análisis microbiológico realizado
- Ejemplos comunes:
  - Cultivo Bacteriano
  - Antibiograma
  - Coprocultivo (análisis de heces)
  - Análisis Fecal
  - Cultivo de Orina
  - Cultivo Fúngico
  - PCR
  - Análisis Parasitológico

### 4. **Fecha**
- Fecha del examen en formato YYYY-MM-DD
- Ejemplos: 2024-01-15, 2024-02-20, 2024-03-10
- ⚠️ IMPORTANTE: Usa siempre el formato YYYY-MM-DD

### 5. **Resultado**
- Resultado del examen
- Valores comunes:
  - Positivo
  - Negativo
  - Sensible
  - Resistente
  - Inconcluso
  - Pendiente

---

## 🔗 Cómo Obtener la URL de Google Sheets

1. Abre tu Google Sheets
2. Haz clic en "Compartir" (arriba a la derecha)
3. Asegúrate que sea "Cualquiera con el enlace" puede verlo
4. Copia la URL que aparece en la barra de direcciones
5. Debería verse así:
   ```
   https://docs.google.com/spreadsheets/d/1A2B3C4D5E6F7G8H9I0J1K2L3M4N5O6P7Q8R9S0T/edit#gid=0
   ```
6. En la aplicación, pega esta URL cuando se te pida

---

## ✅ Checklist Antes de Usar

- [ ] Mi Google Sheets tiene las columnas: Cliente, Especie, Examen, Fecha, Resultado
- [ ] Los datos están en formato correcto (Fechas en YYYY-MM-DD)
- [ ] El Google Sheets está compartido públicamente o con enlace
- [ ] He copiado correctamente la URL del Google Sheets
- [ ] Tengo Python 3.8+ instalado
- [ ] He ejecutado el archivo instalar.bat

---

## 🚀 Cómo Usar la Aplicación

1. Abre un PowerShell o CMD en esta carpeta
2. Ejecuta: `instalar.bat` (solo la primera vez)
3. Luego ejecuta: `ejecutar.bat`
4. En la aplicación, selecciona "📊 Usar Google Sheets"
5. Pega tu URL de Google Sheets
6. ¡Explora los datos interactivamente!

---

## 📊 Funcionalidades Disponibles

Una vez cargados los datos, tendrás acceso a:

✅ Exámenes ordenados de más a menos común
✅ Desplegable para filtrar por cliente
✅ Desplegable para filtrar por especie
✅ Análisis temporal (tendencia en el tiempo)
✅ Matriz de relación clientes vs exámenes
✅ Heatmap visual
✅ Descarga de datos en CSV y Excel

---

**¡Espero que disfrutes explorando tus datos! 🧬**
