import matplotlib.pyplot as plt
import seaborn as sns

def plot_distributions(data):
    # Gráfico de niveles de fidelidad
    sns.countplot(x='category', data=data)
    plt.title("Distribución de Niveles de Fidelidad")
    plt.show()

    # Gráfico de sentimientos
    sns.histplot(data['sentiment'], bins=20, kde=True)
    plt.title("Distribución de Sentimientos")
    plt.show()
    