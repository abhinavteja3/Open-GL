from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
posx, posy = 0,0
sides = 32
glBegin(GL_POLYGON)
for i in range(100):
    cosine=cos(i*2*pi/sides)+posx
    sine=sin(i*2*pi/sides)+posy
    glVertex2f(cosine,sine)
    print(cosine , sine)
def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    for i in range(100):
    	glVertex2f(cosine , sine)