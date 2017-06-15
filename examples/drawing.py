from minecraftstuff import MinecraftDrawing, ShapeBlock, Points
import mcpi.minecraft as minecraft
import mcpi.block as block

#connect to minecraft
mc = minecraft.Minecraft.create()

#test MinecraftDrawing

#clear area
mc.setBlocks(-25, 0, -25, 25, 25, 25, block.AIR.id)

#create drawing object
mcDrawing = MinecraftDrawing(mc)

#line
mcDrawing.drawLine(0,0,-10,-10,10,-5,block.STONE.id)

#circle
mcDrawing.drawCircle(-15,15,-15,10,block.WOOD.id)

#sphere
mcDrawing.drawSphere(-15,15,-15,5,block.OBSIDIAN.id)

#face - solid triangle
faceVertices = []
faceVertices.append(minecraft.Vec3(0,0,0))
faceVertices.append(minecraft.Vec3(5,10,0))
faceVertices.append(minecraft.Vec3(10,0,0))
mcDrawing.drawFace(faceVertices, True, block.SNOW_BLOCK.id)

#face - wireframe square - using Points
faceVertices = Points()
faceVertices.add(0,0,5)
faceVertices.add(10,0,5)
faceVertices.add(10,10,5)
faceVertices.add(0,10,5)
mcDrawing.drawFace(faceVertices, False, block.DIAMOND_BLOCK.id)

#face - 5 sided shape
faceVertices = []
faceVertices.append(minecraft.Vec3(0,15,0))
faceVertices.append(minecraft.Vec3(5,15,5))
faceVertices.append(minecraft.Vec3(3,15,10))
faceVertices.append(minecraft.Vec3(-3,15,10))
faceVertices.append(minecraft.Vec3(-5,15,5))
mcDrawing.drawFace(faceVertices, True, block.GOLD_BLOCK.id)
