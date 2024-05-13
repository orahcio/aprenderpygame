---
title: Construindo jogos em Python
sub_title: com o Pygame Zero (Aula 2)
author: Orahcio Felício de Sousa e Jaylson Teixeira
theme:
    name: catppuccin-mocha
    # override:
    #     footer:
    #         style: empty
---

Pygame Zero com classe
===

Na aula passa escrevemos um jogo que está totalmente funcional dentro das regras que estabelecemos para ele.

Vamos refinar esse mesmo jogo, usando a programação orientada a objetos para que as regras fiquem mais compactadas dentro de cada elemento do jogo. Cada uma deles será entendido como um objeto, definidos em uma classe.

![](tesouro.png)

<!-- end_slide -->

Pygame Zero com classe
===

# O jogo tem início igual ao anterior, importando bibliotecas e definindo as dimensões da janela.
```python
from random import randint

WIDTH = 800
HEIGHT = 600
```

# Primeiro vamos definir a classe dos objetos que caem, eles têm praticamente os mesmo comportamento, exceto pelo incremento de pontos (moedas) e decremento de vidas (bomba)
```python
class Item(Actor):
    global HEIGHT

    vel = 7
```

A definição dessa classe `Item` é herdeira da classe `Actor`, isso significa que iremos montar a moeda da forma idêntica como fizemos anteriormente, sem necessitar posicioná-la logo de cara:
```pyhton
coin = Item('coin')
bomb = Item('bomb')
```
tudo que precisamos fazer seja com  bomba seja com a moeda, redefinimos a classe.

<!-- end_slide -->

Pygame Zero com classe (`tesouro-class.py`)
===

# Até o momento!
```python
from random import randint

WIDTH = 800
HEIGHT = 600


class Item(Actor):
    global HEIGHT

    vel = 7


coin = Item('coin')
bomb = Item('bomb')
```
Até o momento apenas definimos que a classe `Item` herdará a classe `Actor` e usará a variável global `HEIGHT` que definirá o piso da tela do jogo, além da variável `vel` que podemos mudar quando o objeto for utilizado em `coin` ou `bomb`.

Vamos desenhar os elementos já usando a lógica do `game_over` aprendida anteriormente.

<!-- end_slide -->

Pygame Zero com classe (`tesouro-class.py`)
===

Iniciando a variável `game_over` e desenhando todos elementos na tela:
```python
game_over = False


def draw():
    global game_over

    if not game_over:
        screen.blit('background',(0,0))
        coin.draw()
        bomb.draw()
    
    else:
        screen.blit('background',(0,0))
        screen.draw.text(f'Game Over', (400,300),\
            fontname='pixel', color=(255,255,255),\
            fontsize=30)
```

<!-- end_slide -->

Pygame Zero com classe (`tesouro-class.py`)
===

# Até o momento!

```python
from random import randint

WIDTH = 800
HEIGHT = 600


class Item(Actor):
    global HEIGHT

    vel = 7


coin = Item('coin')
bomb = Item('bomb')

game_over = False


def draw():
    global game_over

    if not game_over:
        screen.blit('background',(0,0))
        coin.draw()
        bomb.draw()
    
    else:
        screen.blit('background',(0,0))
        screen.draw.text(f'Game Over', (400,300),\
            fontname='pixel', color=(255,255,255),\
            fontsize=30)
```
Experimente virar a chave da variável `game_over` definindo ela como `True` para visualizar a tela de `Game Over`.

<!-- end_slide -->

Pygame Zero com classe (`tesouro-class.py`)
===

Melhorando a classe `Item` para definir a posição e a dinâmica de queda

```python
class Item(Actor):
    global HEIGHT

    vel = 7


    def set_pos(self):
        self.midtop = randint(20,780), 0


    def update(self):
        self.y += self.vel
        if self.bottom > HEIGHT:
            self.set_pos()    
```

E então faça o update no jogo, não esqueça de definir a posição logo depois que atribuir os objetos:
```python
# essa linha é logo após de coin=Item('coin')
coin.set_pos()
# essa linha é logo após bomb=Item('bomb')
bomb.set_pos()


def update():
    if not game_over;
        coin.update()
        bomb.update()
```

<!-- end_slide -->

Pygame Zero (`tesouro-class.py`)
===

# Até o momento!

<!-- column_layout: [1, 1] -->

<!-- column: 0 -->
## Definições
```python
from random import randint

WIDTH = 800
HEIGHT = 600


class Item(Actor):
    global HEIGHT

    vel = 7

    def set_pos(self):
        self.midtop = randint(20,780), 0


    def update(self):
        self.y += self.vel
        if self.bottom > HEIGHT:
            self.set_pos()    
        


coin = Item('coin')
coin.set_pos()
bomb = Item('bomb')
bomb.set_pos()

game_over = False
```

<!-- column: 1 -->

## Desenho e dinâmica
```python
def draw():
    global game_over

    if not game_over:
        screen.blit('background',(0,0))
        coin.draw()
        bomb.draw()
    
    else:
        screen.blit('background',(0,0))
        screen.draw.text(f'Game Over', (400,300),\
                         fontname='pixel', color=(255,255,255),
                         fontsize=30)


def update():
    if not game_over:
        coin.update()
        bomb.update()
```
<!-- reset_layout -->
E vai ver uma chuva de moedas e bombas.