import csv

class Chamado:
  def __init__(self, id, titulo, descricao, status, dataAbertura, dataConclusao, solicitante, responsavel, prioridade):
    self.id = id
    self.titulo = titulo
    self.descricao = descricao
    self.status = status
    self.dataAbertura = dataAbertura
    self.dataConclusao = dataConclusao
    self.solicitante = solicitante
    self.responsavel = responsavel
    self.prioridade = prioridade

  @staticmethod
  def getFromCSV():
    todosChamados = []
    with open('./Chamados.csv', 'r', encoding='utf-8') as chamadosCSV:
      reader = csv.DictReader(chamadosCSV, delimiter=',')
      for linha in reader:
        chamado = Chamado(
          linha['id'],
          linha['titulo'],
          linha['descricao'],
          linha['status'],
          linha['dataAbertura'],
          linha['dataConclusao'],
          linha['solicitante'],
          linha['responsavel'],
          linha['prioridade']
        )
        todosChamados.append(chamado)
    return todosChamados