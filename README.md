# Homework 7

## Learning Outcomes

- Practice with abstract classes and interfaces
- Contributing to an existing codebase
- Following a UML diagram
- Using the `super` keyword
- Practicing encapsulation

This assignment is to implement Mobs in the style of Minecraft.
It is not necessary to be familiar with the video game Minecraft.
It is useful to understand what a Mob is:[(Minecraft Wiki)](https://minecraft.fandom.com/wiki/Mob)

## Instructions

You will get practice with interfaces and generic types by implementing [spawners](https://minecraft.fandom.com/wiki/Spawner). Specifically, you will write a generic type `Spawner[T]`, which creates an entity that spawns (creates) entities of type `T` until the spawner is destroyed. This will enable you to create a `ZombieSpawner` and even a `ZombieSpawnerSpawner`.

Feel free to change the `NOISINESS` constant in `mob.py` if the noises get annoying.

The initial code should be runnable from `main.py`.
It may be useful to run it to see what it does.

### Problem 1: Selecting an adjacent empty cell

Implement the method `select_adjacent_empty_cell()` in the `Entity` class (in `entity.py`) to fit the provided documentation.

For full credit, it needs to behave as described. It does not need to select an
adjacent cell randomly. For example, it is fine if it always chooses the
position to the left if it is available. You do need to include the documentation above
your code.

UML diagram at this point:
<img width="458" height="467" alt="added one method" src="https://github.com/user-attachments/assets/dd19d085-d911-4423-ba8c-ff3e4f80b58b" />

### Problem 2: Refactoring

Right now, the `take_damage()` method is in `LivingEntity`. You will be creating
a new type of `Entity` that is not a `LivingEntity` but will be capable of
taking damage. To lay the groundwork, you will complete the interface
`Damageable`, move `take_damage()` to it, have `LivingEntity` implement the
`Damageable` interface, and generalize functions to accept arguments of the more 
general type `Damageable` rather than the specific type `LivingEntity`. You will 
learn more if you keep this big picture in mind when doing each of the following steps.

1. Open `damageable.py`. You should see the declaration of an empty interface,
   `Damageable`, preceded by documentation (which you should not change).
2. Move the documentation for `take_damage()` from `LivingEntity` to `Damageable`.
   Remove all references to properties, since they will not necessarily apply. 
   Replace the word `hearts` with `units`, since not all entities have hearts or 
   status.
3. Copy over the signature of the method and mark it as abstract. That means
   that subclasses will have to provide an implementation of the method.
4. Modify `LivingEntity` to indicate that it implements the `Damageable`
   interface. When you override or implement a method declared elsewhere, you 
   are not required to provide documentation.
5. We want it to be possible to attack anything that is `Damageable`, so, in
   `LivingEntity`, change the type of the `attack()` parameter to `Damageable`.
   You will also need to change the reference to `victim.type` because
   `Damageable` objects do not have a `type`.
6. Make the corresponding change to the `attack()` parameter in `Mob`.
7. Make sure your code still runs and that living entities can still take 
   damage and be killed.

UML diagram at this point:
<img width="458" height="467" alt="add Damageable interface" src="https://github.com/user-attachments/assets/b8f1faf1-82b6-40b8-80aa-a2675a92e6a6" />


### Problem 3: Creating a spider spawner

You will create a spider [spawner](https://minecraft.fandom.com/wiki/Monster_Spawner)
that randomly creates spiders that appear in empty adjacent cells.

1. Create a class `SpiderSpawner` that is a subclass of `Entity`. Its 
   constructor should have no parameters. Use the provided `Spawner` image (`SpawnerOnSand.png`). Don't forget to add documentation (a brief 
   description of the class).
2. Create a private method `_spawn_if_space()` that checks for an adjacent empty
   cell using `select_adjacent_empty_cell()`. If it finds one, it constructs a
   `Spider` and places it at the returned `Position`.
3. Add a property `spawn_probability`, which should be a `float` in the range 0-1, 
   indicating the probability of spawning a spider on each turn. For example, if it 
   is .75, the per-turn probability would be 75%. You may choose the value.
4. Create a method `tick()` so that on each turn, a random number between 0 and
   1 is generated. If the number is less than `spawn_probability`,
   `spawn_if_space()` should be called.
5. For debugging and documentation purposes, have `tick()` and `spawn_if_space()`
   call `Game.GAME.add_text()` with messages indicating the value of the random 
   number and (if `spawn_if_space()` is called) whether an empty adjacent cell was 
   found and a spider spawned.
6. Modify the constructor in `Game` to randomly place a `SpiderSpawner` on the
   board. Run the program and make sure it behaves as expected. You should
   see turns in which a spider is spawned and turns in which they are not.
   **Copy the transcript showing different behaviors into `Summary.md`**.
7. Modify the constructor in `Game` to place the `SpiderSpawner` at (0, 0), and
   place other entities so they block it in (surround it on all three sides). 
   Increase the spawn probability to 1.0. Make sure it behaves as expected (not 
   spawning spiders when there is no adjacent empty cell). **Copy the transcript 
   into `Summary.md`**. Undo the changes in this step before proceeding to the next
   problem.

UML diagram at this point:
<img width="555" height="229" alt="add SpiderSpawner" src="https://github.com/user-attachments/assets/1c665102-1ae3-4730-aa7c-9f193be0c1f6" />


### Problem 4: Making spawners damageable

In Problem 3, you created indestructible spider spawners. In this problem, you
will make them `Damageable`.

1. In `SpiderSpawner`, add a private attribute `__hardness`, which should be
   an `int` of your choice greater than 0, such as 6.
2. Modify the `SpiderSpawner` class header to indicate that it will implement
   the `Damageable` interface.
3. Implement the method `take_damage()`. (You might want to refer to
   the implementation in `LivingEntity` for reference.) It should print appropriate
   messages and reduce the `__hardness` value. When `__hardness` reaches
   0, it should call an appropriately named private method that you create that
   prints that the spawner has been destroyed and removes it from the game.
   The private method should be named starting with an underscore, and does not
   require documentation.
4. Right now, the player attacks only aggressive mobs that are nearby. Change it
   so it also attacks all`Damageable` entities. Make sure to exclude the player
   or it will attack itself! Also make sure the names of your methods are
   accurate and proper style (verbs).
5. **Test your code to make sure the player can destroy a spider spawner and
   save the transcript to `Summary.md`.**

UML diagram at this point:
<img width="507" height="242" alt="SpiderSpawner is damageable" src="https://github.com/user-attachments/assets/168608fe-ec76-4355-9483-828a9dee11fa" />


### Problem 5: Creating a generic spawner

In this problem, you will complete a generic version of `Spawner` so you are
able to construct spawners for different types of mobs. Do not delete
`SpiderSpawner`, which you should keep for reference and grading.

1. Examine the provided class `Spawner[T]`. Note that the constructor takes two
   arguments:
    * The name of the entity type. This enables it to create its own type string
      (e.g., `"Spider Spawner"`) to pass to the `Entity` constructor.
    * A no-argument function `spawn()` that constructs a new instance of the
      class to spawn (e.g., `Spider`) whenever it is called. For example, you
      could write: `new_entity: Entity = spawn()`
2. Add these parameters to the constructor and make them attributes:
    * `spawn_probability` (`float`)
    * `hardness` (`int`)
3. Modify the class header to show that `Spawner[T]` will implement the
   `Damageable` interface.
4. Copy all the methods from `SpiderSpawner`, replacing occurrences of the
   string literal `"Spider"` with the property `spawn_type`. Replace any calls
   to the `Spider` constructor with calls to `spawn()`. Make other changes as
   needed.

UML diagram at this point:
<img width="503" height="324" alt="Generic Spawner" src="https://github.com/user-attachments/assets/ae124e6a-907b-477d-9bc6-b274ba1d4d3b" />


### Problem 6: Creating a zombie spawner

For this part, you will create a zombie spawner, which will take very little
code, thanks to the work you did making `Spawner` generic.

1. Create a new class `ZombieSpawner` that is a subclass of `Spawner[Zombie]`.
   The new class constructor should take no parameters, but it should
   pass the necessary arguments to the `Spawner[Zombie]` constructor.
   These are:
    * the name of the class being spawned (`"Zombie"`)
    * an anonymous function of no arguments that returns a new `Zombie`
    * `spawn_probability` (you can choose the value)
    * `hardness` (you can choose the value)
      You should not need to provide any code.
2. Add code to the `Game` constructor to create and randomly place a
   `ZombieSpawner`.
3. Test out the game and make sure the zombie spawner
    * spawns zombies
    * generates appropriate output
    * can be destroyed

   It would be wise to decrease zombies' attack strength or increase the
   player's number of hearts for testing purposes. You don't need to change
   them back.

UML diagram at this point:
<img width="481" height="329" alt="ZombieSpawner" src="https://github.com/user-attachments/assets/b0ed35de-1935-4b1a-a91e-4af0091b9250" />


### Problem 7: Adding another spawner

That was a lot work, but now it is easy to add other spawners. Create a
spawner for an existing (or new) `Mob`. You can get a picture of a mob from
the [Minecraft Wiki](https://minecraft.fandom.com/wiki/Mob) and
[convert it from webpng to a 64x64 png online](https://cloudconvert.com/webp-to-png).
You can pass `None` for the sound file name.

Add your new `Spawner` subclass to the game and make sure it works.

### Problem 8: Creating a spawner spawner

You should now be able to create a `ZombieSpawnerSpawner`: a spawner that
creates instances of `ZombieSpawner`. This should take only a few lines of code.
Test that it works.

## Tips

The #1 tip is to ask for help in office hours if anything is unclear.

* Always read provided documentation carefully when implementing a method.
* If you prefer, you can modify `Player` (in `player.py`) to be Alex rather than
  Steve.
* Text output
    * If the game grid uses up too much of your screen for you to see the
      messages in the text area, you can:
        - Change the constant `NUM_ROWS` in `main.py`.
        - View the text in VSCode's Terminal.
    * You may find it useful to call `clear_text()` from inside `Game.tick()`.
    * You can print debugging messages by calling `Game.GAME.add_text()`.
* The [Minecraft Wiki](https://minecraft.fandom.com/wiki/Minecraft_Wiki) is
  a useful resource.
