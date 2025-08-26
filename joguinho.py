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


        self.p3borda = parede(0, 0, 5, 100)
        self.p4borda = parede(0, 0,80, 5)
        self.p5borda = parede(0, 95, 80, 5)
        self.p6borda = parede(75, 0, 5, 100)

        self.obs1 = parede (80*1/3, 0, 5, 70)
        self.obs2 = parede (80*2/3, 30, 5, 70)

        pyxel.init(80, 100, title="Labirinto", fps=60)
        pyxel.run(self.update, self.draw)

    def colisao( self, circulo, retangulo):
        c_dir = circulo.x + circulo.raio
        c_esq = circulo.x - circulo.raio
        c_topo = circulo.y - circulo.raio
        c_base = circulo.y + circulo.raio

        r_dir = retangulo.x + retangulo.largura
        r_esq = retangulo.x
        r_topo = retangulo.y
        r_baixo = retangulo.y + retangulo.altura

        if (c_dir >= r_esq and
            c_esq <= r_dir and
            c_base >= r_topo and
            c_topo <= r_baixo):
            return True
        else:
            return False

    def update(self):
        #movimento do circulo
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

        #colisão com as paredes
        if self.colisao(self.c, self.obs1) or self.colisao(self.c, self.obs2):
            self.c.move(-dx, -dy)

    def draw(self):
        pyxel.cls(0)
        self.c.desenha()
        self.p3borda.desenha()
        self.p4borda.desenha()
        self.p5borda.desenha()
        self.p6borda.desenha()

        self.obs1.desenha()
        self.obs2.desenha()

labirinto()