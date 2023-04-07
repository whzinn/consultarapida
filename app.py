from flask import Flask, render_template, request, redirect, url_for
import mp
import os
app = Flask(__name__)

@app.route('/pagar?pix=<pix>', methods=['GET'])
def pagar(pix):
    return f"""<script>window.location = "{pix}";</script>
"""

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        tipo_consulta = request.form['campo-seletor']
        campo = request.form['campo-texto']
        email = request.form['campo-email']
        pix = mp.pix(email, tipo_consulta, campo)
        # fazer algo com os dados recebidos
        return return f"""<script>window.location = "https://consultarapida.onrender.com/pagar?pix={pix}";</script>
"""
    return render_template('busca.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
