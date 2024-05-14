---
title: Construindo jogos em Python
sub_title: com o Pygame Zero (Aula 2, complemento)
author: Orahcio Felício de Sousa e Jaylson Teixeira
theme:
    name: catppuccin-mocha
    # override:
    #     footer:
    #         style: empty
---

Pygame Zero com classe
===

Vamos dar uma versão melhor organizada para nossas classes.

Sabemos que os objetos possuem uma série de características que são padrão para nosso jogo, por exemplo a velocidade, e que ao atribuir uma variável para se tornar esse objeto, uma série de funções devem sem feitas: velocidade, seleção de som, posição inicial na tela, e a depender do jogo outros métodos mais.

Então será muito útil que seja redefinido o método `__init__` da classe `Actor` em todos os objetos que iremos crias no jogo, para que ao atribuirmos ele durante o jogo, todos os métodos sejam calculados de uma vez só. Observe uma versão 2.0 para nossa classe `Hero`.

Veja no próximo slide.

<!-- end_slide -->

Pygame Zero com classe
===

```python
class Hero(Actor):
    def __init__(self, image, pos=None, anchor=None, vel=7, life=3, **kwargs):
        super().__init__(image, pos, anchor, **kwargs)
        self.vel = vel
        self.life = life
        self.score = 0
        
        
    def update(self):
        if keyboard.left or keyboard.a:
            ship.x -= self.vel
            if ship.left < 0: # Parede à esquerda
                ship.left = 0
        if keyboard.right or keyboard.d:
            ship.x += self.vel
            if ship.right > WIDTH: # Parede à direita`
                ship.right = WIDTH
    

    def collide(self, item, items, c=1):
        if self.colliderect(item):
            if c>0: self.score += c
            else: self.life += c
            item.set_pos()
            item.som()
            items.remove(item)
```
Veja a definição da função `__init__`, a primeira função que ela executa é a função `super` que possui todos os métodos da classe mãe `Actor` e em específico devemos usar `super().__init__(...)` com todos os parâmetros em que originalmente a classe foi criada. Em outras palavras, estamos repetindo na classe herdeira `Hero` todo o início que ela tinha na classe mãe, assim ficamos livres para criar novas características e executar novos métodos.

Nesse exemplo, podemos definir novas características: `vel`, `life` e `score`. Enquanto as antigas são mantidas: `image`, `pos`, `anchor` e `**kwargs`. Esse último parâmetro é de utilização mais avançada, caso tenha interesse depois podemos recomendar alguma referência para o uso desse parâmetro.

Fica simples usarmos o navio com a velocidade desejada ou com quantas vidas quisermos:
```python
# Para deixar com vel=7 e life =3
ship = Hero('ship', midbottom=(WIDTH/2,HEIGTH))

# Para deixar com deixar um pouco mais lento e com mais vida
ship = Hero('ship', midbottom=(WIDTH/2,HEIGTH), vel=6, life=10)
```

Redefina o `__init__` da classe `Item` para que ela selecione o som tipo de som e posicione o objeto assim que for atribuída. Resposta no próximo slide.

<!-- end_slide -->

Pygame Zero com classe
===

```python
class Item(Actor):
    global HEIGHT


    def __init__(self, image, pos=None, anchor=None, vel=7, som=None, **kwargs):
        super().__init__(image, pos, anchor, **kwargs)
        self.vel = vel
        self.midtop = randint(20,780), 0
        self.som = som.play


    def set_pos(self):
        self.midtop = randint(20,780), 0

    
    def update(self):
        self.y += self.vel
        if self.bottom > HEIGHT:
            self.midtop = randint(20,780), 0
```