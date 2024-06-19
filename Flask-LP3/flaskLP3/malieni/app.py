from flask import Flask , render_template, request, redirect, url_for
lista_produtos = [
        {"nome": "Coca-cola" , "descricao":"Bom" , "preco": "5.00" , "imagem": "https://i.ytimg.com/vi/kgCJV5ChGa4/maxresdefault.jpg"},
        {"nome": "Pepsi" , "descricao":"Ruim" , "preco": "4.00", "imagem": "https://i.ytimg.com/vi/ey24G0EzJYI/maxresdefault.jpg"},
        {"nome": "Dolly" , "descricao":"Custo beneficios" , "preco": "2.00" , "imagem": "https://i1.sndcdn.com/artworks-000504423309-2hzdh2-t500x500.jpg"},
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


    return "Produto não existe!" 

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