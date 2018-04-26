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

vertices = (
    (0, 0, 0),
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0)
    )

def piramide_n_lados():
    #Drawing the base
    posx, posy = 0,0
    sides = 50
    radius = 1
    for i in range(1,9999):
        glBegin(GL_POLYGON)
        for v in vertices:
            glVertex3f(v[0] * cos(i) ,v[1],v[2]* sin(i))
        glEnd()

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    piramide_n_lados()
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
glTranslatef(0,0,-4)
glRotatef(45,0,0,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
