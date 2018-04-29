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
    global texture
    folder = "house_pieces_png/"
    images = os.listdir(folder)
    images.sort()#The images numbers start on '1' because the number 0 goes to the end of the array when the array is sorted
    texture = glGenTextures(len(images))

    ################################################################################
    
    for i in range(0,len(images)):
        glBindTexture(GL_TEXTURE_2D, texture[i])
        reader = png.Reader(filename=folder+images[i])
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
    glClearDepth(0)
    #glDepthFunc(GL_LESS)
    #glEnable(GL_DEPTH_TEST)
    #glShadeModel(GL_SMOOTH)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 0.0)

    glMatrixMode(GL_MODELVIEW)


def DrawHSH():
    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glClearColor(0,0,1,1.0)

    glTranslatef(-0.6,-0.5,-2.0)
    glRotatef(45,10,0,0)


    # Base
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_QUADS)

    glTexCoord2f(0, 0); glVertex3f(0, 0, -1)
    glTexCoord2f(1, 0); glVertex3f(1, 0, -1)
    glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 0, 0)
    glTexCoord2f(0, 1); glVertex3f( 0, 0, 0)
    
    glEnd()

    # Frente
    glBindTexture(GL_TEXTURE_2D, texture[1])
    glBegin(GL_POLYGON)

    #to finish
    #glTexCoord2f(0, 320/533); glVertex3f(431/990, 0, -1 -(700-553/700) )
    #glTexCoord2f(214/853, 1); glVertex3f(857/990 + 213/853, 213/533 + 0, -1)
    #glTexCoord2f(425/853, 213/533); glVertex3f(1.0, 0, 0)
    #glTexCoord2f(1, 213/533); glVertex3f( 0, 0, 0)
    #glTexCoord2f(0, 1.0); glVertex3f(1.0, 0, 0)
    #glTexCoord2f(0, 0); glVertex3f( 0, 0, 0)
    
    #This homework code will take too much of my time time... =( 

    glEnd()

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
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print "Hit ESC key to quit."
    main()