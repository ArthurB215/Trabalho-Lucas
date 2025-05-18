from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicial():
    return render_template('inicial.html')

@app.route('/editor-imagem')
def editor_imagem():
    return render_template('ImgEdit.html')

if __name__ == '__main__':
    app.run(debug=True)
