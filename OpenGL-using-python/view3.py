from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from sys import argv
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0); 
    glClearDepth(1.0);                   
    glEnable(GL_DEPTH_TEST);   
    glDepthFunc(GL_LEQUAL);    
    glShadeModel(GL_SMOOTH);   
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST); 
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); 
    glMatrixMode(GL_MODELVIEW);     
 
   
    glLoadIdentity();                 
    glTranslatef(1.5, 0.0, -7.0);  
 
    glBegin(GL_QUADS);                      
    glColor3f(0.0, 1.0, 0.0);     
    glVertex3f( 1.0, 1.0, -1.0);
    glVertex3f(-1.0, 1.0, -1.0);
    glVertex3f(-1.0, 1.0,  1.0);
    glVertex3f( 1.0, 1.0,  1.0);
 
      
    glColor3f(1.0, 0.5, 0.0);     
    glVertex3f( 1.0, -1.0,  1.0);
    glVertex3f(-1.0, -1.0,  1.0);
    glVertex3f(-1.0, -1.0, -1.0);
    glVertex3f( 1.0, -1.0, -1.0);
 
      
    glColor3f(1.0, 0.0, 0.0);     
    glVertex3f( 1.0,  1.0, 1.0);
    glVertex3f(-1.0,  1.0, 1.0);
    glVertex3f(-1.0, -1.0, 1.0);
    glVertex3f( 1.0, -1.0, 1.0);
 
      
    glColor3f(1.0, 1.0, 0.0);     
    glVertex3f( 1.0, -1.0, -1.0);
    glVertex3f(-1.0, -1.0, -1.0);
    glVertex3f(-1.0,  1.0, -1.0);
    glVertex3f( 1.0,  1.0, -1.0);
 
      
    glColor3f(0.0, 0.0, 1.0);     
    glVertex3f(-1.0,  1.0,  1.0);
    glVertex3f(-1.0,  1.0, -1.0);
    glVertex3f(-1.0, -1.0, -1.0);
    glVertex3f(-1.0, -1.0,  1.0);
 
      
    glColor3f(1.0, 0.0, 1.0);     
    glVertex3f(1.0,  1.0, -1.0);
    glVertex3f(1.0,  1.0,  1.0);
    glVertex3f(1.0, -1.0,  1.0);
    glVertex3f(1.0, -1.0, -1.0);
    glEnd();  
 
   
    glLoadIdentity();                  
    glTranslatef(-1.5, 0.0, -6.0);  
 
    glBegin(GL_TRIANGLES);           
      
    glColor3f(1.0, 0.0, 0.0);     
    glVertex3f( 0.0, 1.0, 0.0);
    glColor3f(0.0, 1.0, 0.0);     
    glVertex3f(-1.0, -1.0, 1.0);
    glColor3f(0.0, 0.0, 1.0);     
    glVertex3f(1.0, -1.0, 1.0);
 
      
    glColor3f(1.0, 0.0, 0.0);     
    glVertex3f(0.0, 1.0, 0.0);
    glColor3f(0.0, 0.0, 1.0);     
    glVertex3f(1.0, -1.0, 1.0);
    glColor3f(0.0, 1.0, 0.0);     
    glVertex3f(1.0, -1.0, -1.0);
 
      
    glColor3f(1.0, 0.0, 0.0);     
    glVertex3f(0.0, 1.0, 0.0);
    glColor3f(0.0, 1.0, 0.0);     
    glVertex3f(1.0, -1.0, -1.0);
    glColor3f(0.0, 0.0, 1.0);     
    glVertex3f(-1.0, -1.0, -1.0);
 
      
    glColor3f(1.0,0.0,0.0);       
    glVertex3f( 0.0, 1.0, 0.0);
    glColor3f(0.0,0.0,1.0);       
    glVertex3f(-1.0,-1.0,-1.0);
    glColor3f(0.0,1.0,0.0);       
    glVertex3f(-1.0,-1.0, 1.0);
    glEnd();   
    glutSwapBuffers();  

def reshape(width, height):
    if height==0:
        height=1                
    aspect=width/height;
 
   
    glViewport(0, 0, width, height);
 
   
    glMatrixMode(GL_PROJECTION);  
    glLoadIdentity();             
    gluPerspective(45.0, aspect, 0.1, 100.0);
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    glMatrixMode(GL_MODELVIEW)
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE); 
    glutInitWindowSize(640, 480);   
    glutInitWindowPosition(50, 50); 
    glutCreateWindow("ABC");          
    glutDisplayFunc(display);       
    glutReshapeFunc(reshape);       
    init();                       
    glutMainLoop();         
    
main()
