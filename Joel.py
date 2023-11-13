# Meteoritos
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        # Llamamos al constructor de la clase base (Sprite)
        super().__init__()
        # Elegimos una imagen de meteorito al azar de la lista 'meteor_images'
        self.image = random.choice(meteor_images)
        # Configuramos el color transparente de la imagen como negro (BLACK)
        self.image.set_colorkey(BLACK)
        # Obtenemos el rectángulo (área rectangular que ocupa el sprite) de la imagen
        self.rect = self.image.get_rect()
        # Colocamos el meteorito en una posición aleatoria en la parte superior de la pantalla
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-140, -100)
        # Asignamos velocidades aleatorias en los ejes x e y para simular el movimiento
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randrange(-5, 5)
    def update(self):
        # Actualizamos la posición del meteorito basado en sus velocidades
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # Verificamos si el meteorito ha salido de la pantalla
        if self.rect.top > HEIGHT + 10 or self.rect.left < -40 or self.rect.right > WIDTH + 40:
            # Si el meteorito está fuera de la pantalla, lo volvemos a colocar en la parte superior
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-140, - 100)
            # Asignamos nuevas velocidades aleatorias para un movimiento variado
            self.speedy = random.randrange(1, 10)
