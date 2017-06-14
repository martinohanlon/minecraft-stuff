from minecraftstuff import MinecraftShape, ShapeBlock
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

#connect to minecraft
mc = minecraft.Minecraft.create()

#test MinecraftShape
playerPos = mc.player.getTilePos()

#create the shape object
shapeBlocks = [ShapeBlock(0,0,0,block.DIAMOND_BLOCK.id),
                ShapeBlock(1,0,0,block.DIAMOND_BLOCK.id),
                ShapeBlock(1,0,1,block.DIAMOND_BLOCK.id),
                ShapeBlock(0,0,1,block.DIAMOND_BLOCK.id),
                ShapeBlock(0,1,0,block.DIAMOND_BLOCK.id),
                ShapeBlock(1,1,0,block.DIAMOND_BLOCK.id),
                ShapeBlock(1,1,1,block.DIAMOND_BLOCK.id),
                ShapeBlock(0,1,1,block.DIAMOND_BLOCK.id)]

#move the shape about
myShape = MinecraftShape(mc, playerPos, shapeBlocks)
print("drawn shape")
time.sleep(10)
myShape.moveBy(-1,1,-1)
time.sleep(1)
myShape.moveBy(1,0,1)
time.sleep(1)
myShape.moveBy(1,1,0)
time.sleep(1)

#rotate the shape
myShape.rotate(90,0,0)

#clear the shape
myShape.clear()
