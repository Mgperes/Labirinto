import pyxel

class Jogo:
    def __init__(self):
        pyxel.init(160, 120, title="Jogo Multi-Fase")
        self.fase_atual = 1
        self.total_fases = 3
        self.jogador_x = 80
        self.jogador_y = 60
        self.iniciar_fase(self.fase_atual)
        
        pyxel.run(self.update, self.draw)
    
    def iniciar_fase(self, numero_fase):
        """Inicializa os elementos específicos de cada fase"""
        self.fase_atual = numero_fase
        self.jogador_x = 80
        self.jogador_y = 60
        
        # Configurações específicas por fase
        if numero_fase == 1:
            self.obstaculos = [(40, 40), (100, 80)]
            self.meta = (140, 100)
            self.cor_fundo = 1  # Azul escuro
        elif numero_fase == 2:
            self.obstaculos = [(30, 30), (60, 60), (90, 90)]
            self.meta = (20, 20)
            self.cor_fundo = 3  # Roxo
        elif numero_fase == 3:
            self.obstaculos = [(20, 40), (60, 20), (100, 60), (140, 40)]
            self.meta = (80, 100)
            self.cor_fundo = 5  # Verde
    
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.jogador_x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.jogador_x += 2
        if pyxel.btn(pyxel.KEY_UP):
            self.jogador_y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.jogador_y += 2
        
        # Verificar colisão com obstáculos
        for obs_x, obs_y in self.obstaculos:
            if (abs(self.jogador_x - obs_x) < 8 and 
                abs(self.jogador_y - obs_y) < 8):
                self.jogador_x = 80
                self.jogador_y = 60
        
        # Verificar se alcançou a meta
        meta_x, meta_y = self.meta
        if (abs(self.jogador_x - meta_x) < 8 and 
            abs(self.jogador_y - meta_y) < 8):
            if self.fase_atual < self.total_fases:
                self.fase_atual += 1
                self.iniciar_fase(self.fase_atual)
            else:
                # Jogo completo
                print("Parabéns! Você completou todas as fases!")
                pyxel.quit()
    
    def draw(self):
        pyxel.cls(self.cor_fundo)
        
        # Desenhar jogador
        pyxel.circ(self.jogador_x, self.jogador_y, 4, 8)
        
        # Desenhar obstáculos
        for x, y in self.obstaculos:
            pyxel.rect(x-4, y-4, 8, 8, 2)
        
        # Desenhar meta
        meta_x, meta_y = self.meta
        pyxel.circ(meta_x, meta_y, 6, 11)
        
        # Mostrar número da fase
        pyxel.text(5, 5, f"Fase: {self.fase_atual}/{self.total_fases}", 7)

# Iniciar o jogo
Jogo()
