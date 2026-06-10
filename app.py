import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import warnings
from config import URL_SHEETS_SIRIO, PAGE_TITLE, PAGE_ICON, PAGE_LAYOUT, CACHE_TTL, COLUMN_MAPPING

warnings.filterwarnings('ignore')

# ================== FUNCIÓN HELPER PARA MAPEO DE COLUMNAS ==================
def get_col(column_name):
    """
    Obtiene el nombre real de columna desde COLUMN_MAPPING
    Args: column_name (str): Nombre interno (ej: 'cliente', 'examen')
    Returns: str o None: Nombre real de columna o None si no existe
    """
    return COLUMN_MAPPING.get(column_name.lower())

# Configuración de la página
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=PAGE_LAYOUT
)

# Evitar que el traductor del navegador (Google Translate, etc.) interfiera y rompa React (removeChild error)
import streamlit.components.v1 as components
components.html("""
    <script>
        try {
            // Modificar el documento principal para desactivar la traducción automática
            const parentDoc = window.parent.document;
            
            parentDoc.documentElement.setAttribute('translate', 'no');
            parentDoc.documentElement.classList.add('notranslate');
            
            parentDoc.body.setAttribute('translate', 'no');
            parentDoc.body.classList.add('notranslate');
            
            // Añadir etiquetas meta de no traducción
            if (!parentDoc.querySelector('meta[name="google"][content="notranslate"]')) {
                const meta1 = parentDoc.createElement('meta');
                meta1.name = 'google';
                meta1.content = 'notranslate';
                parentDoc.head.appendChild(meta1);
            }
            
            if (!parentDoc.querySelector('meta[name="googlebot"][content="notranslate"]')) {
                const meta2 = parentDoc.createElement('meta');
                meta2.name = 'googlebot';
                meta2.content = 'notranslate';
                parentDoc.head.appendChild(meta2);
            }
            console.log("Traducción automática desactivada con éxito.");
        } catch (e) {
            console.warn("No se pudo desactivar traducción automática en el documento principal (posible restricción CORS):", e);
        }
    </script>
""", height=0)

# Estilos y título
st.markdown("""
    <h1 style='text-align: center; color: #1f77b4;'>🧬 Análisis de Datos - Laboratorio Microbiología Veterinaria</h1>
    """, unsafe_allow_html=True)

st.markdown("---")

# Función para limpiar y normalizar los datos
def limpiar_dataframe(df):
    """
    Limpia el DataFrame: elimina espacios, maneja NaN y booleanos
    """
    try:
        # Reemplazar todos los NaN y valores vacíos con strings vacíos
        df = df.fillna("")
        
        # Convertir TODO a string para evitar problemas de tipo
        for col in df.columns:
            df[col] = df[col].astype(str)
        
        # Limpiar espacios en valores de texto (no cambiar nombres de columnas aquí)
        for col in df.columns:
            try:
                df[col] = df[col].str.strip()
                # Reemplazar "none", "nan", etc. con vacío
                df[col] = df[col].replace(["None", "nan", "<NA>", "NaN", "none"], "")
            except:
                pass
        
        return df
    except Exception as e:
        print(f"Error al limpiar dataframe: {e}")
        return df

# Función para conectar con Google Sheets
@st.cache_data
def cargar_datos_google_sheets(url_sheets):
    """
    Carga datos desde Google Sheets y renombra columnas según COLUMN_MAPPING
    """
    try:
        # Extrae el ID de la hoja
        sheet_id = url_sheets.split('/d/')[1].split('/')[0]
        url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv'
        
        # Cargar con opciones que manejan mejor valores vacíos y especiales
        df = pd.read_csv(
            url, 
            dtype=str,
            keep_default_na=False,  # No interpretar valores como NaN
            na_values=['']  # Solo "" es considerado como NaN
        )
        
        # Rellenar cualquier NaN con vacío
        df = df.fillna("")
        
        # Limpiar el dataframe
        df = limpiar_dataframe(df)
        
        # Remover filas completamente vacías
        df = df[(df != "").any(axis=1)]
        
        # ========== RENOMBRAR COLUMNAS SEGÚN COLUMN_MAPPING ==========
        rename_dict = {}
        for internal_name, real_name in COLUMN_MAPPING.items():
            if real_name and real_name in df.columns:
                rename_dict[real_name] = internal_name.capitalize()
        
        df = df.rename(columns=rename_dict)
        
        return df
    except Exception as e:
        st.error(f"❌ Error al cargar los datos: {e}")
        return None

# Sidebar para configuración
st.sidebar.title("⚙️ Configuración")

# Cargar datos automáticamente desde Google Sheets
@st.cache_data(ttl=CACHE_TTL)
def cargar_datos_sirio():
    """Carga los datos del Google Sheets del Laboratorio SIRIO"""
    return cargar_datos_google_sheets(URL_SHEETS_SIRIO)

# Intentar cargar datos automáticamente
with st.spinner("📊 Cargando datos del Laboratorio SIRIO..."):
    df = cargar_datos_sirio()
    
if df is None or df.empty:
    st.warning("⚠️ No se pudieron cargar los datos. Mostrando datos de ejemplo...")
    # Datos de ejemplo como fallback
    df = pd.DataFrame({
        'Cliente': ['Clínica San José', 'Veterinaria La Paz', 'Clínica San José', 
                    'Veterinaria Rural', 'Clínica San José', 'Veterinaria La Paz',
                    'Veterinaria Rural', 'Clínica Moderna', 'Clínica San José',
                    'Veterinaria La Paz', 'Clínica Moderna', 'Veterinaria Rural'],
        'Especie': ['Perro', 'Gato', 'Perro', 'Bovino', 'Gato', 'Perro',
                    'Bovino', 'Equino', 'Perro', 'Gato', 'Equino', 'Bovino'],
        'Examen': ['Cultivo Bacteriano', 'Antibiograma', 'Cultivo Bacteriano',
                   'Cultivo Bacteriano', 'Coprocultivo', 'Antibiograma',
                   'Cultivo Bacteriano', 'Cultivo Bacteriano', 'Análisis Fecal',
                   'Coprocultivo', 'Cultivo Bacteriano', 'Análisis Fecal'],
        'Fecha': pd.date_range('2024-01-01', periods=12, freq='W'),
        'Resultado': ['Positivo', 'Sensible', 'Positivo', 'Positivo', 'Negativo', 'Sensible',
                      'Positivo', 'Positivo', 'Positivo', 'Negativo', 'Positivo', 'Negativo']
    })
    df = limpiar_dataframe(df)
else:
    st.sidebar.success("✅ Datos cargados correctamente")
    
    # Botón para recargar datos
    if st.sidebar.button("🔄 Recargar Datos"):
        st.cache_data.clear()
        st.rerun()
    
    # Información de los datos
    st.sidebar.markdown("---")
    st.sidebar.metric("📊 Total de Registros", len(df))
    st.sidebar.metric("👥 Clientes Únicos", df['Cliente'].nunique())
    st.sidebar.metric("🐾 Especies", df['Especie'].nunique())
    st.sidebar.metric("📋 Tipos de Examen", df['Examen'].nunique())

# Validar que existan las columnas requeridas
columnas_requeridas = ['Cliente', 'Especie', 'Examen', 'Fecha', 'Resultado']
columnas_disponibles = df.columns.tolist()
columnas_faltantes = [col for col in columnas_requeridas if col not in columnas_disponibles]

if columnas_faltantes:
    st.warning(f"⚠️ Columnas faltantes: {', '.join(columnas_faltantes)}")
    st.info(f"📋 Columnas disponibles: {', '.join(columnas_disponibles)}")
    # No detenemos la ejecución, solo mostramos advertencia

# Mostrar vista previa de los datos
with st.expander("📋 Ver datos crudos"):
    st.dataframe(df, use_container_width=True)

st.markdown("---")

# ============ SECCIÓN 1: EXÁMENES POR FRECUENCIA ============
# Contar exámenes (excluir valores vacíos)
df_examenes = df[df['Examen'] != ""].copy()

if len(df_examenes) > 0:
    examenes_freq = df_examenes['Examen'].value_counts().reset_index()
    examenes_freq.columns = ['Examen', 'Cantidad']
    
    # Ordenar y tomar solo los primeros 20
    examenes_freq = examenes_freq.sort_values(
        'Cantidad',
        ascending=False
    ).head(20)

    # Gráfico de barras
    fig_examenes = px.bar(
        examenes_freq,
        x='Examen',
        y='Cantidad',
        title='📈 Top 20 Exámenes Más Solicitados',
        labels={
            'Cantidad': 'Número de Solicitudes',
            'Examen': 'Tipo de Examen'
        },
        color='Cantidad',
        color_continuous_scale='Blues'
    )

    fig_examenes.update_layout(
        height=400,
        showlegend=False,
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig_examenes, use_container_width=True)

# ============ SECCIÓN 2: ANÁLISIS POR CLIENTE ============
st.header("👥 2. Análisis de Clientes")

if 'Cliente' in df.columns:
    try:
        # Filtrar clientes con datos válidos
        df_clientes = df[df['Cliente'] != ""].copy()
        clientes_unicos = sorted(df_clientes['Cliente'].unique())
        
        if len(clientes_unicos) > 0:
            # Desplegable de cliente - Añadir opción "Todos los Clientes"
            opciones_cliente = ["🔹 Todos los Clientes"] + list(clientes_unicos)
            cliente_seleccionado = st.selectbox(
                "Selecciona un cliente:",
                opciones_cliente,
                key="cliente_select"
            )

            # Lógica para filtrar: si selecciona "Todos", usa todos; si no, filtra por cliente
            es_todos_clientes = cliente_seleccionado == "🔹 Todos los Clientes"
            
            if es_todos_clientes:
                df_cliente = df_clientes.copy()
                titulo_cliente = "Todos los Clientes"
            else:
                df_cliente = df_clientes[df_clientes['Cliente'] == cliente_seleccionado]
                titulo_cliente = cliente_seleccionado

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Total de Exámenes Solicitados", len(df_cliente))
                
            with col2:
                if 'Especie' in df_cliente.columns:
                    st.metric("Especies Atendidas", df_cliente[df_cliente['Especie'] != ""]["Especie"].nunique())
                
            with col3:
                if 'Examen' in df_cliente.columns:
                    st.metric("Tipos de Exámenes", df_cliente[df_cliente['Examen'] != ""]["Examen"].nunique())

            # Exámenes del cliente(s) seleccionado(s)
            if 'Examen' in df_cliente.columns:
                st.subheader(f"Exámenes solicitados por {titulo_cliente}")
                df_cliente_examenes = df_cliente[df_cliente['Examen'] != ""].copy()
                
                if len(df_cliente_examenes) > 0:
                    examenes_cliente = df_cliente_examenes['Examen'].value_counts().reset_index()
                    examenes_cliente.columns = ['Examen', 'Cantidad']

                    # ========== LÓGICA ESPECIAL PARA "TODOS LOS CLIENTES" ==========
                    if es_todos_clientes:
                        # Solo mostrar TOP 15 exámenes más comunes
                        examenes_cliente_top15 = examenes_cliente.head(15).copy()
                        
                        # Calcular porcentajes
                        total_examenes = examenes_cliente_top15['Cantidad'].sum()
                        examenes_cliente_top15['Porcentaje'] = (examenes_cliente_top15['Cantidad'] / total_examenes * 100).round(1)
                        
                        # Crear gráfico circular CON PORCENTAJES
                        fig_cliente = px.pie(
                            examenes_cliente_top15,
                            names='Examen',
                            values='Cantidad',
                            title=f'Top 15 Exámenes Más Comunes - {titulo_cliente}',
                            labels={'Cantidad': 'Cantidad', 'Porcentaje': 'Porcentaje %'},
                            hover_data={'Porcentaje': ':.1f'},
                            hole=0.0  # Gráfico circular sin agujero
                        )
                        
                        # Añadir porcentajes en el gráfico
                        fig_cliente.update_traces(
                            textposition='inside',
                            textinfo='label+percent',
                            hovertemplate='<b>%{label}</b><br>Cantidad: %{value}<br>Porcentaje: %{customdata[0]:.1f}%<extra></extra>'
                        )
                        
                        st.plotly_chart(fig_cliente, use_container_width=True)
                        
                        # Mostrar tabla de los top 15
                        st.dataframe(examenes_cliente_top15[['Examen', 'Cantidad', 'Porcentaje']], use_container_width=True)
                    
                    else:
                        # CLIENTE INDIVIDUAL: mostrar como antes
                        fig_cliente = px.pie(
                            examenes_cliente,
                            names='Examen',
                            values='Cantidad',
                            title=f'Distribución de Exámenes - {titulo_cliente}',
                            hole=0.3
                        )
                        st.plotly_chart(fig_cliente, use_container_width=True)

                        st.dataframe(examenes_cliente, use_container_width=True)
                else:
                    st.info("No hay datos de exámenes para esta selección")
        else:
            st.warning("No hay datos de clientes disponibles")
    except Exception as e:
        st.error(f"Error al procesar clientes: {e}")
else:
    st.warning("⚠️ La columna 'Cliente' no existe en los datos")

st.markdown("---")

# ============ SECCIÓN 3: ANÁLISIS POR ESPECIE ============
st.header("🐾 3. Análisis por Especie Animal")

if 'Especie' in df.columns:
    try:
        # Filtrar especies con datos válidos
        df_especies = df[df['Especie'] != ""].copy()
        especies_unicas = sorted(df_especies['Especie'].unique())
        
        if len(especies_unicas) > 0:
            especie_seleccionada = st.selectbox(
                "Selecciona una especie:",
                especies_unicas,
                key="especie_select"
            )

            df_especie = df_especies[df_especies['Especie'] == especie_seleccionada]

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Exámenes para esta especie", len(df_especie))
                
            with col2:
                if 'Cliente' in df_especie.columns:
                    st.metric("Clientes que atienden esta especie", df_especie[df_especie['Cliente'] != ""]["Cliente"].nunique())
                
            with col3:
                if 'Examen' in df_especie.columns:
                    st.metric("Tipos de exámenes", df_especie[df_especie['Examen'] != ""]["Examen"].nunique())

            st.subheader(f"Exámenes más solicitados para {especie_seleccionada}")
            
            if 'Examen' in df_especie.columns:
                df_especie_examenes = df_especie[df_especie['Examen'] != ""].copy()
                
                if len(df_especie_examenes) > 0:
                    examenes_especie = df_especie_examenes['Examen'].value_counts().reset_index()
                    examenes_especie.columns = ['Examen', 'Cantidad']

                    fig_especie = px.bar(
                        examenes_especie,
                        x='Examen',
                        y='Cantidad',
                        title=f'Exámenes para {especie_seleccionada}',
                        color='Cantidad',
                        color_continuous_scale='Viridis'
                    )
                    fig_especie.update_layout(height=400, xaxis_tickangle=-45)
                    st.plotly_chart(fig_especie, use_container_width=True)

                    st.dataframe(examenes_especie, use_container_width=True)
                else:
                    st.info(f"No hay datos de exámenes para {especie_seleccionada}")
        else:
            st.warning("No hay datos de especies disponibles")
    except Exception as e:
        st.error(f"Error al procesar especies: {e}")
else:
    st.warning("⚠️ La columna 'Especie' no existe en los datos")

st.markdown("---")

# ============ SECCIÓN 4: MATRIZ DE RELACIÓN: CLIENTES vs EXÁMENES ============
st.header("🔗 4. Matriz de Relación: Clientes vs Exámenes")

if 'Cliente' in df.columns and 'Examen' in df.columns:
    try:
        # Filtrar datos válidos
        df_matriz = df[(df['Cliente'] != "") & (df['Examen'] != "")].copy()
        
        if len(df_matriz) > 0:
            # 1. Mostrar clientes con cantidad de registros
            st.subheader("👥 Clientes por Número de Registros")
            
            # Calcular registros por cliente
            df_clientes_counts = df_matriz['Cliente'].value_counts().reset_index()
            df_clientes_counts.columns = ['Cliente', 'Cantidad de Registros']
            total_registros = df_clientes_counts['Cantidad de Registros'].sum()
            df_clientes_counts['Porcentaje %'] = ((df_clientes_counts['Cantidad de Registros'] / total_registros) * 100).round(1)
            
            # Mostrar la tabla resumida sin ceros redundantes
            st.dataframe(df_clientes_counts, use_container_width=True)
            
            # 2. Configurar y mostrar el Heatmap filtrado por clientes más activos
            st.subheader("🔥 Heatmap de Incidencia: Clientes Más Activos vs Exámenes")
            st.markdown("Visualiza la relación de exámenes solicitados únicamente por los clientes con mayor volumen de registros.")
            
            # Determinar dinámicamente el rango del control de Top Clientes
            num_clientes_unicos = len(df_clientes_counts)
            max_slider = min(30, num_clientes_unicos)
            default_slider = min(10, num_clientes_unicos)
            
            if num_clientes_unicos > 5:
                top_n = st.slider(
                    "Selecciona la cantidad de Top Clientes a visualizar en el Heatmap:",
                    min_value=5,
                    max_value=max_slider,
                    value=default_slider,
                    key="heatmap_top_n"
                )
            else:
                top_n = num_clientes_unicos
                
            # Obtener nombres de los top N clientes
            top_clientes = df_clientes_counts.head(top_n)['Cliente'].tolist()
            
            # Filtrar el DataFrame de la matriz para los clientes seleccionados
            df_matriz_top = df_matriz[df_matriz['Cliente'].isin(top_clientes)].copy()
            
            if len(df_matriz_top) > 0:
                # Crear la tabla de incidencia cruzada
                matriz_cliente_examen = pd.crosstab(df_matriz_top['Cliente'], df_matriz_top['Examen'])
                
                # Reordenar las filas para que vayan de más activos a menos activos
                matriz_cliente_examen = matriz_cliente_examen.reindex(top_clientes)
                
                # Excluir exámenes (columnas) que tengan cero solicitudes entre este grupo de clientes top
                matriz_cliente_examen = matriz_cliente_examen.loc[:, (matriz_cliente_examen != 0).any(axis=0)]
                
                if not matriz_cliente_examen.empty:
                    fig_heatmap = px.imshow(
                        matriz_cliente_examen,
                        labels=dict(x='Tipo de Examen', y='Cliente', color='Solicitudes'),
                        title=f'Heatmap: Top {top_n} Clientes vs Exámenes Solicitados',
                        color_continuous_scale='YlOrRd',
                        text_auto=True  # Muestra el número dentro de la celda
                    )
                    fig_heatmap.update_layout(
                        height=500,
                        xaxis_tickangle=-45
                    )
                    st.plotly_chart(fig_heatmap, use_container_width=True)
                else:
                    st.info("No hay datos cruzados suficientes para graficar.")
            else:
                st.info("No se encontraron registros para los clientes seleccionados.")
        else:
            st.info("No hay datos de clientes y exámenes válidos.")
    except Exception as e:
        st.error(f"Error al procesar la matriz: {e}")
else:
    st.warning("⚠️ Faltan columnas 'Cliente' o 'Examen' para esta sección")

st.markdown("---")

# ============ SECCIÓN 5: RESULTADOS Y ANÁLISIS TEMPORAL ============
st.header("📅 5. Análisis Temporal y Resultados")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribución de Resultados")
    if 'Resultado' in df.columns:
        try:
            df_resultados = df[df['Resultado'] != ""].copy()
            if len(df_resultados) > 0:
                resultados = df_resultados['Resultado'].value_counts()
                fig_resultados = px.bar(
                    resultados.reset_index(),
                    x='Resultado',
                    y='count',
                    title='Resultados de Exámenes',
                    labels={'count': 'Cantidad', 'Resultado': 'Tipo de Resultado'},
                    color='count',
                    color_continuous_scale='RdYlGn'
                )
                st.plotly_chart(fig_resultados, use_container_width=True)
            else:
                st.info("No hay datos de resultados")
        except Exception as e:
            st.error(f"Error al procesar resultados: {e}")
    else:
        st.warning("⚠️ La columna 'Resultado' no existe")

with col2:
    st.subheader("Tendencia Temporal")
    if 'Fecha' in df.columns:
        try:
            df_tiempo = df[df['Fecha'] != ""].copy()
            if len(df_tiempo) > 0:
                # Intentar convertir a datetime
                try:
                    df_tiempo['Fecha'] = pd.to_datetime(df_tiempo['Fecha'])
                    df_tiempo = df_tiempo.sort_values('Fecha')
                    df_tiempo['Semana'] = df_tiempo['Fecha'].dt.strftime('%Y-%W')
                    exams_por_semana = df_tiempo.groupby('Semana').size().reset_index(name='Cantidad')
                    
                    if len(exams_por_semana) > 0:
                        fig_tiempo = px.line(
                            exams_por_semana,
                            x='Semana',
                            y='Cantidad',
                            title='Exámenes Solicitados en el Tiempo',
                            markers=True
                        )
                        fig_tiempo.update_layout(height=400)
                        st.plotly_chart(fig_tiempo, use_container_width=True)
                    else:
                        st.info("No hay datos para mostrar tendencia")
                except:
                    st.info("No se pudo procesar la columna de fechas (formato inválido)")
            else:
                st.info("No hay datos de fechas válidas")
        except Exception as e:
            st.error(f"Error al procesar temporal: {e}")
    else:
        st.warning("⚠️ La columna 'Fecha' no existe")

st.markdown("---")

# ============ SECCIÓN 6: RESUMEN Y ESTADÍSTICAS ============
st.header("📈 6. Resumen Estadístico General")

try:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total de Registros", len(df))
    with col2:
        if 'Cliente' in df.columns:
            st.metric("Total de Clientes", df[df['Cliente'] != ""]["Cliente"].nunique())
    with col3:
        if 'Especie' in df.columns:
            st.metric("Total de Especies", df[df['Especie'] != ""]["Especie"].nunique())

    col1, col2, col3 = st.columns(3)

    with col1:
        if 'Examen' in df.columns:
            st.metric("Total de Tipos de Examen", df[df['Examen'] != ""]["Examen"].nunique())
    with col2:
        if 'Resultado' in df.columns:
            positivos = len(df[(df['Resultado'] == 'Positivo') | (df['Resultado'] == 'positivo')])
            st.metric("Exámenes Positivos", positivos)
    with col3:
        if 'Resultado' in df.columns:
            positivos = len(df[(df['Resultado'] == 'Positivo') | (df['Resultado'] == 'positivo')])
            if len(df) > 0:
                porcentaje_pos = (positivos / len(df)) * 100
                st.metric("Porcentaje Positivos", f"{porcentaje_pos:.1f}%")
except Exception as e:
    st.error(f"Error al calcular estadísticas: {e}")

st.markdown("---")

# ============ SECCIÓN 7: DESCARGA DE DATOS ============
st.header("💾 7. Descargar Datos")

col1, col2 = st.columns(2)

with col1:
    try:
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Descargar datos en CSV",
            data=csv,
            file_name="datos_laboratorio.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"Error al generar CSV: {e}")

with col2:
    try:
        # Usar BytesIO para Excel para evitar problemas
        import io
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False, engine='openpyxl')
        excel_buffer.seek(0)
        
        st.download_button(
            label="📊 Descargar datos en Excel",
            data=excel_buffer,
            file_name="datos_laboratorio.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.warning(f"No se puede descargar en Excel: {e}. Usa CSV en su lugar.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Desarrollado para Laboratorio de Microbiología Veterinaria 🧬</p>", unsafe_allow_html=True)
