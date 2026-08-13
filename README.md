At the state it's in right now, This is a very simple 2d engine for handling a tilemap and entities and such. It's written with python 3.8.10 mainly.
There's some pathfinding code that was provided by my good friend Chet Gepeiti, but it lowkey sucks and I'll probably re-write it once I get bored of procrsatinating (And actually understand the A* algorithm).

# The Engine has two main parts:

## The Tilemap:

Which is, under the hood, one big image that is used to put together the tiles into one large pygame surface at startup to minimize draw calls.

## And, the Entities:

These are the real moving parts of the engine. They (eventually) can be anything, from a building, to an item on the ground, 
to each and every Hero and Monster running around the world.

the engine runs on a descrete-tick system, with 10 ticks per second.
Every frame, Each entity runs it's own Update() function in the order that they are created. (I see how minecraft has that pickup priority thing now)
I've not implimented it yet, but that's where AI thinking, pathfinding, combat, and other interactions will happen.

# Overall:

This game, Ideally, should be a game that works fine without a player.
I personally enjoy games, such as kenshi or Stalker: Anomaly, that put the player in a world that couldn't care less about them.
This, ideally, should be similiar to something like that, but much more casual.

At the end of the day though, this is just practice in project organization and creating different systems that work together, rather than writing everything into one large file.