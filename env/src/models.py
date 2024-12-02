from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.preprocessing import LabelEncoder

def train_logistic_regression(data):
    # Codificar categorías
    def categorize_user(total_spent):
        if total_spent < 200:
            return "Basic"
        elif total_spent < 400:
            return "Gold"
        else:
            return "Premium"
    data['category'] = data['total_spent'].apply(categorize_user)
    encoder = LabelEncoder()
    data['category_encoded'] = encoder.fit_transform(data['category'])

    # Separar características y etiquetas
    X = data[['purchase_frequency', 'total_spent', 'visits']]
    y = data['category_encoded']

    # Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar modelo
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluar modelo
    accuracy = model.score(X_test, y_test)
    return model, accuracy

def train_linear_regression(data):
    # Separar características y etiquetas
    X = data[['purchase_frequency', 'visits']]
    y = data['total_spent']

    # Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar modelo
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluar modelo
    mse = model.score(X_test, y_test)
    return model, mse
