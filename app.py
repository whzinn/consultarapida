from flask import Flask, render_template, request, redirect, url_for
import mp
import os
app = Flask(__name__)

@app.route('/aqui', methods=['POST'])
def aqui():
    if request.method == 'POST':
        tipo_consulta = request.form['campo-seletor']
        campo = request.form['campo-texto']
        email = request.form['campo-email']
        pix = mp.pix(email, tipo_consulta, campo)
        # fazer algo com os dados recebidos
        return f"""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-GV5WKX5XPV">
</script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-GV5WKX5XPV');
</script>
<script>window.location = "{pix}";</script>
"""
@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('busca.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
