from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import sys
from math import *
from ctypes import *
Xlib = CDLL("libX11.so.6")
display = Xlib.XOpenDisplay(None)
(root_id, child_id) = (c_uint32(), c_uint32())
#w = Xlib.XRootWindow(display, c_int(0))
(root_x, root_y, win_x, win_y) = (c_int(), c_int(), c_int(), c_int())
mask = c_uint()

#mouse cursor positions
#ret = Xlib.XQueryPointer(display, c_uint32(w), byref(root_id), byref(child_id), byref(root_x), byref(root_y), byref(win_x), byref(win_y), byref(mask))
#print root_x, root_y#print the values

top_vertex=(1,0,0)

def cilindro():
    #Drawing the base    
    posx, posy = 0,0    
    sides = 3
    radius = 1    
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine = radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

    #Drawing the side
    glBegin(GL_TRIANGLE_STRIP)    
    for i in range(100):    
        cosine = radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy
        glVertex3f(cosine,sine, 0)
        glVertex3f(0,0,-1)
    glEnd()

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    cilindro()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Cone")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.0)
gluPerspective(40,800.0/600.0,0.5,100.0)
glTranslatef(0,0,-10)
glRotatef(95,45,0,0)
glutTimerFunc(50,timer,1)
glutMainLoop()