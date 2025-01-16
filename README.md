# apiestoquepython
Esta api tem como utilidade um cadastro de estoque de Produtos

# Projeto de Api Estoque Python Flask com Histórico

# Detalhes
- Data: 16/01/2025
- Python: 3.12.7
- Flask:
- objetivo: api para cadastrar estoque de Mercadorias/Equipamentos
- Ambiente Virtual: ./venvapi/Scripts/activate  (deactivate)
- IA: Copilot
- Método Histórico: guarda no BD as alterações feitas usando os métodos POST(inserir), PUT(atualizar) e DELETE (apagar).

# JSON
{
    "descricao": "Descrição do Produto",
    "embalagem": "Tipo de Embalagem",
    "quantidade": 100,
    "observacao": "Observações adicionais"
}

--- EndPoint (POSTMAN)
Use uma ferramenta como Postman ou curl para enviar requisições POST, GET, UPDATE e DELETE para gerenciar informações 

# Para listar produtos específicos, passe os IDs como parâmetros de consulta:
GET http://127.0.0.1:5000/estoque?id=1&id=2&id=3 


# Exemplo: http://127.0.0.1:5000/estoque?id=1&id=2&id=3
** mostra os produtos dos IDs solicitados: id2, id3

# Para buscar um único produto fornecendo seu ID, você pode fazer uma requisição GET com um único parâmetro de consulta id.
GET http://127.0.0.1:5000/estoque?id=2



GET http://127.0.0.1:5000/estoque (Para listar todos os produtos)

POST http://127.0.0.1:5000/estoque

PUT http://127.0.0.1:5000/estoque{id}

DELETE http://127.0.0.1:5000/estoque{id}

# Visualizar o Histórico das ações efetuadas no cadastro

http://127.0.0.1:5000/historico


--- instalar pip:

pip install sqlalchemy
pip install flask

