from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *  
import sys
import time

def init():
    # global quadric
    glClearColor(0.0,0.0,0.0,0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT,GL_NICEST)

def draw():                                            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLineWidth(2.5);
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(3.0,0.0,-15.0)
    posx, posy = 0.1,0.1
    sides = 100000   
    r1 = 1
    glBegin(GL_POLYGON)
    c1=0
    s1=0
    c2=0
    s2=0
    for i in range(100000):
        glColor3f(1.0,0.0,0.0)
        c1= r1 * cos(i*2*pi/sides) + posx    
        s1= r1 * sin(i*2*pi/sides) + posy
        glVertex3f(c1,s1,-15)
    glEnd()
    glBegin(GL_POLYGON)
    for i in range(100000):
        glColor3f(0.0,0.0,1.0)
        c2= r1 * cos(i*2*pi/sides) + posx    
        s2= r1 * sin(i*2*pi/sides) + posy    
        glVertex3f(c2,s2,5)
    glEnd()
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    for i in range(100000):
        c1= r1 * cos(i*2*pi/sides) + posx    
        s1= r1 * sin(i*2*pi/sides) + posy
        glVertex3f(c1,s1,-15)
        c2= r1 * cos(i*2*pi/sides) + posx    
        s2= r1 * sin(i*2*pi/sides) + posy
        glVertex3f(c2,s2,5)
    glEnd
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Plot Points")
    glutDisplayFunc(draw)
    glViewport(0,0,500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(75.0,1.0,1.0,75.0)
    init()
    glutMainLoop()
main()