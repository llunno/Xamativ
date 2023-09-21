import csv
import sqlite3

def getFromCSVAtivosFornecedores():
  listaRelacionamentos = []
  with open('Fornecedores_Ativos.csv', 'r',
            encoding='utf-8') as relacionamentosCSV:
    reader = csv.reader(relacionamentosCSV, delimiter=',')
    for linha in reader:
      listaRelacionamentos.append(linha)
  listaRelacionamentos.pop(0)
  return listaRelacionamentos


def gerarArquivosCSV():

  arquivos = [
    'Usuarios.csv', 'Chamados.csv', 'Departamentos.csv', 'Enderecos.csv',
    'Ativos.csv', 'Fornecedores.csv', 'Fornecedores_Ativos.csv'
  ]

  with open(arquivos[0], 'w', newline='', encoding='utf-8') as usuarioCSV, \
  open(arquivos[1],'w', newline='', encoding='utf-8') as chamadosCSV, \
  open(arquivos[2],'w', newline='', encoding='utf-8') as departamentosCSV, \
  open(arquivos[3], 'w', newline='', encoding='utf-8') as enderecosCSV, \
  open(arquivos[4], 'w', newline='', encoding='utf-8') as ativosCSV, \
  open(arquivos[5], 'w', newline='', encoding='utf-8') as fornecedoresCSV, \
  open(arquivos[6], 'w', newline='', encoding='utf-8') as fornecedoresAtivosCSV:

    # Escreve no arquivo de Usuarios
    writer = csv.writer(usuarioCSV)
    usuarios = [
      [
        'id', 'nome', 'dataNascimento', 'matricula', 'email', 'cargo',
        'endereco', 'telefone', 'departamento'
      ],
      [
        1, 'João Silva', '1990-03-15', '12345', 'joao.silva@example.com',
        'Analista de Vendas', 1, 987654321, 5
      ],
      [
        2, 'Maria Souza', '1985-08-10', '54321', 'maria.souza@example.com',
        'Gerente de Recursos Humanos', 2, 876543210, 5
      ],
      [
        3, 'Pedro Santos', '1992-11-25', '98765', 'pedro.santos@example.com',
        'Desenvolvedor de Software', 3, 765432109, 2
      ],
      [
        4, 'Ana Oliveira', '1988-05-03', '23456', 'ana.oliveira@example.com',
        'Analista de Marketing', 4, 654321098, 1
      ],
      [
        5, 'Luiz Pereira', '1995-02-18', '67890', 'luiz.pereira@example.com',
        'Engenheiro de Produção', 5, 543210987, 3
      ],
      [
        6, 'Fernanda Rodrigues', '1987-07-22', '43210',
        'fernanda.rodrigues@example.com', 'Contadora', 6, 432109876, 4
      ],
      [
        7, 'Ricardo Almeida', '1991-09-09', '87654',
        'ricardo.almeida@example.com', 'Analista Financeiro', 7, 321098765, 2
      ],
      [
        8, 'Camila Lima', '1984-12-07', '13579', 'camila.lima@example.com',
        'Designer Gráfico', 8, 210987654, 7
      ],
      [
        9, 'André Castro', '1993-06-30', '24680', 'andre.castro@example.com',
        'Engenheiro de Software', 9, 109876543, 6
      ],
      [
        10, 'Juliana Fernandes', '1989-04-12', '98765',
        'juliana.fernandes@example.com', 'Analista de Recursos Humanos', 10,
        987654321, 6
      ]
    ]
    writer.writerows(usuarios)

    # Escreve no arquivo de chamados
    writer = csv.writer(chamadosCSV)
    chamados = [[
      'id', 'titulo', 'descricao', 'status', 'dataAbertura', 'dataConclusao',
      'solicitante', 'responsavel', 'prioridade'
    ],
                [
                  1, 'Problema na Impressora',
                  'A impressora não está funcionando', 'Aberto', '2023-03-10',
                  '-', 2, 4, 'Alta'
                ],
                [
                  2, 'Erro no Sistema',
                  'O sistema está apresentando um erro ao salvar dados',
                  'Em andamento', '2023-03-12', '-', 2, 5, 'Média'
                ],
                [
                  3, 'Troca de Lâmpada', 'A lâmpada do corredor está queimada',
                  'Fechado', '2023-08-14', '2023-08-15', 7, 6, 'Baixa'
                ],
                [
                  4, 'Solicitação de Acesso',
                  'Solicito acesso ao novo sistema de RH', 'Aberto',
                  '2023-08-15', '-', 2, 8, 'Alta'
                ],
                [
                  5, 'Internet Lenta',
                  'A conexão com a internet está muito lenta', 'Em andamento',
                  '2023-08-16', '-', 1, 9, 'Baixa'
                ],
                [
                  6, 'Atualização de Software',
                  'Solicito atualização do software de contabilidade',
                  'Aberto', '2023-03-17', '-', 5, 2, 'Média'
                ],
                [
                  7, 'Instalação de Software',
                  'Preciso que seja instalado o software de edição de imagens',
                  'Fechado', '2023-08-18', '2023-08-20', 3, 7, 'Baixa'
                ],
                [
                  8, 'Configuração de Email',
                  'Necessito de ajuda para configurar meu email corporativo',
                  'Aberto', '2023-03-19', '-', 8, 10, 'Média'
                ],
                [
                  9, 'Troca de Teclado',
                  'O teclado do meu computador está com teclas travando',
                  'Em andamento', '2023-08-20', '-', 4, 1, 'Baixa'
                ],
                [
                  10, 'Backup de Dados',
                  'Preciso realizar um backup dos meus arquivos importantes',
                  'Fechado', '2023-08-21', '2023-08-22', 6, 3, 'Alta'
                ]]
    writer.writerows(chamados)

    # Escreve no arquivo de departamentos
    writer = csv.writer(departamentosCSV)
    departamentos = [
      ['id', 'nome', 'descricao', 'local', 'telefone', 'email'],
      [
        1, 'Recursos Humanos',
        'Responsável pela gestão de pessoal e contratações',
        'Andar 2, Sala 201', 1234567890, 'rh@empresa.com'
      ],
      [
        2, 'TI - Tecnologia da Informação',
        'Responsável pela infraestrutura e sistemas de tecnologia',
        'Andar 3, Sala 301', 2345678901, 'ti@empresa.com'
      ],
      [
        3, 'Marketing', 'Responsável pela promoção e divulgação da empresa',
        'Andar 2, Sala 205', 3456789012, 'marketing@empresa.com'
      ],
      [
        4, 'Financeiro',
        'Responsável pelo controle financeiro e contabilidade',
        'Andar 4, Sala 401', 4567890123, 'financeiro@empresa.com'
      ],
      [
        5, 'Produção', 'Responsável pela fabricação e produção de produtos',
        'Andar 1, Sala 101', 5678901234, 'producao@empresa.com'
      ],
      [
        6, 'Atendimento ao Cliente',
        'Responsável pelo atendimento e suporte aos clientes',
        'Andar 3, Sala 302', 6789012345, 'atendimento@empresa.com'
      ],
      [
        7, 'Administração',
        'Responsável pela gestão e administração geral da empresa',
        'Andar 1, Sala 102', 1234567890, 'administracao@empresa.com'
      ]
    ]
    writer.writerows(departamentos)

    # Escreve no arquivo de enderecos
    writer = csv.writer(enderecosCSV)
    enderecos = [[
      'id', 'numero', 'rua', 'bairro', 'cidade', 'estado', 'referencia', 'CEP'
    ],
                 [
                   1, 123, 'Rua das Flores', 'Centro', 'São Paulo', 'SP',
                   'Próximo à Praça Principal', 12345678
                 ],
                 [
                   2, 456, 'Avenida das Árvores', 'Bairro Novo',
                   'Rio de Janeiro', 'RJ', 'Ao lado do Supermercado XYZ',
                   23456789
                 ],
                 [
                   3, 789, 'Rua das Montanhas', 'Alto da Colina',
                   'Belo Horizonte', 'MG', 'Perto do Parque Municipal',
                   34567890
                 ],
                 [
                   4, 101, 'Rua dos Ventos', 'Vila Serena', 'Curitiba', 'PR',
                   'Em frente à Escola ABC', 45678901
                 ],
                 [
                   5, 202, 'Avenida do Rio', 'Beira-Mar', 'Salvador', 'BA',
                   'Próximo à Praia Principal', 56789012
                 ],
                 [
                   6, 303, 'Rua das Estrelas', 'Céu Azul', 'Fortaleza', 'CE',
                   'No final da Rua da Lua', 67890123
                 ],
                 [
                   7, 404, 'Avenida dos Jardins', 'Jardim Florido', 'Recife',
                   'PE', 'Junto ao Parque das Flores', 78901234
                 ],
                 [
                   8, 505, 'Rua da Paz', 'Bairro Tranquilo', 'Brasília', 'DF',
                   'Perto do Lago Sereno', 89012345
                 ],
                 [
                   9, 606, 'Avenida das Colinas', 'Morro Alto', 'Porto Alegre',
                   'RS', 'Em frente à Praça dos Pássaros', 90123456
                 ],
                 [
                   10, 707, 'Rua dos Sonhos', 'Bairro Feliz', 'Manaus', 'AM',
                   'Ao lado do Hospital Esperança', 12345678
                 ],
                 [
                   11, 789, 'Avenida das Palmeiras', 'Jardim das Flores',
                   'Campinas', 'SP', 'Próximo ao Parque Central', 45678901
                 ],
                 [
                   12, 345, 'Rua das Pedras', 'Centro Histórico', 'Ouro Preto',
                   'MG', 'Próximo à Igreja Matriz', 67890123
                 ],
                 [
                   13, 567, 'Avenida do Sol', 'Praia Azul', 'Natal', 'RN',
                   'Frente à Praia Principal', 78901234
                 ],
                 [
                   14, 123, 'Rua das Montanhas', 'Alto da Serra',
                   'Campos do Jordão', 'SP', 'Vista panorâmica da cidade',
                   89012345
                 ],
                 [
                   15, 901, 'Avenida da Liberdade', 'Centro', 'Lisboa', 'PT',
                   'Próximo ao Museu Nacional', 90123456
                 ],
                 [
                   16, 234, 'Calle de la Luna', 'Barrio Gótico', 'Barcelona',
                   'ES', 'Cerca de la Catedral', 12345678
                 ],
                 [
                   17, 678, 'Rue de la Seine', 'Quartier Latin', 'Paris', 'FR',
                   'Vue sur la rivière', 23456789
                 ],
                 [
                   18, 456, 'Via Roma', 'Centro Storico', 'Roma', 'IT',
                   'Vicino al Colosseo', 34567890
                 ],
                 [
                   19, 890, 'Bahnhofstraße', 'Mitte', 'Berlim', 'DE',
                   'Nähe des Brandenburger Tors', 45678901
                 ],
                 [
                   20, 123, 'Trafalgar Square', 'Westminster', 'Londres', 'UK',
                   'Close to the National Gallery', 56789012
                 ]]
    writer.writerows(enderecos)

    # Escreve no arquivo de ativos
    writer = csv.writer(ativosCSV)
    ativos = [[
      'id', 'nome', 'descricao', 'status', 'dataModificacao',
      'dataUltimaCompra', 'usuario', 'valor'
    ],
              [
                1, 'Computador Desktop', 'Desktop para uso geral', 'Em uso',
                '2023-08-10', '2022-05-15', 3, 1500.00
              ],
              [
                2, 'Laptop', 'Laptop para trabalho remoto', 'Em uso',
                '2023-08-12', '2023-01-20', 4, 1200.00
              ],
              [
                3, 'Projetor', 'Projetor para apresentações', 'Manutenção',
                '2023-08-14', '2023-03-10', 6, 800.00
              ],
              [
                4, 'Câmera DSLR', 'Câmera profissional para fotografia',
                'Em uso', '2023-08-15', '2023-07-05', 2, 1000.00
              ],
              [
                5, 'Impressora Multifuncional',
                'Impressora, scanner e copiadora', 'Em uso', '2023-08-16',
                '2023-04-28', 7, 300.00
              ],
              [
                6, 'Monitor 27 polegadas', 'Monitor para estação de trabalho',
                'Em uso', '2023-08-17', '2023-06-20', 9, 350.00
              ],
              [
                7, 'Telefone IP', 'Telefone VoIP para chamadas internas',
                'Em uso', '2023-08-18', '2023-02-15', 10, 100.00
              ],
              [
                8, 'Tablet', 'Tablet para demonstrações de produtos',
                'Manutenção', '2023-08-19', '2023-01-10', 1, 250.00
              ],
              [
                9, 'Scanner de Documentos', 'Scanner de alta resolução',
                'Em uso', '2023-08-20', '2023-07-15', 5, 150.00
              ],
              [
                10, 'Servidor', 'Servidor de arquivos e aplicativos', 'Em uso',
                '2023-08-21', '2023-05-05', 8, 2000.00
              ],
              [
                11, 'Computador Desktop', 'Desktop para uso geral', 'Em uso',
                '2023-08-22', '2023-06-01', 7, 1400.00
              ],
              [
                12, 'Telefone IP', 'Telefone VoIP para chamadas internas',
                'Em uso', '2023-08-23', '2023-03-18', 9, 80.00
              ],
              [
                13, 'Laptop', 'Laptop para trabalho remoto', 'Em uso',
                '2023-08-24', '2023-07-10', 2, 1300.00
              ],
              [
                14, 'Computador Desktop', 'Desktop para uso geral', 'Em uso',
                '2023-08-25', '2023-04-22', 6, 1550.00
              ],
              [
                15, 'Telefone IP', 'Telefone VoIP para chamadas internas',
                'Em uso', '2023-08-26', '2023-05-12', 4, 110.00
              ]]
    writer.writerows(ativos)

    # Escreve no arquivo de fornecedores
    writer = csv.writer(fornecedoresCSV)
    fornecedores = [
      ['id', 'nome', 'observacoes', 'telefone', 'endereco'],
      [
        1, 'Tech Components Ltda.',
        'Fornecimento de componentes eletrônicos para diversos setores industriais.',
        '11 1234-5678', 11
      ],
      [
        2, 'ElectroParts S.A.',
        'Especializada na distribuição de peças e partes eletrônicas de alta qualidade.',
        '22 2345-6789', 12
      ],
      [
        3, 'ElecTech Indústria Eletrônica',
        'Produção de componentes eletrônicos avançados para aplicações de alta tecnologia.',
        '33 3456-7890', 13
      ],
      [
        4, 'CircuitSupply Ltda.',
        'Fornecendo soluções completas de circuitos e placas eletrônicas para empresas de todos os tamanhos.',
        '44 4567-8901', 14
      ],
      [
        5, 'ElectroEquipamentos Ltda.',
        'Especializada em equipamentos eletrônicos de precisão para laboratórios e indústrias.',
        '55 5678-9012', 15
      ],
      [
        6, 'TechPartners Eletrônicos',
        'Parceiro confiável para desenvolvimento e fornecimento de componentes eletrônicos sob medida.',
        '66 6789-0123', 16
      ],
      [
        7, 'EletrônicaTech Comércio',
        'Vasta gama de produtos eletrônicos, desde componentes básicos até sistemas completos.',
        '77 7890-1234', 17
      ],
      [
        8, 'ElectroParts Brazil',
        'Distribuição líder no Brasil de peças eletrônicas de alta qualidade para indústrias diversas.',
        '88 8901-2345', 18
      ],
      [
        9, 'ElecSupply S.A.',
        'Fornecimento confiável de componentes eletrônicos essenciais para aplicações industriais e comerciais.',
        '99 9012-3456', 19
      ],
      [
        10, 'TechComponents Brasil',
        'Oferece soluções inovadoras em componentes eletrônicos para empresas de diversos segmentos.',
        '00 0123-4567', 20
      ]
    ]
    writer.writerows(fornecedores)

    # Escreve relacionamentos de fornecedores e ativos
    writer = csv.writer(fornecedoresAtivosCSV)
    fornecedores_ativos = [
      ['id_fornecedor', 'id_ativo'],
      [1, 1],
      [1, 2],
      [2, 3],
      [3, 4],
      [4, 5],
      [5, 6],
      [6, 7],
      [7, 8],
      [8, 9],
      [9, 10],
      [10, 11],
      [3, 2],
      [5, 4],
      [5, 12],
      [6, 13],
      [1, 14],
      [2, 15],
      [1, 15]
    ]
    writer.writerows(fornecedores_ativos)


def gerarTabelasSQL():
  conn = sqlite3.connect('sysChamadosAtivos.db')
  cursor = conn.cursor()

  # Gerar tabela SQL usuários
  drop_table_if_exists = "DROP TABLE IF EXISTS usuarios;"
  
  create_usuarios_table = """
  CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(45),
    dataNascimento DATE,
    matricula TEXT,
    email VARCHAR(45),
    cargo VARCHAR(25),
    endereco INTEGER,
    telefone VARCHAR(25),
    departamento INTEGER
  );
  """
  cursor.execute(drop_table_if_exists)
  cursor.execute(create_usuarios_table)

  # Gerar tabela SQL chamados
  drop_table_if_exists = "DROP TABLE IF EXISTS chamados;"
  
  create_chamados_table = """
  CREATE TABLE IF NOT EXISTS chamados (
    id INTEGER PRIMARY KEY,
    titulo VARCHAR(45),
    descricao TEXT,
    status VARCHAR(25),
    dataAbertura DATE,
    dataConclusao DATE,
    solicitante INTEGER,
    responsavel INTEGER,
    prioridade VARCHAR(10)
  );
  """
  cursor.execute(drop_table_if_exists)
  cursor.execute(create_chamados_table)

  # Gerar tabela SQL departamentos
  drop_table_if_exists = "DROP TABLE IF EXISTS departamentos;"
  
  create_departamentos_table = """
  CREATE TABLE IF NOT EXISTS departamentos (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(45),
    descricao TEXT,
    local VARCHAR(45),
    telefone VARCHAR(25),
    email VARCHAR(45)
  );
  """
  cursor.execute(drop_table_if_exists)
  cursor.execute(create_departamentos_table)

  # Gerar tabela SQL enderecos
  drop_table_if_exists = "DROP TABLE IF EXISTS enderecos;"
  
  create_enderecos_table = """
  CREATE TABLE IF NOT EXISTS enderecos (
    id INTEGER PRIMARY KEY,
    numero INTEGER,
    rua VARCHAR(45),
    bairro VARCHAR(45),
    cidade VARCHAR(25),
    estado VARCHAR(2),
    referencia TEXT,
    CEP INTEGER
  );
  """
  cursor.execute(drop_table_if_exists)
  cursor.execute(create_enderecos_table)

  # Gerar tabela SQL ativos
  drop_table_if_exists = "DROP TABLE IF EXISTS ativos;"
  
  create_ativos_table = """
  CREATE TABLE IF NOT EXISTS ativos (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(45),
    descricao TEXT,
    status VARCHAR(25),
    dataModificacao DATE,
    dataUltimaCompra DATE,
    usuario INTEGER,
    valor DOUBLE
  );
  """
  cursor.execute(drop_table_if_exists)
  cursor.execute(create_ativos_table)

  # Gerar tabela SQL fornecedores
  drop_table_if_exists = "DROP TABLE IF EXISTS fornecedores;"
  
  create_fornecedores_table = """
  CREATE TABLE IF NOT EXISTS fornecedores (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(45),
    observacoes TEXT,
    telefone VARCHAR(25),
    endereco INTEGER
  );
  """
  cursor.execute(drop_table_if_exists)
  cursor.execute(create_fornecedores_table)

  # Gerar tabela SQL ativos_fornecedores
  drop_table_if_exists = "DROP TABLE IF EXISTS ativos_fornecedores;"
  
  create_ativosFornecedores_table = """
  CREATE TABLE IF NOT EXISTS ativos_fornecedores (
    id_fornecedor INTEGER,
    id_ativo INTEGER
  );
  """
  cursor.execute(drop_table_if_exists)
  cursor.execute(create_ativosFornecedores_table)

  conn.commit()
  conn.close()


def insertObjectsInSQLTables(todosUsuarios, todosChamados, todosDepartamentos,
                             todosEnderecos, todosFornecedores, todosAtivos):
  conn = sqlite3.connect('sysChamadosAtivos.db')
  cursor = conn.cursor()

  # insert usuarios
  insert_usuarios_sql = "INSERT INTO usuarios(id, nome, dataNascimento, matricula, email, cargo, endereco, telefone, departamento) VALUES (?,?,?,?,?,?,?,?,?)"

  for usuario in todosUsuarios:
    cursor.execute(insert_usuarios_sql, (usuario.id, usuario.nome, usuario.dataNascimento, usuario.matricula, usuario.email, usuario.cargo, usuario.endereco, usuario.telefone, usuario.departamento))

  # insert chamados
  insert_chamados_sql = "INSERT INTO chamados(id, titulo, descricao, status, dataAbertura, dataConclusao, solicitante, responsavel, prioridade) VALUES (?,?,?,?,?,?,?,?,?)"

  for chamado in todosChamados:
    cursor.execute(
      insert_chamados_sql,
      (chamado.id, chamado.titulo, chamado.descricao, chamado.status,
       chamado.dataAbertura, chamado.dataConclusao, chamado.solicitante,
       chamado.responsavel, chamado.prioridade))

  # insert departamentos
  insert_departamentos_sql = "INSERT INTO departamentos(id, nome, descricao, local, telefone, email) VALUES (?,?,?,?,?,?)"

  for departamento in todosDepartamentos:
    cursor.execute(
      insert_departamentos_sql,
      (departamento.id, departamento.nome, departamento.descricao,
       departamento.local, departamento.telefone, departamento.email))

  # insert enderecos
  insert_enderecos_sql = "INSERT INTO enderecos(id, numero, rua, bairro, cidade, estado, referencia, CEP) VALUES (?,?,?,?,?,?,?,?)"

  for endereco in todosEnderecos:
    cursor.execute(
      insert_enderecos_sql,
      (endereco.id, endereco.numero, endereco.rua, endereco.bairro,
       endereco.cidade, endereco.estado, endereco.referencia, endereco.CEP))

  # insert ativos
  insert_ativos_sql = "INSERT INTO ativos(id, nome, descricao, status, dataModificacao, dataUltimaCompra, usuario, valor) VALUES (?,?,?,?,?,?,?,?)"

  for ativo in todosAtivos:
    cursor.execute(insert_ativos_sql,
                   (ativo.id, ativo.nome, ativo.descricao, ativo.status,
                    ativo.dataModificacao, ativo.dataUltimaCompra,
                    ativo.usuario, ativo.valor))

  # insert fornecedores
  insert_fornecedores_sql = "INSERT INTO fornecedores(id, nome, observacoes, telefone, endereco) VALUES (?,?,?,?,?)"

  for fornecedor in todosFornecedores:
    cursor.execute(insert_fornecedores_sql,
                   (fornecedor.id, fornecedor.nome, fornecedor.observacoes,
                    fornecedor.telefone, fornecedor.endereco))

  # insert ativos_fornecedores
  ativosFornecedores = getFromCSVAtivosFornecedores()

  insert_ativosFornecedores_sql = "INSERT INTO ativos_fornecedores(id_fornecedor, id_ativo) VALUES (?,?)"

  for ativoFornecedor in ativosFornecedores:
    cursor.execute(insert_ativosFornecedores_sql, ativoFornecedor)

  conn.commit()
  conn.close()


def getUsuarios_Departamentos():
  conn = sqlite3.connect('sysChamadosAtivos.db')
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()

  # Criar relacionamento entre usuario e departamento
  join_usuarios_departamentos = """
  SELECT u.id, u.nome, u.dataNascimento, u.matricula, u.email, u.cargo, u.endereco, u.telefone, u.departamento,d.id as idDepartamento, d.nome as nomeDepartamento, d.descricao as descricaoDepartamento, d.local as localDepartamento, d.telefone as telefoneDepartamento, d.email as emailDepartamento
  FROM usuarios u
  LEFT JOIN departamentos d ON u.departamento = d.id
  """
  cursor.execute(join_usuarios_departamentos)
  results = cursor.fetchall()

  conn.commit()
  conn.close()

  return results


def getAtivos_Fornecedores():
  conn = sqlite3.connect('sysChamadosAtivos.db')
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()

  # Criar relacionamento entre ativo e fornecedor
  join_ativos_fornecedores = """
  SELECT a.id, a.nome, a.descricao, a.status, a.dataModificacao, a.dataUltimaCompra, a.usuario, a.valor, f.id AS idFornecedor, f.nome AS nomeFornecedor, f.observacoes, f.telefone, f.endereco
  FROM ativos a
  LEFT JOIN ativos_fornecedores af ON a.id = af.id_ativo
  LEFT JOIN fornecedores f ON af.id_fornecedor = f.id
  """

  cursor.execute(join_ativos_fornecedores)
  results = cursor.fetchall()

  conn.commit()
  conn.close()

  return results


def getEnderecos():
  conn = sqlite3.connect('sysChamadosAtivos.db')
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()

  get_enderecos = """
  SELECT e.id, e.numero, e.rua, e.bairro, e.cidade, e.estado, e.referencia, e.CEP
  FROM enderecos e
  """

  cursor.execute(get_enderecos)
  results = cursor.fetchall()

  conn.commit()
  conn.close()

  return results


def getChamados():

  conn = sqlite3.connect('sysChamadosAtivos.db')
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()

  get_chamados = """
  SELECT c.id, c.titulo, c.descricao, c.status, c.dataAbertura, c.dataConclusao, c.solicitante, c.responsavel, c.prioridade
  FROM chamados c
  """

  cursor.execute(get_chamados)
  results = cursor.fetchall()

  conn.commit()
  conn.close()

  return results

def getAtivos():

  conn = sqlite3.connect('sysChamadosAtivos.db')
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()

  get_chamados = """
  SELECT a.id, a.nome, a.descricao, a.status, a.dataModificacao, a.dataUltimaCompra, a.usuario, a.valor
  FROM ativos a
  """

  cursor.execute(get_chamados)
  results = cursor.fetchall()

  conn.commit()
  conn.close()

  return results

def getFornecedores():

  conn = sqlite3.connect('sysChamadosAtivos.db')
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()

  get_chamados = """
  SELECT f.id, f.nome, f.observacoes, f.telefone, f.endereco
  FROM fornecedores f
  """

  cursor.execute(get_chamados)
  results = cursor.fetchall()

  conn.commit()
  conn.close()

  return results

def getAtivosFornecedoresDetatched():

  conn = sqlite3.connect('sysChamadosAtivos.db')
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()

  get_chamados = """
  SELECT af.id_ativo, af.id_fornecedor
  FROM ativos_fornecedores af
  """

  cursor.execute(get_chamados)
  results = cursor.fetchall()

  conn.commit()
  conn.close()

  return results