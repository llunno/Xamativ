import csv

class Ativo:
  def __init__(self, id, nome, descricao, status, dataModificacao, dataUltimaCompra,usuario,valor):
    self.id = id
    self.nome = nome
    self.descricao = descricao
    self.status = status
    self.dataModificacao = dataModificacao
    self.dataUltimaCompra = dataUltimaCompra
    self.usuario = usuario
    self.valor = valor

  @staticmethod
  def getFromCSV():
    todosAtivos = []
    with open('./Ativos.csv', 'r', encoding='utf-8') as ativosCSV:
      reader = csv.DictReader(ativosCSV, delimiter=',')
      for linha in reader:
        ativo = Ativo(
          linha['id'],
          linha['nome'],
          linha['descricao'],
          linha['status'],
          linha['dataModificacao'],
          linha['dataUltimaCompra'],
          linha['usuario'],
          linha['valor']
        )
        todosAtivos.append(ativo)
    return todosAtivos