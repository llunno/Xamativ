import csv

class Departamento:
  def __init__(self, id, nome, descricao, local, telefone, email):
    self.id = id
    self.nome = nome
    self.descricao = descricao
    self.local = local
    self.telefone = telefone
    self.email = email

  @staticmethod
  def getFromCSV():
    todosDepartamentos = []
    with open('./Departamentos.csv', 'r', encoding='utf-8') as departamentosCSV:
      reader = csv.DictReader(departamentosCSV, delimiter=',')
      for linha in reader:
        departamento = Departamento(
          linha['id'],
          linha['nome'],
          linha['descricao'],
          linha['local'],
          linha['telefone'],
          linha['email']
        )
        todosDepartamentos.append(departamento)
    return todosDepartamentos