from flask import Flask , render_template, request, redirect, url_for
from validate_docbr import CPF , CNPJ
lista_produtos = [
        {"nome": "Coca-cola" , "descricao":"Beba água" , "preco": "5.00" , "imagem": "https://pbs.twimg.com/media/E38B0zOWQAMC1bu.jpg"},
        {"nome": "Pepsi" , "descricao":"Ruim" , "preco": "4.00", "imagem": "https://i.ytimg.com/vi/ey24G0EzJYI/maxresdefault.jpg"},
        {"nome": "Baly" , "descricao":"Custo beneficios" , "preco": "12.00" , "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq_wNULSboJKGGIQDg82K1h8bbtbdP_L_a8Q&s.jpg"},
    ]

app = Flask(__name__)

@app.route("/")
def home(): 
    return '<h1>Home</h1>'

@app.route("/contato")
def contato(): 
    return '<h1>Contato</h1>'

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos = lista_produtos)
 
@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto["nome"] == nome:
            return render_template("produto.html", produto=produto)


    return "Produto não existe!" @app.route('/gerar_cnpj')
def gerar_cnpj():
    cnpj = CNPJ()
    novo_cnpj = cnpj.generate(True)
    return render_template('gerar_cnpj.html', cnpj=novo_cnpj)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro-produto.html")

@app.route("/produtos", methods=["POST"])
def salvar_produto():
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    preco = request.form["preco"]
    imagem = request.form["imagem"]
    produto = {"nome": nome, "descricao": descricao, "preco": preco, "imagem": imagem}
    lista_produtos.append(produto)

    return redirect(url_for("produtos"))

app.run(port=5001)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/gerar_cpf')
def gerar_cpf():
    cpf = CPF()
    novo_cpf = cpf.generate(True)
    return render_template('gerar_cpf.html', cpf=novo_cpf)

@app.route('/gerar_cnpj')
def gerar_cnpj():
    cnpj = CNPJ()
    novo_cnpj = cnpj.generate(True)
    return render_template('gerar_cnpj.html', cnpj=novo_cnpj)

@app.route('/validar_cpf', methods=["GET", "POST"])
def validar_cpf():
    if request.method == "POST":
        cpf_usuario = request.form["cpf_usuario"]
        cpf = CPF()
        if cpf.validate(cpf_usuario):
            mensagem = "CPF válido!"
        else:
            mensagem = "CPF inválido!"
        return render_template("validar_cpf.html", mensagem=mensagem)
    return render_template("validar_cpf.html")

@app.route('/validar_cnpj', methods=["GET", "POST"])
def validar_cnpj():
    if request.method == "POST":
        cnpj_usuario = request.form["cnpj_usuario"]
        cnpj = CNPJ()
        if cnpj.validate(cnpj_usuario):
            mensagem = "CNPJ válido!"
        else:
            mensagem = "CNPJ inválido!"
        return render_template("validar_cnpj.html", mensagem=mensagem)
    return render_template("validar_cnpj.html")

if __name__ == '__main__':
    app.run(debug=True)