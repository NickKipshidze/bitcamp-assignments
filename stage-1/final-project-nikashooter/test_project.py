import project, pygame

def test_get_cursor_position():
    pygame.init()

    assert project.get_cursor_position() == (0, 0)

def test_check_game_over():
    surface = pygame.display.set_mode((10, 10))
    player = project.Player(surface, 10, 10, 0, 0)

    assert project.check_game_over(surface, player, 10, 10) == False

    player.health = 0

    assert project.check_game_over(surface, player, 10, 10) == True

def test_check_game_won():
    surface = pygame.display.set_mode((10, 10))
    player = project.Player(surface, 10, 10, 0, 0)

    assert project.check_game_won(surface, player, 10, 10) == False

    player.score = 128

    assert project.check_game_won(surface, player, 10, 10) == True

def test_draw_interface():
    surface = pygame.display.set_mode((10, 10))
    player = project.Player(surface, 10, 10, 0, 0)

    assert project.draw_interface(surface, player) == None