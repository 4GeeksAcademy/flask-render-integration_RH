from flask import Flask, render_template, request
import joblib
import numpy as np


app = Flask(__name__)

try:
    model = joblib.load("/workspaces/flask-render-integration_RH/src/modelo_titanic.pkl")
    MODEL_LOADED = True
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    MODEL_LOADED = False

@app.route('/')
def home():
    """Muestra el formulario principal."""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Recibe los datos del formulario y devuelve una predicción."""
    if not MODEL_LOADED:
        return render_template('index.html', error="El modelo de predicción no está disponible.")

    try:
        # 1. Recolectar datos del formulario.
        pclass = int(request.form['Pclass'])
        sex = int(request.form['Sex'])
        age = float(request.form['Age'])
        sibsp = int(request.form['SibSp'])
        parch = int(request.form['Parch'])
        fare = float(request.form['Fare'])
        embarked = int(request.form['Embarked']) # Este valor ya es 0, 1 o 2.


        input_data = np.array([[
            pclass, sex, age, sibsp, parch, fare, embarked
        ]])



        if prediction[0] == 1:
            output = "¡Habrías sobrevivido! 🚢🎉"
        else:
            output = "No habrías sobrevivido. 😔"

    except Exception as e:
        return render_template('index.html', error=f"Error en la predicción: {e}")


    return render_template('resultado.html', prediccion_texto=output)



if __name__ == '__main__':
    app.run(debug=True)