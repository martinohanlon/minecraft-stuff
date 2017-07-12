=========================
Minecraft - Stuff Library
=========================

An extension library of useful 'stuff' (aka classes) I have created for Minecraft: Pi Edition's API.  

It provides functions for drawing lines, creating, moving and rotating shapes and a pretty cool turtle.  Check out the `documentation`_ and `examples`_.

|minecraftstuff|

Created by `Martin O'Hanlon`_, `@martinohanlon`_, `stuffaboutco.de`_.

Install
=========================

Open a terminal and run the following commands::

    sudo pip install minecraftstuff
    sudo pip3 install minecraftstuff

Code
=========================

See the `documentation`_ for more information, but below is a summary.

MinecraftDrawing
-------------------------

::

    from minecraftstuff import MinecraftDrawing
    from mcpi.minecraft import Minecraft
    from mcpi import block

    #Connect to minecraft
    mc = Minecraft.create()
    # get the players position
    pos = mc.player.getTilePos()

    #Using the Minecraft Drawing API
    mcdrawing = MinecraftDrawing(mc)
    
    # draw a circle with a radius of 10 blocks
    mcdrawing.drawCircle(pos.x, pos.y + 15, pos.z, 10, block.WOOD.id)

MinecraftShape
-------------------------

::

    from minecraftstuff import MinecraftShape
    from mcpi.minecraft import Minecraft
    from mcpi import block
    from time import sleep

    #Connect to minecraft
    mc = Minecraft.create()
    # get the players position
    pos = mc.player.getTilePos()

    #Using the Minecraft Shape API
    mcshape = MinecraftShape(mc, pos)

    # create a stone cube
    mcshape.setBlocks(-5, -5, -5, 5, 5, 5, block.STONE.id)
    
    # move it around
    for i in range(0,10):
        mcshape.moveBy(1,0,1)
        sleep(0.5)


MinecraftTurtle
-------------------------

::

    from minecraftstuff import MinecraftTurtle
    from mcpi.minecraft import Minecraft

    #Connect to minecraft
    mc = Minecraft.create()
    # get the players position
    pos = mc.player.getTilePos()

    #Using the Minecraft Turtle
    steve = MinecraftTurtle(mc, pos)
    
    # draw a square 
    steve.forward(5)
    steve.right(90)
    steve.forward(5)
    steve.right(90)
    steve.forward(5)
    steve.right(90)
    steve.forward(5)
 
.. _Martin O'Hanlon: https://github.com/martinohanlon
.. _stuffaboutco.de: http://stuffaboutco.de
.. _@martinohanlon: https://twitter.com/martinohanlon
.. _documentation: http://minecraft-stuff.readthedocs.io
.. _examples: https://github.com/martinohanlon/minecraft-stuff/tree/master/examples

.. |minecraftstuff| image:: https://raw.githubusercontent.com/martinohanlon/minecraft-stuff/master/docs/images/minecraftstuff.png
   :height: 853 px
   :width: 480 px
   :scale: 100 %
   :alt: shapes and lines in minecraft