
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
	glClearColor(1.0, 1.0, 1.0, 1.0)
	gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
	

def plotpoints():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 0.0, 0.0)
	glPointSize(100);
	glBegin(GL_POINTS)
	glVertex2f(0.0, 0.0)
	glEnd()
	glFlush()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Plot Points")
	glutDisplayFunc(plotpoints)
	init()
	glutMainLoop()

main()