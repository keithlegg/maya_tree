import maya.cmds as cmds


def makecircle(name):
 return cmds.circle( nr=(0,1,0),n=name )
  
##
def stackloft(stack):
  cmds.select(clear=True)
  for element in stack:
    print element
    cmds.select(element,add=True)
  cmds.loft( ch=False, rn=True, ar=True )

##
def stack(scale,rx,ry,rz,nameofcurve,number):
  output =[]
  movedist = 1 #this will determine branch length
  a = 0

  dupeinit = cmds.duplicate(nameofcurve,name='foo')
  cmds.scale(scale,scale,scale ,dupeinit,relative=True)
  cmds.rotate(rx,ry,rz ,dupeinit,relative=True)

  while a <= number:
   duper = cmds.duplicate(dupeinit,name='foo')
   cmds.move(0,(movedist*a),0, duper, relative=True, objectSpace=True, worldSpaceDistance=True )
   output.append(duper)
   a=a+1

  cmds.delete(dupeinit)
  return output


##
def maketree(curve,depth,maxdepth):
  if depth==maxdepth:
    return 

  numberinstack = 5
  taperfactor   = .7
  slant         = 35

  #trunk
  if depth==0:
   stax = stack(taperfactor,0,0,0,curve,numberinstack)
   laststack= stax[numberinstack]
   stackloft(stax) 

  if depth>0:
   #branchone
   stax = stack(taperfactor,slant ,0  ,0  ,curve,numberinstack)
   laststack= stax[numberinstack]
   #debug
   stackloft(stax) 

   stax = stack(taperfactor,slant ,120,0,curve,numberinstack)
   laststacktwo= stax[numberinstack]
   stackloft(stax) 

   stax = stack(taperfactor,slant ,270,0,curve,numberinstack)
   laststackthree= stax[numberinstack]
   stackloft(stax) 

  maketree(laststack      ,depth+1,maxdepth)

  if depth>0:
   maketree(laststacktwo  ,depth+1,maxdepth)
   maketree(laststackthree,depth+1,maxdepth)

##
foo=makecircle('stack_')
maketree(foo,0,3)
