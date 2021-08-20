from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
print("import success")
w,h =50 ,50
def square():
	glBegin(GL_QUADS)
	glVertex2f(10,10)
	glVertex2f(0,10)
	glVertex2f(10,0)
	glVertex2f(0,0)
	glEnd()
def showScreen():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	square()
	glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500,500)
glutInitWindowPosition(0,0)
wind=glutCreateWindow("OpenGL Practise")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()


