import csv

class Fornecedor:
  def __init__(self, id, nome, observacoes, telefone, endereco):
    self.id = id
    self.nome = nome
    self.observacoes = observacoes
    self.telefone = telefone
    self.endereco = endereco

  @staticmethod
  def getFromCSV():
    todosFornecedores = []
    with open('./Fornecedores.csv', 'r', encoding='utf-8') as fornecedoresCSV:
      reader = csv.DictReader(fornecedoresCSV, delimiter=',')
      for linha in reader:
        fornecedor = Fornecedor(
          linha['id'],
          linha['nome'],
          linha['observacoes'],
          linha['telefone'],
          linha['endereco']
        )
        todosFornecedores.append(fornecedor)
    return todosFornecedores