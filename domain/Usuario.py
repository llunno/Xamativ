import csv

class Usuario:
  def __init__(self, id, nome, dataNascimento, matricula, email, cargo, endereco, telefone, departamento):
    self.id = id
    self.nome = nome
    self.dataNascimento = dataNascimento
    self.matricula = matricula
    self.email = email
    self.cargo = cargo
    self.endereco = endereco
    self.telefone = telefone
    self.departamento = departamento

  @staticmethod
  def getFromCSV():
    todosUsuarios = []
    with open('./Usuarios.csv', 'r', encoding='utf-8') as usuarioCSV:
      reader = csv.DictReader(usuarioCSV, delimiter=',')
      for linha in reader:
        id = linha['id']
        nome = linha['nome']
        dataNascimento = linha['dataNascimento']
        matricula = linha['matricula']
        email = linha['email']
        cargo = linha['cargo']
        endereco = linha['endereco']
        telefone = linha['telefone']
        departamento = linha['departamento']
        todosUsuarios.append(
          Usuario(id, nome, dataNascimento, matricula, email, cargo, endereco, telefone, departamento)
        )
      return todosUsuarios