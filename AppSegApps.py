from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola! Andrea!!!! \n\n Tu servidor Flask está funcionando correctamente. \n\n SEGURIDAD DE APLICACIONES"

if __name__ == "__main__":
    app.run(debug=True)
