import pyxel

class circulo:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self.raio = 3
        self.cor = 7

    def desenha(self):
        pyxel.circ(self.x, self.y, self.raio, self.cor)

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

    def update(self):
        #movimento do circulo
        if pyxel.btn(pyxel.KEY_UP):
            self.c.y -= 0.5
        if pyxel.btn(pyxel.KEY_DOWN):
            self.c.y += 0.5
        if pyxel.btn(pyxel.KEY_LEFT):
            self.c.x -= 0.5
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.c.x += 0.5
        #colisão com as paredes
        

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