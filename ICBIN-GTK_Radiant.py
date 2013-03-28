class vec3:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
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

#brush converter here

def brush_to_vector(vec3, vec3):
        start = vec3(x,y,z)
        end = vec3(x2,y2,z2)
        xlength = end.x - start.x
        ylength = end.y - start.y
        zlength = end.z - start.z
                
#initialize variables
textures = ["gothic_block/blocks18c_3"]
entitynum = 0
brushnum = 0

#initialize map file, write first lines
newmap = open("generation.map", "w")
newmap.write('// entity '+str(entitynum)+' \n{ \n"classname" "worldspawn" \n')











#explanation of how radiant actually maps this junk
"""
Rectangular prism example.

newmap.write('\n( 128 0 0 ) ( 128 1 0 ) ( 128 0 1 ) '+textures[0]+' 0 0 0 0.5 0.5 0 0 0')
newmap.write('\n( 256 0 0 ) ( 256 0 1 ) ( 256 1 0 ) '+textures[0]+' 0 0 0 0.5 0.5 0 0 0')

This first pair of points describes the height of the brush to radiant. The first set of points
is the lower bound of the height description, and the second set of points is the upper bound
of the height description. These vertices are -128u on both x & y axis from the bottom left corner
side of the prism, if looking top down at a standard 90 degree view.

newmap.write('\n( 0 128 0 ) ( 0 128 1 ) ( 1 128 0 ) '+textures[0]+' 0 0 0 0.5 0.5 0 0 0')
newmap.write('\n( 0 384 0 ) ( 1 384 0 ) ( 0 384 1 ) '+textures[0]+' 0 0 0 0.5 0.5 0 0 0')

The second pair of points describes the length of the brush to radiant. The first set of points
is the lower bound of the length description, and the second set of points is the upper bound of
the length of the prism. These vertices are -128u on the x axis from the "-x" side of the prism,
and 64u below the "-z" face of the prism.

newmap.write('\n( 0 0 64 ) ( 1 0 64 ) ( 0 1 64 ) '+textures[0]+' 0 0 0 0.5 0.5 0 0 0')
newmap.write('\n( 0 0 128 ) ( 0 1 128 ) ( 1 0 128 ) '+textures[0]+' 0 0 0 0.5 0.5 0 0 0\n}')

The third pair of points describes the width of the brush to radiant. The first set of points is
the lower bound of the width description, and the second set of points is the upper bound of the width.
These vertices are -128u on the y axis from the "-y" of the prism, and 64u below the "-z" face of the prism.
"""
