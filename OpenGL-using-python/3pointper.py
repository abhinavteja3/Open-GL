from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from sys import argv
import time

def init():
    glClearColor(0.0,0.0,0.0,0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT,GL_NICEST)
    mat_specular = [ 1.0, 1.0, 1.0, 1.0 ];
    mat_shininess = [ 50.0 ];
    light_position = [ 1.0, 1.0, -1.0, 0.0 ];
    red_light = [ 1.0, 1.0, 1.0, 1.0 ];
    lmodel_ambient = [ 0.1, 0.1, 0.1, 1.0 ];
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glShadeModel(GL_SMOOTH);
    glMaterialfv(GL_FRONT,    GL_DIFFUSE, mat_specular);
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess);
    glLightfv(GL_LIGHT0, GL_POSITION, light_position);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, red_light);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, red_light);
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lmodel_ambient);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_DEPTH_TEST);

def draw():                                            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLineWidth(2.5);
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(5.0,-5,-5)
    
    glColor3f(1.0, 0.0, 0.0);
    glBegin(GL_QUADS);

    glColor3f(1.0, 0.0, 0.0);
    
    glVertex3f(-1, 1, -1);
    glVertex3f(1, 1, -1);
    glVertex3f(1, -1, -1);
    glVertex3f(-1, -1, -1);

    glColor3f(0.0, 0.0, 1.0);
    
    glVertex3f(-1, 1, 1);
    glVertex3f(1, 1, 1);
    glVertex3f(1, -1, 1);
    glVertex3f(-1, -1, 1);

    glColor3f(0.0, 1.0, 0.0);
    
    glVertex3f(-1, 1, -1);
    glVertex3f(-1, -1, -1);
    glVertex3f(-1, -1, 1);
    glVertex3f(-1, 1, 1);

    glColor3f(1.0, 0.0, 0.0);
    glVertex3f(-1, 1, -1);
    glVertex3f(1, 1, -1);
    glVertex3f(1, 1, 1);
    glVertex3f(-1, 1, 1);

    glColor3f(1.0, 0.0, 0.0);
    glVertex3f(1, 1, -1);
    glVertex3f(1, -1, -1);
    glVertex3f(1, -1, 1);
    glVertex3f(1, 1, 1);

    glColor3f(1.0, 0.0, 0.0);
    glVertex3f(-1, -1, -1);
    glVertex3f(1, -1, -1);
    glVertex3f(1, -1, 1);
    glVertex3f(-1, -1, 1);

    
    glEnd()
    glutSwapBuffers()      
def reshape(w, h):
    #glViewport(0, 0, w, h)
    #glMatrixMode(GL_PROJECTION)
    #glLoadIdentity()
    #glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    #glMatrixMode(GL_MODELVIEW)
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if w <= h:
        glOrtho(-1.5, 1.5, -1.5*h/w, 1.5*h/w, -10.0, 10.0);
    else:
        glOrtho(-1.5*w/h, 1.5*w/h, -1.5, 1.5, -10.0, 10.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB |GLUT_DEPTH);
    glutInitWindowSize(500,500);
    glutInitWindowPosition(100,100);
    glutCreateWindow(argv[0]);
    
    glViewport(0,0,500,500);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(75.0,1,0.1,25.0);
    
    glRotatef(45,1,0,0)
    glRotatef(45,0,1,0)

    init()
    glutDisplayFunc(draw);
    glutReshapeFunc(display);
    glutMainLoop();
main()
