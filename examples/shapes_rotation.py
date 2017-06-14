from minecraftstuff import MinecraftShape
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

#connect to minecraft
mc = minecraft.Minecraft.create()

#test shape
pos = mc.player.getTilePos()
pos.y += 40

myShape = MinecraftShape(mc, pos)
try:
    print("draw shape")
    myShape.setBlocks(-5, 0, -5, 3, 0, 3, block.WOOL.id, 5)
    print("draw shape done")
    
    time.sleep(5)
    roll = 0
    pitch = 0
    yaw = 0

    #angles = [15,30,45,60,75,90]
    angles = [45, 90]

    print("roll shape")
    for roll in angles:
        myShape.rotate(yaw, pitch, roll)
        print("roll shape {} done".format(roll))
        time.sleep(1)
    
    for pitch in angles:
        myShape.rotate(yaw, pitch, roll)
        time.sleep(1)

    for yaw in angles:
        myShape.rotate(yaw, pitch, roll)
        time.sleep(1)

    for count in range(0,5):
        myShape.moveBy(1,0,0)
        time.sleep(0.5)

    time.sleep(5)
finally:
    myShape.clear()

