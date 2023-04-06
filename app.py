from flask import Flask, render_template, request, redirect, url_for
import mp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        tipo_consulta = request.form['campo-seletor']
        campo = request.form['campo-texto']
        email = request.form['campo-email']
        pix = mp.pix(email, tipo_consulta, campo)
        # fazer algo com os dados recebidos
        return f"""<script>window.location = "{pix}";</script>
"""
    return render_template('busca.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)

