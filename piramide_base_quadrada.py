from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import sys
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

vertices_pi = (
    ( 1, 0,-1),
    ( 1, 0,-2),
    (-1, 0,-2),
    (-1, 0,-1),
)

top_vertex = (0, 1, -1.5)
cor = (0,0.5,0)

def piramid_square_base_hard_coded():
    #Drawing the base
    glBegin(GL_QUADS)
    glColor4f(1,1,1,0.8)
    for v in vertices_pi:
        glVertex3fv(v)
    glEnd()

    #Drawing triangles
    glBegin(GL_TRIANGLE_FAN)
    for v in vertices_pi:
        glVertex3fv(v)
        glVertex3fv(top_vertex)
    glEnd()

    #Drawing lines
    glColor3fv((1,0,0))
    glBegin(GL_LINES)
    for v in vertices_pi:
        glVertex3fv(v)
    glEnd()

    glBegin(GL_LINES)
    for v in vertices_pi:
        glVertex3fv(v)
        glVertex3fv(top_vertex)
    glEnd()

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    piramid_square_base_hard_coded()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Piramid")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.0)
gluPerspective(40,800.0/600.0,0.5,100.0)
glTranslatef(0.0,0,-5)
glRotatef(45,10,10,0)
glutTimerFunc(50,timer,1)
glutMainLoop()