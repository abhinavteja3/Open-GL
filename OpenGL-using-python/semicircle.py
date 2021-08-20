# PyFunc.py
# Plotting functions
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(3.0)
    r = 3.0
    for x in arange(-5.0, 5.0, 0.01):
        y = sqrt(r*r-x*x)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        #glVertex2f(x, y)
        # do we need another glVertex2f statement here?
        glEnd()
        glFlush()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutInitWindowSize(400,400)
    glutCreateWindow("Function Plotter")
    glutDisplayFunc(plotfunc)
    init()
    glutMainLoop()
main()

