from domain.Endereco import Endereco
from domain.Departamento import Departamento
from domain.Usuario import Usuario
from domain.Chamado import Chamado
from gerarDadosCSV import gerarArquivos

def obterUsuariosPorDepartamento():
  todosDepartamentos.sort(key=lambda departamento: departamento.nome)
  for departamento in todosDepartamentos:
    print(departamento.nome)
    usuariosEncontrados = []
    for usuario in todosUsuarios:
      if usuario.departamento == departamento.id:
        usuariosEncontrados.append(usuario)  
    usuariosEncontrados.sort(key=lambda usuario: usuario.nome)
    for usuario in usuariosEncontrados:
      print('  - ' + usuario.nome)
    print('')

def obterChamadoPorPrioridade():
  chamadosPrioridadeAlta = []
  chamadosPrioridadeMedia = []
  chamadosPrioridadeBaixa = []
  for chamado in todosChamados:
    if chamado.prioridade == 'Alta':
      chamadosPrioridadeAlta.append(chamado)
    elif chamado.prioridade == 'Média':
      chamadosPrioridadeMedia.append(chamado)
    elif chamado.prioridade == 'Baixa':
      chamadosPrioridadeBaixa.append(chamado)
  print("Prioridade Alta:")
  for chamado in chamadosPrioridadeAlta:
    print(f' - Chamado número {chamado.id}: {chamado.titulo}')
  print('')
  print("Prioridade Média:")
  for chamado in chamadosPrioridadeMedia:
    print(f' - Chamado número {chamado.id}: {chamado.titulo}')
  print('')
  print("Prioridade Baixa:")
  for chamado in chamadosPrioridadeBaixa:
    print(f' - Chamado número {chamado.id}: {chamado.titulo}')
  print('')

def obterUsuarioComMaisChamados():
  chamadosUsuario = {}
  for usuario in todosUsuarios:
    listaChamados = []
    for chamado in todosChamados:
      if chamado.solicitante == usuario.id:
        listaChamados.append(chamado)
    chamadosUsuario[usuario.nome] = len(listaChamados)
  for usuario in chamadosUsuario:
    if chamadosUsuario[usuario] == max(chamadosUsuario.values()):
      print(f'O usuário com mais chamados é {usuario} com {chamadosUsuario[usuario]} chamados')

def obterChamadosPorDepartamento():
  chamadosUsuario = {}
  chamadosDepartamento = {}
  
  for usuario in todosUsuarios:
    listaChamados = []
    for chamado in todosChamados:
      if chamado.solicitante == usuario.id:
        listaChamados.append(chamado)
    chamadosUsuario[usuario] = listaChamados
    
  for usuario in chamadosUsuario:
    departamentoUsuario = None
    for departamento in todosDepartamentos:
      if usuario.departamento == departamento.id:
        departamentoUsuario = departamento
        break
    for chamado in chamadosUsuario[usuario]:
      chamadosDepartamento[departamentoUsuario] = chamadosDepartamento.get(departamentoUsuario, []) + [chamado]

  for departamento in chamadosDepartamento:
    print(f'Chamados do departamento {departamento.nome}:')
    for chamado in chamadosDepartamento[departamento]:
      print(f' - Chamado número {chamado.id}: {chamado.titulo}, status: {chamado.status}, prioridade: {chamado.prioridade}, solicitante: {getKeyByValue(chamadosUsuario,chamado)}')
    print(f'Total de chamados: {len(chamadosDepartamento[departamento])}')
    print('')

def getKeyByValue(dict, value) -> Usuario:
  for key in dict:
    if value in dict[key]:
      return key.nome

gerarArquivos()
todosUsuarios = Usuario.getFromCSV()
todosChamados = Chamado.getFromCSV()
todosDepartamentos = Departamento.getFromCSV()
todosEnderecos = Endereco.getFromCSV()

print('*******Usuários por departamento*******')
print('')
obterUsuariosPorDepartamento()
print('')
print('*******Chamados por prioridade*******')
print('')
obterChamadoPorPrioridade()
print('')
print('*******Usuário com mais chamados*******')
print('')
obterUsuarioComMaisChamados()
print('')
print('*******Chamados por departamento*******')
print('')
obterChamadosPorDepartamento()