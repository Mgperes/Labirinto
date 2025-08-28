import pyxel

class circulo:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self.raio = 3
        self.cor = 7

    def desenha(self):
        pyxel.circ(self.x, self.y, self.raio, self.cor)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class parede:
    def __init__ (self,x,y,largura,altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = 8

    def desenha(self):
        pyxel.rect(self.x, self.y, self.largura, self.altura, self.cor)

class labirinto:
    def __init__ (self):
        self.c = circulo(10,10)
        #largura das paredes
        self.paredes = []
        # Cria as paredes para desviar
        borda_esq = parede(0, 0, 5, 100)
        self.paredes.append(borda_esq)
        borda_top = parede(0, 0,80, 5)
        self.paredes.append(borda_top)
        borda_base = parede(0, 95, 80, 5)
        self.paredes.append(borda_base)
        borda_dir = parede(75, 0, 5, 100)
        self.paredes.append(borda_dir)

        # cria Obstáculos
        obs1 = parede (80*1/3, 0, 5, 70)
        self.paredes.append(obs1)
        obs2 = parede (80*2/3, 30, 5, 70)
        self.paredes.append(obs2)

        pyxel.init(80, 100, title="Labirinto", fps=60)
        # carregar imagens
        pyxel.image(0).load(0,0,"cat_16x16.png")


        # Ultima linha
        pyxel.run(self.update, self.draw)

    # Calcula a colisão dos objetos
    def colisao(self, circulo, retangulo):
        # Limites do círculo
        c_dir = circulo.x + circulo.raio
        c_esq = circulo.x - circulo.raio
        c_topo = circulo.y - circulo.raio
        c_base = circulo.y + circulo.raio

        # Limites do retângulo
        r_dir = retangulo.x + retangulo.largura
        r_esq = retangulo.x
        r_top = retangulo.y
        r_base = retangulo.y + retangulo.altura

        
        if ( c_dir >= r_esq and c_esq <= r_dir and c_base >= r_top and c_topo <= r_base):
            return True
        return False

    def update(self):
        # movimento do circulo
        dx = 0
        dy = 0

        if pyxel.btn(pyxel.KEY_UP):
            dy -= 0.5
        if pyxel.btn(pyxel.KEY_DOWN):
            dy += 0.5
        if pyxel.btn(pyxel.KEY_LEFT):
            dx -= 0.5
        if pyxel.btn(pyxel.KEY_RIGHT):
            dx += 0.5

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