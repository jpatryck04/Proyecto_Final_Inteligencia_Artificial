Este proyecto "Clasificación de Usuarios para un Programa de Fidelidad" tiene como objetivo segmentar a los usuarios en categorías de fidelidad utilizando modelos de aprendizaje automático. 
Este enfoque ayuda a las empresas a personalizar sus estrategias de marketing y mejorar la retención de clientes.

--Requisitos de Software:

Python 3.8 o superior
Pip (gestor de paquetes de Python)

--Instalación de Dependencias
Para instalar las dependencias necesarias, se deben segir lo siguientes pasos:

1. Clona el repositorio del proyecto:
git clone https://github.com/jpatryck04/Proyecto_Final_Inteligencia_Artificial.git
cd Proyecto_Final_Inteligencia_Artificial

2.Instala las dependencias con Pip:
pip install -r requirements.txt


--Ejecución del Script Principal
python main.py

--Descripción de los Pasos
-Carga y limpieza de datos: Se utiliza la función load_and_clean_data para cargar el archivo CSV y procesar los datos.

-Entrenamiento de modelos:
♦Regresión logística: Entrena un modelo para clasificar a los usuarios en categorías de fidelidad (Básico, Oro, Premium).

♦Regresión lineal: Predice el gasto total de los usuarios.

-Análisis de sentimiento: Utiliza la función analyze_sentiments para analizar los comentarios de los usuarios.

-Visualización: La función plot_distributions genera gráficos para analizar la distribución de las características de los datos.

-Exportación de resultados: Se exporta un informe con los datos procesados a reports/final_report.xlsx.
