# Nikashooter
#### <b> Video Demo: </b> https://youtu.be/oaCp_kQO3UY
#### <b> Description: </b> Simple Python shooting game made with PyGame

<br>

### <span style="color: cyan">TODO</span>
- Pygame boilerplate <br>
- Player class <br>
- Enemy class <br>
- Wave class (Enemy waves) <br>
- Bullet class <br>
- Explosion class <br>
- Particle class <br>
- Functions to check if game has ended <br>

<br>

### <span style="color: cyan">Inputs, Processes, Outputs</span>

- <span style="color: white">prompt</span>
- <span style="color: red">compute</span>
- <span style="color: blue">display</span>

#### Inputs:
- Player mouse X coordinate
- Player mouse left button click

#### Processes:
- On click - shoot a bullet
- Follow player to mouse X coordinate
- Detect collisions
- Increase score
- Check for game end
- Update display
- Update player, enemies, explosions, particles

#### Outputs:
- Draw display

<br><hr><br>

### <span style="color: cyan">Pseudocode</span>

> ### Nikashooter
>> Initialize **PyGame** window <br>
>> Define `Player` class and its `draw` and `update` methods <br>
>> Define `Enemy` class and its `draw` and `update` methods <br>
>> Define `Explosion` class and its `draw` and `update` methods <br>
>> Define `Waves` class and its `next_wave` and `update` methods <br>
>> Define `check_game_won` method <br>
>> Define `check_game_over` method <br>
>> Define `draw_interface` method <br>
> 
>> Update `Player`, `Enemy`, `Explosion` and `Waves` objects inside PyGame game loop <br>
>
>> Display player `score` and `health` to the user <br>
>> Display `enemies` to the user <br>
>
> <br>

<br><br>

##### Made by Nick Kipshidze (: