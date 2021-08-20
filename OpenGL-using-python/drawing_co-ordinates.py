# PyFunc.py
# Plotting functions
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    #gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    w,h=500,500
def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)
    # Plot the coordinate axes
    glBegin(GL_LINES)
    glVertex2f(-2.0, 0.0)
    glVertex2f(2.0, 0.0)
    glVertex2f(0.0, 2.0)
    glVertex2f(0.0, -2.0)
    glEnd()
    # Plot the parametric equations
    for t in arange(2,3, 0.01):
        x = sin(t)
        y = cos(t)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()
        glFlush()
# End plotfunc()
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

