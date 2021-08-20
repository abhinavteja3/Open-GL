from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import * 
from numpy import *
import sys
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-3.0, 3.0, -3.0, 3.0)   
def stickman():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    posx, posy = 0,0
    sides = 10000
    radius = 0.3
    glLineWidth(4)
    glBegin(GL_LINE_LOOP)    
    for i in range(10000):    
        cosine= radius * cos(i*2*pi/sides) + posx
        sine  = radius * sin(i*2*pi/sides) + posy
        glVertex2f(cosine,sine)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0, -0.3)
    glVertex2f(0, -1.5)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(-0.5 , -0.6)
    glVertex2f(0.5 , -0.6)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0, -1.5)
    glVertex2f(-0.5, -2.0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0, -1.5)
    glVertex2f(0.5, -2.0)
    glEnd()
    glFlush()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("StickMan")
    glutDisplayFunc(stickman)
    init()
    glutMainLoop()
main()