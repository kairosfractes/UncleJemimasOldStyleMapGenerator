class vec3:
	def __init__(self, x, y, z):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)
	def __str__(self):
		return "("+str(self.x)+", "+str(self.y)+", "+str(self.z)+")"
	def __len__(self):
		return 3
	def ints(self):
		self.x = round(self.x)
		self.y = round(self.y)
		self.z = round(self.z)
		return self

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

#brush converter here

def vectors2brush(veca, vecb):
	brush = '// brush '+str(brushnum)+'\n{\n('+str(veca.x)+' 0 0) ('+str(veca.x)+' 1 0) ('+str(veca.x)+' 0 1) '+str(textures)[0]+' 0 0 0 0.5 0.5 0 0 0\n ('+str(vecb.x)+' 0 0) ('+str(vecb.x)+' 1 0) ('+str(vecb.x)+' 0 1) '+str(textures[0])+' 0 0 0 0.5 0.5 0 0 0\n ('+str(veca.y)+' 0 0) ('+str(veca.y)+' 1 0) ('+str(veca.y)+' 0 1) '+str(textures[0])+' 0 0 0 0.5 0.5 0 0 0\n ('+str(vecb.y)+' 0 0) ('+str(vecb.y)+' 1 0) ('+str(vecb.y)+' 0 1) '+str(textures[0])+' 0 0 0 0.5 0.5 0 0 0\n ('+str(veca.z)+' 0 0) ('+str(veca.z)+' 1 0) ('+str(veca.z)+' 0 1) '+str(textures[0])+' 0 0 0 0.5 0.5 0 0 0\n ('+str(vecb.z)+' 0 0) ('+str(vecb.z)+' 1 0) ('+str(vecb.z)+' 0 1) '+str(textures[0])+' 0 0 0 0.5 0.5 0 0 0\n}'
	return str(brush)

#initialize variables
textures = ["gothic_block/blocks18c_3"]
entitynum = 0
brushnum = 0

#initialize map file, write first lines
newmap = open("generation.map", "w")
newmap.write('// entity '+str(entitynum)+' \n{ \n"classname" "worldspawn" \n')

#platform test
def platform(vec1, vec2):
        vectors2brush(vec1, vec2)
        return newmap.write(brush)

platform((0,0,0), (512,512,32))

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
