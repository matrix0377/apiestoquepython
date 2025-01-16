from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estoques.db'
db = SQLAlchemy(app)

class Estoque(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    embalagem = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    observacao = db.Column(db.String(200), nullable=True)

class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, nullable=False)
    metodo = db.Column(db.String(10), nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)
    descricao = db.Column(db.String(100), nullable=False)
    embalagem = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    observacao = db.Column(db.String(200), nullable=True)

@app.route('/estoque', methods=['POST'])
def adicionar_estoque():
    novo_estoque = Estoque(
        descricao=request.json['descricao'],
        embalagem=request.json['embalagem'],
        quantidade=request.json['quantidade'],
        observacao=request.json['observacao']
    )
    db.session.add(novo_estoque)
    db.session.commit()

    novo_historico = Historico(
        produto_id=novo_estoque.id,
        metodo='POST',
        descricao=novo_estoque.descricao,
        embalagem=novo_estoque.embalagem,
        quantidade=novo_estoque.quantidade,
        observacao=novo_estoque.observacao
    )
    db.session.add(novo_historico)
    db.session.commit()

    return jsonify({
        'mensagem': 'Produto cadastrado com sucesso!',
        'id': novo_estoque.id,
        'descricao': novo_estoque.descricao,
        'embalagem': novo_estoque.embalagem,
        'quantidade': novo_estoque.quantidade,
        'observacao': novo_estoque.observacao
    }), 201

@app.route('/estoque', methods=['GET'])
def listar_estoques():
    ids = request.args.getlist('id')
    if ids:
        estoques = Estoque.query.filter(Estoque.id.in_(ids)).all()
    else:
        estoques = Estoque.query.all()
    lista_estoques = []
    for estoque in estoques:
        lista_estoques.append({
            'id': estoque.id,
            'descricao': estoque.descricao,
            'embalagem': estoque.embalagem,
            'quantidade': estoque.quantidade,
            'observacao': estoque.observacao
        })
    return jsonify(lista_estoques)

@app.route('/estoque/<int:id>', methods=['PUT'])
def atualizar_estoque(id):
    estoque = Estoque.query.get_or_404(id)
    estoque.descricao = request.json.get('descricao', estoque.descricao)
    estoque.embalagem = request.json.get('embalagem', estoque.embalagem)
    estoque.quantidade = request.json.get('quantidade', estoque.quantidade)
    estoque.observacao = request.json.get('observacao', estoque.observacao)
    db.session.commit()

    novo_historico = Historico(
        produto_id=estoque.id,
        metodo='PUT',
        descricao=estoque.descricao,
        embalagem=estoque.embalagem,
        quantidade=estoque.quantidade,
        observacao=estoque.observacao
    )
    db.session.add(novo_historico)
    db.session.commit()

    return jsonify({
        'id': estoque.id,
        'descricao': estoque.descricao,
        'embalagem': estoque.embalagem,
        'quantidade': estoque.quantidade,
        'observacao': estoque.observacao
    })

@app.route('/estoque/<int:id>', methods=['DELETE'])
def excluir_estoque(id):
    estoque = Estoque.query.get_or_404(id)
    db.session.delete(estoque)

    novo_historico = Historico(
        produto_id=estoque.id,
        metodo='DELETE',
        descricao=estoque.descricao,
        embalagem=estoque.embalagem,
        quantidade=estoque.quantidade,
        observacao=estoque.observacao
    )
    db.session.add(novo_historico)
    db.session.commit()

    db.session.commit()
    return jsonify({'mensagem': 'Produto excluído com sucesso!'})

@app.route('/historico', methods=['GET'])
def listar_historico():
    historico = Historico.query.all()
    lista_historico = []
    for entry in historico:
        lista_historico.append({
            'id': entry.id,
            'produto_id': entry.produto_id,
            'metodo': entry.metodo,
            'data_hora': entry.data_hora.strftime('%Y-%m-%d %H:%M:%S'),
            'descricao': entry.descricao,
            'embalagem': entry.embalagem,
            'quantidade': entry.quantidade,
            'observacao': entry.observacao
        })
    return jsonify(lista_historico)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
