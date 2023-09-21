import pygame
import psutil

# Cores a serem utilizadas:
cinza = (169,169,169)
azul = (0, 0, 255)
branco = (255,255,255)
preto = (0,0,0)

# Para exibir o console basta chamar esta função com pygame corretamente configurado
def inicializarMostradorMemoriaPyGame():
  
  # Iniciando a janela principal
  largura_tela = 800
  altura_tela = 600
  tela = pygame.display.set_mode((largura_tela, altura_tela)) # Definindo tamanho da tela
  pygame.display.set_caption("Informações de memória do computador") # Definindo titulo da janela
  pygame.display.init() # Inicialização da exibição
  pygame.font.init() # Inicialização do texto
  font = pygame.font.Font(None, 24) # Configurações da fonte
  
  # Cria relogio e contador
  clock = pygame.time.Clock() # Relógio para definir o FPS de atualização
  cont = 60 # Inicialização do contador
  
  end = False
  
  while not end:
    for event in pygame.event.get(): # Para cada evento no pygame
      if event.type == pygame.QUIT: # Se o evento for uma saída ou pausa de utilização
        end = True # Avisa ao sistema que o processamento terminou
    # Fazer a atualizacao a cada segundo:
    if cont == 60:
      mostra_uso_memoria_pygame(largura_tela,tela,font) # Chama a função que mostra o uso de memória
      cont = 0
    # Atualiza o desenho na tela
    pygame.display.update()
    # 60 frames por segundo
    clock.tick(60)
    cont = cont + 1
  # Finaliza a janela
  pygame.display.quit()

def mostra_uso_memoria_pygame(largura_tela,tela,font):
  mem = psutil.virtual_memory() # Obtem o total de memória virtual disponível no sistema
  larg = largura_tela - 40 # Define uma medida de largura
  pygame.draw.rect(tela, cinza, (20, 170, larg, 50)) # desenha um retângulo cinza com as medidas descritas
  larg = larg*mem.percent/100
  pygame.draw.rect(tela, azul, (20, 170, larg, 50)) # Desenha um retângulo azul correspondendo a barra de utilização da memória
  total = round(mem.total/(1024*1024),2) # Arredonda o total da memória para megabytes
  used = round(mem.used/(1024*1024),2) # Arredonda o uso da memória para megabytes
  texto_barra = f"Uso de Memória: {str(used)} MB / {str(total)} MB" # Define o texto que será exibido acima da barra de utilização
  text = font.render(texto_barra, 1, branco) # Configura como o texto será renderizado
  text_x = 20
  text_y = 120
  tela.fill(preto, (text_x,text_y, text.get_width() + 400, text.get_height())) # Apaga o texto anterior antes de exibir o novo
  tela.blit(text, (text_x, text_y)) # Define o posicionamento do texto na tela

def mostrarMemoria():
  mem = psutil.virtual_memory()
  memTotalMB = round(mem.total/(1024*1024),2)
  memUsedMB = round(mem.used/(1024*1024),2)

  string = f"Memória utilizada: {str(memUsedMB)} MB / {str(memTotalMB)} MB"

  return string