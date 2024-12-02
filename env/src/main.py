from src.data_processing import load_and_clean_data
from src.models import train_logistic_regression, train_linear_regression
from src.sentiment_analysis import analyze_sentiments
from src.visualization import plot_distributions
import pandas as pd

# Paso 1: Cargar y procesar datos
data = load_and_clean_data("data/data.csv")

# Paso 2: Entrenar y evaluar modelo de clasificación
classification_model, accuracy = train_logistic_regression(data)
print(f"Accuracy del modelo de clasificación: {accuracy:.2f}")

# Paso 3: Entrenar y evaluar modelo de predicción
regression_model, mse = train_linear_regression(data)
print(f"Mean Squared Error del modelo de predicción: {mse:.2f}")

# Paso 4: Análisis de sentimiento
data = analyze_sentiments(data)

# Paso 5: Generar visualizaciones
plot_distributions(data)

# Paso 6: Exportar resultados
data.to_excel("reports/final_report.xlsx", index=False)
print("Reporte exportado a 'reports/final_report.xlsx'")
