class brush:
	def __init__(self, veca, vecb):
		self.spoint = veca
		self.epoint = vecb
		self.texlist = []
		for i in range(6):
			self.texlist.append(texture("gothic_block/blocks18c_3", 0, 0, 0, 0.5, 0.5, 0))
	def __str__(self):
		l1 = "( "+str(self.spoint.x)+" 0 0 ) ( "+str(self.spoint.x)+" 1 0 ) ( "+str(self.spoint.x)+" 0 1 ) "+str(self.texlist[0])+"\n"
		l2 = "( "+str(self.epoint.x)+" 0 0 ) ( "+str(self.epoint.x)+" 0 1 ) ( "+str(self.epoint.x)+" 1 0 ) "+str(self.texlist[1])+"\n"
		l3 = "( 0 "+str(self.spoint.y)+" 0 ) ( 0 "+str(self.spoint.y)+" 1 ) ( 1 "+str(self.spoint.y)+" 0 ) "+str(self.texlist[2])+"\n"
		l4 = "( 0 "+str(self.epoint.y)+" 0 ) ( 1 "+str(self.epoint.y)+" 0 ) ( 0 "+str(self.epoint.y)+" 1 ) "+str(self.texlist[3])+"\n"
		l5 = "( 0 0 "+str(self.spoint.z)+" ) ( 1 0 "+str(self.spoint.z)+" ) ( 0 1 "+str(self.spoint.z)+" ) "+str(self.texlist[4])+"\n"
		l6 = "( 0 0 "+str(self.epoint.z)+" ) ( 0 1 "+str(self.epoint.z)+" ) ( 1 0 "+str(self.epoint.z)+" ) "+str(self.texlist[5])+"\n"
		return "{\n"+l1+l2+l3+l4+l5+l6+"}\n"
	def setTexture(self, index, texture):
		self.texlist[index] = texture
	def setAllTextures(self, texture):
		for i in range(6):
			self.texlist[i] = texture

class texture:
	def __init__(self, txstring, xoff, yoff, txrot, xscale, yscale, detailflag):
		self.txstring = txstring
		self.xoff = xoff
		self.yoff = yoff
		self.txrot = txrot
		self.xscale = xscale
		self.yscale = yscale
		self.detailflag = detailflag
	def __str__(self):
		return str(self.txstring)+" "+str(self.xoff)+" "+str(self.yoff)+" "+str(self.txrot)+" "+str(self.xscale)+" "+str(self.yscale)+" "+str(self.detailflag)+" 0 0"
		
class vec3:
	def __init__(self, x, y, z):
		self.x = int(x)
		self.y = int(y)
		self.z = int(z)
	def __str__(self):
		return "("+str(self.x)+", "+str(self.y)+", "+str(self.z)+")"
	def __len__(self):
		return 3

"""
>>> var = vec3(5,8,2)
>>> var.x
5
>>> var.y
8
>>> var.z
2
>>> str(var)
(5,8,2)
"""

#initialize variables
textures = ["gothic_block/blocks18c_3"]
entitynum = 0
brushnum = 0
brushes = []

#initialize map file, write first lines
newmap = open("generation.map", "w")
newmap.write('// entity '+str(entitynum)+' \n{ \n"classname" "worldspawn" \n')

tbrush1 = brush(vec3(0,0,0), vec3(512,512,512))
brushes.append(tbrush1)
tbrush2 = brush(vec3(0,64,128), vec3(512,1024,256))
brushes.append(tbrush2)
tbrush3 = brush(vec3(256,256,256), vec3(384,512,2048))
brushes.append(tbrush3)

for b in range(len(brushes)):
	newmap.write("//brush "+str(brushnum)+"\n")
	brushnum += 1
	newmap.write(str(brushes[b]))

newmap.close()
	
#explanation of how radiant actually maps this junk
"""
Rectangular prism example.

newmap.write('\n( 0 0 64 ) ( 1 0 64 ) ( 0 1 64 ) '+textures[0]+' 0 0 0 0.5 0.5 0 0 0')
newmap.write('\n( 0 0 128 ) ( 0 1 128 ) ( 1 0 128 ) '+textures[0]+' 0 0 0 0.5 0.5 0 0 0\n}')

This first pair of points describes the height of the brush to radiant. The first set of points
is the lower bound of the height description, and the second set of points is the upper bound
of the height description. These vertices are -128u on both x & y axis from the bottom left corner
side of the prism, if looking top down at a standard 90 degree view.

newmap.write('\n( 128 0 0 ) ( 128 1 0 ) ( 128 0 1 ) '+textures[0]+' 0 0 0 0.5 0.5 0 0 0')
newmap.write('\n( 256 0 0 ) ( 256 0 1 ) ( 256 1 0 ) '+textures[0]+' 0 0 0 0.5 0.5 0 0 0')

The second pair of points describes the length of the brush to radiant. The first set of points
is the lower bound of the length description, and the second set of points is the upper bound of
the length of the prism. These vertices are -128u on the x axis from the "-x" side of the prism,
and 64u below the "-z" face of the prism.

newmap.write('\n( 0 128 0 ) ( 0 128 1 ) ( 1 128 0 ) '+textures[0]+' 0 0 0 0.5 0.5 0 0 0')
newmap.write('\n( 0 384 0 ) ( 1 384 0 ) ( 0 384 1 ) '+textures[0]+' 0 0 0 0.5 0.5 0 0 0')

The third pair of points describes the width of the brush to radiant. The first set of points is
the lower bound of the width description, and the second set of points is the upper bound of the width.
These vertices are -128u on the y axis from the "-y" of the prism, and 64u below the "-z" face of the prism.
"""
