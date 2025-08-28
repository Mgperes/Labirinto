import pyxel

class personagem:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self.largura = 14
        self.altura = 18
        self.x_mem = 0
        self.contX = 0
        self.y_mem = 0
        self.contY = 0

    def move(self, dx, dy):
        self.x_mem = self.contX * self.largura
        self.contX = (self.contX + 1) % 4

        if dy > 0: # indo para baixo, linha 0
            self.contY = 0

        if dy < 0: # indo para cima, linha 1
            self.contY = 1

        if dx > 0: # indo para direita, linha 2
            self.contY = 3

        if dx < 0: # indo para esquerda, linha 3
            self.contY = 2

        self.y_mem = self.contY * self.altura
            

        self.x += dx
        self.y += dy

    def desenha(self):
        #----- Desenha o personagem usando a imagem carregada------
        #---------  x    ,  y   , img, x da mem, y da mem, largura, altura, cor de transparência -----------
        pyxel.blt(self.x, self.y, 0, self.x_mem, self.y_mem, self.largura, self.altura, 7)  



class parede:
    def __init__ (self,x,y,largura,altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = 9

    def desenha(self):
        pyxel.rect(self.x, self.y, self.largura, self.altura, self.cor)

class labirinto:
    def __init__ (self):
        self.c = personagem(10,10)
        # ----- largura das paredes -----
        self.paredes = []
        # ----- Cria as paredes para desviar ------
        borda_esq = parede(0, 0, 5, 100)
        self.paredes.append(borda_esq)
        borda_top = parede(0, 0,80, 5)
        self.paredes.append(borda_top)
        borda_base = parede(0, 95, 80, 5)
        self.paredes.append(borda_base)
        borda_dir = parede(75, 0, 5, 100)
        self.paredes.append(borda_dir)

        # ---- Cria Obstáculos ------
        obs1 = parede (80*1/3, 0, 5, 70)
        self.paredes.append(obs1)
        obs2 = parede (80*2/3, 30, 5, 70)
        self.paredes.append(obs2)

        pyxel.init(80, 100, title="Labirinto", fps=10)

        #  ----- carregar imagens -----
        pyxel.image(0).load(0,0,"personagem_56x72.png")


        # ----- Ultima linha -----
        pyxel.run(self.update, self.draw)

    # ----- Calcula a colisão dos objetos -------
    def colisao(self, r1, r2):

        # Largura das paredes = 5

        # Limites do personagem
        r1_dir = r1.x + r1.largura
        r1_esq = r1.x 
        r1_base = r1.y + r1.altura
        r1_topo = r1.y
        

        # Limites do retângulo
        r2_esq = r2.x
        r2_dir = r2.x + r2.largura
        r2_top = r2.y
        r2_base = r2.y + r2.altura

        
        if (r1_dir >= r2_esq and
            r1_esq <= r2_dir and
            r1_base >= r2_top and
            r1_topo <= r2_base):
            return True
        return False

    def update(self):
        # movimento do circulo
        dx = 0
        dy = 0

        if pyxel.btn(pyxel.KEY_UP):
            dy -= 4
        if pyxel.btn(pyxel.KEY_DOWN):
            dy += 4
        if pyxel.btn(pyxel.KEY_LEFT):
            dx -= 4
        if pyxel.btn(pyxel.KEY_RIGHT):
            dx += 4


        if dx != 0 or dy != 0:
            self.c.move(dx, dy)

            for parede in self.paredes:
                if self.colisao(self.c, parede):
                 # Se houver colisão, reverte o movimento
                    self.c.move(-dx, -dy)
                    break

    def draw(self):
        pyxel.cls(0)
        self.c.desenha()
        
        for parede in self.paredes:
            parede.desenha()

labirinto()