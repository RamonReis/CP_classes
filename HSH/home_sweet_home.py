from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

# Rotations for cube.
xrot = yrot = zrot = 0.0
dx = 0.1
dy = 0
dz = 0

# texture = []

def LoadTextures():
    global texture_base
    texture_base = glGenTextures(1)
    texture_front = glGenTextures(2)

    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture_base)
    reader = png.Reader(filename='house_pieces_png/base_casa.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

def InitGL(Width, Height):
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    #glDepthFunc(GL_LESS)
    #glEnable(GL_DEPTH_TEST)
    #glShadeModel(GL_SMOOTH)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(25.0, float(Width)/float(Height), 0.1, 0.0)

    glMatrixMode(GL_MODELVIEW)


def DrawHSH():
    global xrot, yrot, zrot, texture_base

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glClearColor(0,0,1,1.0)

    glTranslatef(0.0,0.0,-5.0)


    glBindTexture(GL_TEXTURE_2D, texture_base)
    glBegin(GL_QUADS)

    # Base
    glTexCoord2f(0, 1); glVertex3f(0, 1, 0)
    glTexCoord2f(1, 1); glVertex3f(1, 1, 0)
    glTexCoord2f(1.0, 0.0); glVertex3f(1.0, 0, 0)
    glTexCoord2f(0, 0); glVertex3f( 0, 0, 0)
    


    glEnd()                # Done Drawing The Cube

    glutSwapBuffers()

def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    glutInitWindowSize(800, 600)
    # the window starts at the upper left corner of the screen
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("HSH")
    glutDisplayFunc(DrawHSH)
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawHSH)

    # Register the function called when our window is resized.
    glutReshapeFunc(DrawHSH)

    # Initialize our window.
    InitGL(800, 600)

    # Start Event Processing Engine
    glTranslatef(0.0,0,0)
    #glRotatef(45,10,10,0)
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print "Hit ESC key to quit."
    main()