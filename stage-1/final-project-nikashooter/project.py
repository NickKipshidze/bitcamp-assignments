from random import randint as rint
import pygame

class Player(object):
    def __init__(self, surface: pygame.surface.Surface, width: int, height: int, y_position: int, x_boundary) -> None:
        self.surface = surface
        
        self.width = width
        self.height = height
        self.y_position = y_position
        self.x_boundary = x_boundary

        self.x_position = 128
        self.color = (255, 255, 255)
        self.bullets = []
        self.shoot_timeout = 5
        self.shoot_timer = 0
    
        self.health = 100
        self.score = 0
        self.image = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load("assets/player.png").convert_alpha()
                , (self.width, self.height))
            , 180
        )

    def shoot(self, amount: int = 1) -> None:
        if self.shoot_timer <= 0:
            self.shoot_timer = self.shoot_timeout

            for offset in range(amount):
                self.bullets.append(
                    Bullet(
                        self.surface, 10, 50,
                        self.x_position+self.width//2+5-(amount*10)+(offset*20),
                        self.y_position+20, 50
                    )
                )
        else:
            self.shoot_timer -= 1
    
    def draw(self) -> None:
        self.player_rect = pygame.rect.Rect(self.x_position, self.y_position, self.width, self.height)
        self.surface.blit(self.image, (self.x_position, self.y_position))
    
    def update(self) -> None:
        self.x_position = get_cursor_position()[0]-self.width//2

        if self.x_position + self.width > self.x_boundary:
            self.x_position = self.x_boundary - self.width
        
        for bullet in self.bullets:
            bullet.update()

        self.draw()

class Enemy(object):
    def __init__(self, surface: pygame.surface.Surface, player: Player, width: int, height: int, x_position: int) -> None:
        self.surface = surface
        self.player = player

        self.width = width
        self.height = height
        self.x_position = x_position
        self.y_position = -self.height-50

        self.color = (255, 0, 0)
        self.speed = 10
        self.health = 100
        self.damage = 5

        self.image = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load("assets/enemy.png").convert_alpha()
                , (self.width, self.height))
            , 0
        )

        self.explosions = []
    
    def check_collision(self) -> None:
        if self.enemy_rect.colliderect(self.player.player_rect):
            self.player.health -= self.damage*2
            self.health -= 50
        
        for bullet in range(len(self.player.bullets)):
            if self.enemy_rect.colliderect(self.player.bullets[bullet].bullet_rect):
                self.health -= self.player.bullets[bullet].damage
                self.explosions.append(
                    Explosion(self.surface, self.player.bullets[bullet].x_position, self.player.bullets[bullet].y_position, 5, 5, (255, 255, 0))
                )
                del self.player.bullets[bullet]
                break
    
    def draw(self) -> None:
        self.enemy_rect = pygame.rect.Rect(self.x_position, self.y_position, self.width, self.height)
        self.surface.blit(self.image, (self.x_position, self.y_position))
    
    def update(self) -> None:
        self.y_position += self.speed
        self.draw()

        for explosion in self.explosions:
            explosion.update()

        try: self.check_collision()
        except AttributeError: pass

class Bullet(object):
    def __init__(self, surface: pygame.surface.Surface, width: int, height: int, x_position: int, y_position: int, speed: int) -> None:
        self.surface = surface
        
        self.width = width
        self.height = height
        self.x_position = x_position
        self.y_position = y_position
        self.speed = speed

        self.color = (255, 255, 255)
        self.damage = 20

        self.image = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load("assets/bullet.png").convert_alpha()
                , (self.width, self.height))
            , 0
        )
    
    def draw(self) -> None:
        self.bullet_rect = pygame.rect.Rect(self.x_position, self.y_position, self.width, self.height)
        self.surface.blit(self.image, (self.x_position, self.y_position))
    
    def update(self) -> None:
        self.y_position -= self.speed
        self.draw()

class Particle(object):
    def __init__(self, surface: pygame.surface.Surface, color: tuple, x: int, y: int, radius: int, velocty: list, drag: list) -> None:
        self.surface = surface

        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.velocity = velocty
        self.drag = drag
    
    def draw(self) -> None:
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)
    
    def update(self) -> None:
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.velocity[0] *= self.drag[0]
        self.velocity[1] *= self.drag[1]

        if self.x >= 0 and abs(self.velocity[0])+abs(self.velocity[1]) > 1:
            self.draw()

class Explosion(object):
    def __init__(self, surface: pygame.surface.Surface, x: int, y: int, power: int, amount: int, color: tuple = (255, 0, 0)) -> None:
        self.surface = surface

        self.x = x
        self.y = y
        self.power = power
        self.amount = amount
        self.color = color
        self.drag = [0.9, 0.9]

        self.particles = []

        self.blast()
    
    def blast(self):
        for _ in range(self.amount):
            self.particles.append(
                Particle(self.surface, self.color, self.x, self.y, 2, [rint(-self.power, self.power), rint(-self.power, self.power)], self.drag)
            )
    
    def update(self):
        for particle in self.particles:
            particle.update()

class Waves(object):
    def __init__(self, surface: pygame.surface.Surface, player: Player) -> None:
        self.surface = surface
        self.player = player

        self.wave_timeout = 100
        self.wave_timer = 0
        self.enemy_speed = 5
        self.enemies = []
        self.explosions = []
    
    def next_wave(self) -> None:
        for offset in range(32, 512, 100):
            self.enemies.append(
                Enemy(self.surface, self.player, 64, 96, offset)
            )
            self.enemies[-1].speed = self.enemy_speed
    
    def update(self, end: bool = False) -> None:
        for explosion in self.explosions:
            explosion.update()

        if self.wave_timer <= 0 and not end:
            self.wave_timer = self.wave_timeout
            self.next_wave()
        else:
            self.wave_timer -= 1

        if not end:
            for enemy in range(len(self.enemies)):
                try:
                    if self.enemies[enemy].health < 0:
                        self.player.score += self.enemies[enemy].damage
                        self.explosions.append(Explosion(self.surface, self.enemies[enemy].x_position+32, self.enemies[enemy].y_position+32, 10, 50))
                        del self.enemies[enemy]
                    if self.enemies[enemy].y_position > 768:
                        del self.enemies[enemy]
                except IndexError:
                    pass
        
        for enemy in self.enemies:
            enemy.update()

def get_cursor_position() -> tuple:
    return pygame.mouse.get_pos()

def check_game_over(surface: pygame.surface.Surface, player: Player, WIDTH: int, HEIGHT: int) -> None:
    if player.health <= 0:
        try:
            player.loose_explosion.update()
        except AttributeError:
            player.loose_explosion = Explosion(surface, player.x_position, player.y_position, 50, 500)

        font = pygame.font.SysFont("Monospace", 32)
        score = font.render(f"Game Over!", True, "#FF0000")
        surface.blit(score, (WIDTH//2-score.get_width()//2, HEIGHT//2))

        return True
    else:
        return False

def check_game_won(surface: pygame.surface.Surface, player: Player, WIDTH: int, HEIGHT: int) -> None:
    if player.score >= 128:
        try:
            player.win_explosion.update()
            for particle in player.win_explosion.particles:
                if particle.y > HEIGHT//2:
                    particle.color = (0, 0, 255)
                if particle.y < HEIGHT//2:
                    particle.color = (255, 255, 0)
        except AttributeError:
            player.win_explosion = Explosion(surface, player.x_position, player.y_position, 50, 1000, color=(0, 0, 255))
        
        font = pygame.font.SysFont("Monospace", 32)
        score = font.render(f"You Won!", True, "#FFFF00")
        surface.blit(score, (WIDTH//2-score.get_width()//2, HEIGHT//2))

        return True
    else:
        return False

def draw_interface(surface: pygame.surface.Surface, player: Player) -> None:
    # Health bar
    pygame.draw.rect(surface, "#FFFFFF", (10, 10, 102*2, 22))
    pygame.draw.rect(surface, "#D94821", (11, 11, player.health*2, 20))

    # Score
    font = pygame.font.SysFont("Monospace", 32)
    score = font.render(f"Score: {player.score}", True, "#FFFF00")
    surface.blit(score, (10, 35))

def main() -> None:
    pygame.init()
    pygame.font.init()

    RUN = True
    WIDTH, HEIGHT = 512, 768
    FPS = 30

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player(screen, 64, 96, 600, WIDTH)
    waves = Waves(screen, player)

    pygame.display.set_caption("Nikashooter - By Nick Kipshidze")

    while RUN:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            
        screen.fill("#595E41")
        
        if not check_game_over(screen, player, WIDTH, HEIGHT) and not check_game_won(screen, player, WIDTH, HEIGHT):
            player.update()
            waves.update()

            if pygame.mouse.get_pressed()[0]:
                player.shoot()
        else:
            if check_game_won(screen, player, WIDTH, HEIGHT):
                player.update()
            else:
                waves.update(end = True)

        draw_interface(screen, player)

        pygame.display.update()
    
    pygame.display.quit()

if __name__ == "__main__":
    main()