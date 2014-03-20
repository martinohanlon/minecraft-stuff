#www.stuffaboutcode.com
#Raspberry Pi, Minecraft - Minecraft 'stuff' extensions

#import the minecraft.py module 
import minecraft
#import block.py module
import block

class MinecraftDrawing:
    def __init__(self, mc):
        self.mc = mc

    # draw point
    def drawPoint3d(self, x, y, z, blockType, blockData=0):
        self.mc.setBlock(x,y,z,blockType,blockData)
        #print "x = " + str(x) + ", y = " + str(y) + ", z = " + str(z)

    # draws a face, when passed a collection of vertices which make up a polyhedron
    def drawFace(self, vertices, filled, blockType, blockData=0):
        # get the edges of the face
        edgesVertices = []
        # persist first vertex
        firstVertex = vertices[0]
        # get last vertex
        lastVertex = vertices[0]
        # loop through vertices and get edges
        for vertex in vertices[1:]:
            # got 2 vertices, get the points for the edge
            edgesVertices = edgesVertices + self.getLine(lastVertex.x, lastVertex.y, lastVertex.z, vertex.x, vertex.y, vertex.z)
            # persist the last vertex found    
            lastVertex = vertex
        # get edge between the last and first vertices
        edgesVertices = edgesVertices + self.getLine(lastVertex.x, lastVertex.y, lastVertex.z, firstVertex.x, firstVertex.y, firstVertex.z)

        if (filled):
            #draw solid face
            # sort edges vertices
            def keyX( point ): return point.x
            def keyY( point ): return point.y
            def keyZ( point ): return point.z
            edgesVertices.sort( key=keyZ )
            edgesVertices.sort( key=keyY )
            edgesVertices.sort( key=keyX )

            #draw lines between the points on the edges
            # this algorithm isnt very efficient, but it does always fill the gap
            lastVertex = edgesVertices[0]
            for vertex in edgesVertices[1:]:
                # got 2 vertices, draw lines between them
                self.drawLine(lastVertex.x, lastVertex.y, lastVertex.z, vertex.x, vertex.y, vertex.z, blockType, blockData)
                #print "x = " + str(lastVertex.x) + ", y = " + str(lastVertex.y) + ", z = " + str(lastVertex.z) + " x2 = " + str(vertex.x) + ", y2 = " + str(vertex.y) + ", z2 = " + str(vertex.z)
                # persist the last vertex found
                lastVertex = vertex

        else:
            #draw wireframe
            self.drawVertices(edgesVertices, blockType, blockData)
        
    # draw's all the points in a collection of vertices with a block
    def drawVertices(self, vertices, blockType, blockData=0):
        for vertex in vertices:
            self.drawPoint3d(vertex.x, vertex.y, vertex.z, blockType, blockData)

    # draw line
    def drawLine(self, x1, y1, z1, x2, y2, z2, blockType, blockData=0):
        self.drawVertices(self.getLine(x1, y1, z1, x2, y2, z2), blockType, blockData)

    # draw sphere
    def drawSphere(self, x1, y1, z1, radius, blockType, blockData=0):
        # create sphere
        for x in range(radius*-1,radius):
            for y in range(radius*-1, radius):
                for z in range(radius*-1,radius):
                    if x**2 + y**2 + z**2 < radius**2:
                        self.drawPoint3d(x1 + x, y1 + y, z1 + z, blockType, blockData)

    # draw a verticle circle
    def drawCircle(self, x0, y0, z, radius, blockType, blockData=0):
        f = 1 - radius
        ddf_x = 1
        ddf_y = -2 * radius
        x = 0
        y = radius
        self.drawPoint3d(x0, y0 + radius, z, blockType, blockData)
        self.drawPoint3d(x0, y0 - radius, z, blockType, blockData)
        self.drawPoint3d(x0 + radius, y0, z, blockType, blockData)
        self.drawPoint3d(x0 - radius, y0, z, blockType, blockData)
     
        while x < y:
            if f >= 0:
                y -= 1
                ddf_y += 2
                f += ddf_y
            x += 1
            ddf_x += 2
            f += ddf_x   
            self.drawPoint3d(x0 + x, y0 + y, z, blockType, blockData)
            self.drawPoint3d(x0 - x, y0 + y, z, blockType, blockData)
            self.drawPoint3d(x0 + x, y0 - y, z, blockType, blockData)
            self.drawPoint3d(x0 - x, y0 - y, z, blockType, blockData)
            self.drawPoint3d(x0 + y, y0 + x, z, blockType, blockData)
            self.drawPoint3d(x0 - y, y0 + x, z, blockType, blockData)
            self.drawPoint3d(x0 + y, y0 - x, z, blockType, blockData)
            self.drawPoint3d(x0 - y, y0 - x, z, blockType, blockData)

    # draw a horizontal circle
    def drawHorizontalCircle(self, x0, y, z0, radius, blockType, blockData=0):
        f = 1 - radius
        ddf_x = 1
        ddf_z = -2 * radius
        x = 0
        z = radius
        self.drawPoint3d(x0, y, z0 + radius, blockType, blockData)
        self.drawPoint3d(x0, y, z0 - radius, blockType, blockData)
        self.drawPoint3d(x0 + radius, y, z0, blockType, blockData)
        self.drawPoint3d(x0 - radius, y, z0, blockType, blockData)
     
        while x < z:
            if f >= 0:
                z -= 1
                ddf_z += 2
                f += ddf_z
            x += 1
            ddf_x += 2
            f += ddf_x   
            self.drawPoint3d(x0 + x, y, z0 + z, blockType, blockData)
            self.drawPoint3d(x0 - x, y, z0 + z, blockType, blockData)
            self.drawPoint3d(x0 + x, y, z0 - z, blockType, blockData)
            self.drawPoint3d(x0 - x, y, z0 - z, blockType, blockData)
            self.drawPoint3d(x0 + z, y, z0 + x, blockType, blockData)
            self.drawPoint3d(x0 - z, y, z0 + x, blockType, blockData)
            self.drawPoint3d(x0 + z, y, z0 - x, blockType, blockData)
            self.drawPoint3d(x0 - z, y, z0 - x, blockType, blockData)
    
    # returns points on a line
    # 3d implementation of bresenham line algorithm
    def getLine(self, x1, y1, z1, x2, y2, z2):

        # return maximum of 2 values
        def MAX(a,b):
            if a > b: return a
            else: return b

        # return step
        def ZSGN(a):
            if a < 0: return -1
            elif a > 0: return 1
            elif a == 0: return 0

        # list for vertices
        vertices = []

        # if the 2 points are the same, return single vertice
        if (x1 == x2 and y1 == y2 and z1 == z2):
            vertices.append(minecraft.Vec3(x1, y1, z1))
                            
        # else get all points in edge
        else:
        
            dx = x2 - x1
            dy = y2 - y1
            dz = z2 - z1

            ax = abs(dx) << 1
            ay = abs(dy) << 1
            az = abs(dz) << 1

            sx = ZSGN(dx)
            sy = ZSGN(dy)
            sz = ZSGN(dz)

            x = x1
            y = y1
            z = z1

            # x dominant
            if (ax >= MAX(ay, az)):
                yd = ay - (ax >> 1)
                zd = az - (ax >> 1)
                loop = True
                while(loop):
                    vertices.append(minecraft.Vec3(x, y, z))
                    if (x == x2):
                        loop = False
                    if (yd >= 0):
                        y += sy
                        yd -= ax
                    if (zd >= 0):
                        z += sz
                        zd -= ax
                    x += sx
                    yd += ay
                    zd += az
            # y dominant
            elif (ay >= MAX(ax, az)):
                xd = ax - (ay >> 1)
                zd = az - (ay >> 1)
                loop = True
                while(loop):
                    vertices.append(minecraft.Vec3(x, y, z))
                    if (y == y2):
                        loop=False
                    if (xd >= 0):
                        x += sx
                        xd -= ay
                    if (zd >= 0):
                        z += sz
                        zd -= ay
                    y += sy
                    xd += ax
                    zd += az
            # z dominant
            elif(az >= MAX(ax, ay)):
                xd = ax - (az >> 1)
                yd = ay - (az >> 1)
                loop = True
                while(loop):
                    vertices.append(minecraft.Vec3(x, y, z))
                    if (z == z2):
                        loop=False
                    if (xd >= 0):
                        x += sx
                        xd -= az
                    if (yd >= 0):
                        y += sy
                        yd -= az
                    z += sz
                    xd += ax
                    yd += ay
                    
        return vertices

# testing
if __name__ == "__main__":

    #connect to minecraft
    mc = minecraft.Minecraft.create()

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

    #face - wireframe square
    faceVertices = []
    faceVertices.append(minecraft.Vec3(0,0,5))
    faceVertices.append(minecraft.Vec3(10,0,5))
    faceVertices.append(minecraft.Vec3(10,10,5))
    faceVertices.append(minecraft.Vec3(0,10,5))
    mcDrawing.drawFace(faceVertices, False, block.DIAMOND_BLOCK.id)

    #face - 5 sided shape
    faceVertices = []
    faceVertices.append(minecraft.Vec3(0,15,0))
    faceVertices.append(minecraft.Vec3(5,15,5))
    faceVertices.append(minecraft.Vec3(3,15,10))
    faceVertices.append(minecraft.Vec3(-3,15,10))
    faceVertices.append(minecraft.Vec3(-5,15,5))
    mcDrawing.drawFace(faceVertices, True, block.GOLD_BLOCK.id)

