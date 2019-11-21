import OpenGL
import OpenGL.GLUT
import OpenGL.GLU

import math
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL.ARB.shader_objects import *
from OpenGL.GL.ARB.fragment_shader import *
from OpenGL.GL.ARB.vertex_shader import *

Xi = 0.0        #    # Translate screen to x direction (left or right)
Yi = 0.0            # Translate screen to y direction (up or down)
Zi = 0.0            # Translate screen to z direction (zoom in or out)
rotXi = 0.0        # Rotate screen on x axis
rotYi = 0.0        # Rotate screen on y axis
rotZi = 0.0        # Rotate screen on z axis

rotLxi = 0.0    #   # Translate screen by using #  # the glulookAt function (left or right)
rotLyi = 0.0       # Translate screen by using
#  # the glulookAt function (up or down)
rotLzi = 0.0       # Translate screen by using
#  # the glulookAt function (zoom in or out)
lines = True           # Display x,y,z lines (coordinate lines)
rotation = False       # Rotate if F2 is pressed
old_x =0
old_y=0            # Used for mouse event
mousePressed =0

X = 0.0        #    # Translate screen to x direction (left or right)
Y = 0.0            # Translate screen to y direction (up or down)
Z = 0.0            # Translate screen to z direction (zoom in or out)
rotX = 0.0        # Rotate screen on x axis
rotY = 0.0        # Rotate screen on y axis
rotZ = 0.0        # Rotate screen on z axis

rotLx = 0.0    #   # Translate screen by using #  # the glulookAt function (left or right)
rotLy = 0.0       # Translate screen by using
#  # the glulookAt function (up or down)
rotLz = 0.0       # Translate screen by using
#  # the glulookAt function (zoom in or out)
         # Display x,y,z lines (coordinate lines)


def initGL():
    glShadeModel(GL_SMOOTH)       # Set the shading model to smooth
    glClearColor(0, 0, 0, 1.0)  # Clear the Color
    glClear(GL_COLOR_BUFFER_BIT |  GL_DEPTH_BUFFER_BIT)     # Clear the
    # Color and Depth Buffer
    glClearDepth(1.0)           # Set the Depth buffer value (ranges[0,1])
    glEnable(GL_DEPTH_TEST)   # Enable Depth test
    glDepthFunc(GL_LEQUAL)    # If two objects on the same
    # coordinate show the first drawn
    glHint(GL_PERSPECTIVE_CORRECTION_HINT,  GL_NICEST)
    glDisable(GL_CULL_FACE)


def setWindow(width,height):
    glMatrixMode(GL_PROJECTION) # Set the Matrix mode
    glLoadIdentity()
    gluPerspective(75.0, width/height, 0.10, 500.0)    # Set the perspective
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():

    widthA = glutGet(GLUT_WINDOW_WIDTH)   # Get the windows width
    heightA = glutGet(GLUT_WINDOW_HEIGHT) # Get the windows height
    width = int((widthA+1)/3)
    height = int((heightA+1)/4)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  ## Clear Colo# and Depth Buffer
    widthA = int(widthA)

    glEnable(GL_SCISSOR_TEST)      # Enable Scissor Test for multiple view

    glViewport(0,height*2,widthA,height*2)
    glScissor(0,height*2,widthA,height*2)
    setWindow(widthA,height*2)
    gluLookAt(1.0 , 0.0 , 15.0 , 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)   # Look at the new window at this position
    drawCubeB()

    # First window (Front view)
    glViewport(0, height, width, height)                   # Set the viewPort
    glScissor(0, height, width, height)                    # Divide the window
    setWindow(width, height)
    gluLookAt(1.0 , 0.0 , 15.0 , 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)   # Look at the new window at this position
    drawCube()         # Draw the cube
    #glRasterPos3f(-15, 19, -15)     # Set the position for the string (text)
    #text("Front")   # Display the text "Front"

    # Second Window (Back View)
    glViewport(0, 0, width, height)
    glScissor(0, 0, width, height)
    setWindow(width, height)
    gluLookAt(0.0, 0.0 , -15.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    drawCube()
    #glRasterPos3f(15.0 , 19.0 , 15.0)
   # text("Back")

    # Third window (Right View)
    glViewport(width, height, width, height)
    glScissor(width, height, width, height)
    setWindow(width, height)
    gluLookAt(15.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    drawCube()
    #glRasterPos3f(-15.0, 19.0, 15.0)
    #text("Right")

    # Forth Window (Left View)
    glViewport(width, 0, width, height)
    glScissor(width, 0, width, height)
    setWindow(width, height)
    gluLookAt(-15.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    drawCube()
    #glRasterPos3f(15.0, 19.0, -15.0)
    #text("Left")

    # Fifth window (Upside down view)
    glViewport(2 * width, height, width, height)
    glScissor(2 * width, height, width, height)
    setWindow(width, height)
    gluLookAt(0.0 , 15.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
    drawCube()
    #glRasterPos3f(-15.0, -15.0, -19.0)
    #text("Up")

    # Sixth window bottom up view
    glViewport(2 * width, 0, width, height)
    glScissor(2 * width, 0, width, height)
    setWindow(width, height)
    gluLookAt(1.0, -15.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
    drawCube()
   # glRasterPos3f(15.0, 15.0, -19.0)
   # text("Bottom")

    glDisable(GL_SCISSOR_TEST)
    glutSwapBuffers()

def drawCube():
    global X,Y,Z,rotX,rotY,rotZ,rotLx,rotLy,rotLz,lines,rotation,old_x,old_y, mousePressed
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()  	# It is important to push the Matrix
    # before calling glRotatef and glTranslatef
    glRotatef(rotX, 1.0, 0.0, 0.0)             # Rotate on x
    glRotatef(rotY, 0.0, 1.0, 0.0)             # Rotate on y
    glRotatef(rotZ, 0.0, 0.0, 1.0)             # Rotate on z

    if rotation: # If F2 is pressed update x,y,z for rotation of the cube
        rotX += 0.2
        rotY += 0.2
        rotZ += 0.2


    glTranslatef(X, Y, Z)         # Translates the screen left or right,
        # up or down or zoom in zoom out

    if lines:  # If F1 is pressed don't draw the lines
    # Draw the positive side of the lines x,y,z
        glBegin(GL_LINES)
        glColor3f(0.0, 1.0, 0.0)                 # Green for x axis
        glVertex3f(0, 0, 0)
        glVertex3f(10, 0, 0)
        glColor3f(1.0, 0.0, 0.0)                 # Red for y axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, 10, 0)
        glColor3f(0.0, 0.0, 1.0)                 # Blue for z axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 10)
        glEnd()

        # Dotted lines for the negative sides of x,y,z coordinates
        glEnable(GL_LINE_STIPPLE) # Enable line stipple to use
                # a dotted pattern for the lines
        glLineStipple(1, 0x0101)      # Dotted stipple pattern for the lines
        glBegin(GL_LINES)
        glColor3f(0.0, 1.0, 0.0)                     # Green for x axis
        glVertex3f(-10, 0, 0)
        glVertex3f(0, 0, 0)
        glColor3f(1.0, 0.0, 0.0)                     # Red for y axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, -10, 0)
        glColor3f(0.0, 0.0, 1.0)                     # Blue for z axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, -10)
        glEnd()
        glDisable(GL_LINE_STIPPLE)              # Disable the line stipple


    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)              # Set color to blue
    glVertex3f(3.0, 3.0, 3.0)
    glColor3f(1.0, 0.0, 0.0)              # Set color to red
    glVertex3f(3.0, -3.0, 3.0)
    glColor3f(0.0,0.0, 1.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-3.0, 3.0, 3.0)
    glEnd()

    # Back side
    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.0, .0)
    glVertex3f(3.0, 3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, -3.0, -3.0)
    glColor3f(0.5, 0.0, 0.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glEnd()

    # Right side
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(3.0, 3.0, 3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, 3.0, -3.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(3.0, -3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, -3.0, 3.0)
    glEnd()

    # Left Side
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, 3.0, 3.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glEnd()

    # Upside
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, 3.0, 3.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(3.0, 3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-3.0, 3.0, 3.0)
    glEnd()

    # Bottom
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(3.0, -3.0, 3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, -3.0, -3.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glEnd()
    glColor3f(1.0, 0.5, 0.5)
    glPopMatrix()
    glutPostRedisplay()    # Redraw the scene

def drawCubeB():
    glMatrixMode(GL_PROJECTION)
    global Xi,Yi,Zi,rotXi,rotYi,rotZi,rotLxi,rotLyi,rotLzi,lines
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()  	# It is important to push the Matrix
    # before calling glRotatef and glTranslatef
    glRotatef(rotXi, 1.0, 0.0, 0.0)             # Rotate on x
   # glRotatef(rotYi, 0.0, 1.0, 0.0)             # Rotate on y
    glRotatef(rotZi, 0.0, 0.0, 1.0)             # Rotate on z



    glTranslatef(Xi, Yi, Zi)         # Translates the screen left or right,
        # up or down or zoom in zoom out

    if lines:  # If F1 is pressed don't draw the lines
    # Draw the positive side of the lines x,y,z
        glBegin(GL_LINES)
        glColor3f(0.0, 1.0, 0.0)                 # Green for x axis
        glVertex3f(0, 0, 0)
        glVertex3f(10, 0, 0)
        glColor3f(1.0, 0.0, 0.0)                 # Red for y axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, 10, 0)
        glColor3f(0.0, 0.0, 1.0)                 # Blue for z axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 10)
        glEnd()

        # Dotted lines for the negative sides of x,y,z coordinates
        glEnable(GL_LINE_STIPPLE) # Enable line stipple to use
                # a dotted pattern for the lines
        glLineStipple(1, 0x0101)      # Dotted stipple pattern for the lines
        glBegin(GL_LINES)
        glColor3f(0.0, 1.0, 0.0)                     # Green for x axis
        glVertex3f(-10, 0, 0)
        glVertex3f(0, 0, 0)
        glColor3f(1.0, 0.0, 0.0)                     # Red for y axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, -10, 0)
        glColor3f(0.0, 0.0, 1.0)                     # Blue for z axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, -10)
        glEnd()
        glDisable(GL_LINE_STIPPLE)              # Disable the line stipple


    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)              # Set color to blue
    glVertex3f(3.0, 3.0, 3.0)
    glColor3f(1.0, 0.0, 0.0)              # Set color to red
    glVertex3f(3.0, -3.0, 3.0)
    glColor3f(0.0,0.0, 1.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-3.0, 3.0, 3.0)
    glEnd()

    # Back side
    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.0, .0)
    glVertex3f(3.0, 3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, -3.0, -3.0)
    glColor3f(0.5, 0.0, 0.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glEnd()

    # Right side
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(3.0, 3.0, 3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, 3.0, -3.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(3.0, -3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, -3.0, 3.0)
    glEnd()

    # Left Side
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, 3.0, 3.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glEnd()

    # Upside
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, 3.0, 3.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(3.0, 3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-3.0, 3.0, 3.0)
    glEnd()

    # Bottom
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(3.0, -3.0, 3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, -3.0, -3.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glEnd()
    glColor3f(1.0, 0.5, 0.5)
    glPopMatrix()
    drawBackground()
    glutPostRedisplay()    # Redraw the scene

def drawBackground():
    global Xi,Yi,Zi,rotXi,rotYi,rotZi,rotLxi,rotLyi,rotLzi,lines

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glRotatef(rotYi, 0.0, 1.0, 0.0)

    glBegin(GL_POLYGON)            # Rotate on y
    glColor3f(0.0, 0.0, 1.0)              # Set color to blue
    glVertex3f(3.0*100, 3.0*100, 3.0*100)
    glColor3f(1.0, 0.0, 0.0)              # Set color to red
    glVertex3f(3.0*100, -3.0*100, 3.0*100)
    glColor3f(0.0,0.0, 1.0)
    glVertex3f(-3.0*100, -3.0*100, 3.0*100)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-3.0*100, 3.0*100, 3.0*100)
    glEnd()

    # Back side
    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.0, .0)
    glVertex3f(3.0*100, 3.0*100, -3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0*100, -3.0*100, -3.0*100)
    glColor3f(0.5, 0.0, 0.0)
    glVertex3f(-3.0*100, -3.0*100, -3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0*100, 3.0*100, -3.0*100)
    glEnd()

    # Right side
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(3.0*100, 3.0*100, 3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0*100, 3.0*100, -3.0*100)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(3.0*100, -3.0*100, -3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0*100, -3.0*100, 3.0*100)
    glEnd()

    # Left Side
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0*100, 3.0*100, 3.0*100)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-3.0*100, -3.0*100, 3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0*100, -3.0*100, -3.0*100)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-3.0*100, 3.0*100, -3.0*100)
    glEnd()

    # Upside
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0*100, 3.0*100, 3.0*100)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(3.0*100, 3.0*100, -3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0*100, 3.0*100, -3.0*100)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-3.0*100, 3.0*100, 3.0*100)
    glEnd()

    # Bottom
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(3.0*100, -3.0*100, 3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0*100, -3.0*100, -3.0*100)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-3.0*100, -3.0*100, -3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0*100, -3.0*100, 3.0*100)
    glEnd()
    glColor3f(1.0, 0.5, 0.5)
    glPopMatrix()
    glutPostRedisplay()

def reshape(w,h):
    global X,Y,Z,rotX,rotY,rotZ,rotLx,rotLy,rotLz,lines,rotation,old_x,old_y, mousePressed
    w = glutGet(GLUT_WINDOW_WIDTH)   # Get the windows width
    h = glutGet(GLUT_WINDOW_HEIGHT)
    glClearColor(0, 0, 0, 0.0)
    glViewport(0, 0, w, h)                 # Set the viewport
    glMatrixMode(GL_PROJECTION)         # Set the Matrix mode
    glLoadIdentity()
    gluPerspective(75, w/h, 0.10, 500.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def keyboard(bkey, x, y):
    global X,Y,Z,rotX,rotY,rotZ,rotLx,rotLy,rotLz,lines,rotation,old_x,old_y, mousePressed
    key = bkey.decode("utf-8")
    if key == 'x':    # x           # Rotates screen on x axis
        rotX -= 2.0

    if key == 'X':    # X            	# Opposite way
        rotX += 2.0

    if key == 'y':    # y            	# Rotates screen on y axis
        rotY -= 2.0

    if key == 'Y':    # Y           	# Opposite way
        rotY += 2.0

    if key == 'z':    # z            	# Rotates screen on z axis
        rotZ -= 2.0

    if key == 'Z':    # Z            	# Opposite way
        rotZ += 2.0

    # j,J,k,K,l,L uses the gluLookAt function for navigation
    if key == 'j':   # j
        rotLx -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'J':    # J
        rotLx += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'k':   # k
        rotLy -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'K':    # K
        rotLy += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'l': 	# (l) It has a special  if key == when the rotLZ becames less
    # than -15 the screen is viewed from the opposite side
    # therefore this if statement below does not allow
    # rotLz be less than -15
        if (rotLz + 14 >= 0):
            rotLz -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'L':    # L
        rotLz += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'b':    # b        # Rotates on x axis by -90 degree
        rotX -= 90.0

    if key == 'B':    # B        # Rotates on y axis by 90 degree
        rotX += 90.0

    if key == 'n':    # n       # Rotates on y axis by -90 degree
        rotY -= 90.0

    if key == 'N':    # N        # Rotates on y axis by 90 degree
        rotY += 90.0

    if key == 'm':    # m       # Rotates on z axis by -90 degree
        rotZ -= 90.0

    if key == 'M':    # M        # Rotates on z axis by 90 degree
        rotZ += 90.0


    if key == 'O':    # O        # Displays the cube in the starting position
        rotation = False
        X = Y = 0.0
        Z = 0.0
        rotX = 0.0
        rotY = 0.0
        rotZ = 0.0
        rotLx = 0.0
        rotLy = 0.0
        rotLz = 0.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0)
    glutPostRedisplay()

def keyboard(bkey, x, y):
    global X,Y,Z,rotX,rotY,rotZ,rotLx,rotLy,rotLz,lines,rotation,old_x,old_y, mousePressed
    key = bkey.decode("utf-8")
    if key == 'x':    # x           # Rotates screen on x axis
        rotX -= 2.0

    if key == 'X':    # X            	# Opposite way
        rotX += 2.0

    if key == 'y':    # y            	# Rotates screen on y axis
        rotY -= 2.0

    if key == 'Y':    # Y           	# Opposite way
        rotY += 2.0

    if key == 'z':    # z            	# Rotates screen on z axis
        rotZ -= 2.0

    if key == 'Z':    # Z            	# Opposite way
        rotZ += 2.0

    # j,J,k,K,l,L uses the gluLookAt function for navigation
    if key == 'j':   # j
        rotLx -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'J':    # J
        rotLx += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'k':   # k
        rotLy -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'K':    # K
        rotLy += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'l': 	# (l) It has a special  if key == when the rotLZ becames less
    # than -15 the screen is viewed from the opposite side
    # therefore this if statement below does not allow
    # rotLz be less than -15
        if (rotLz + 14 >= 0):
            rotLz -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'L':    # L
        rotLz += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'b':    # b        # Rotates on x axis by -90 degree
        rotX -= 90.0

    if key == 'B':    # B        # Rotates on y axis by 90 degree
        rotX += 90.0

    if key == 'n':    # n       # Rotates on y axis by -90 degree
        rotY -= 90.0

    if key == 'N':    # N        # Rotates on y axis by 90 degree
        rotY += 90.0

    if key == 'm':    # m       # Rotates on z axis by -90 degree
        rotZ -= 90.0

    if key == 'M':    # M        # Rotates on z axis by 90 degree
        rotZ += 90.0


    if key == 'O':    # O        # Displays the cube in the starting position
        rotation = False
        X = Y = 0.0
        Z = 0.0
        rotX = 0.0
        rotY = 0.0
        rotZ = 0.0
        rotLx = 0.0
        rotLy = 0.0
        rotLz = 0.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0)
    glutPostRedisplay()

def specialKey(key,x,y):
    global X,Y,Z,rotX,rotY,rotZ,rotLx,rotLy,rotLz,lines,rotation,old_x,old_y, mousePressed
    if key==GLUT_KEY_LEFT:
        X-=2.0
    if key==GLUT_KEY_RIGHT:
        X+=2.0

    if key == GLUT_KEY_UP:
        Y+=2.0

    if key==GLUT_KEY_DOWN:
        Y-=2.0

    if key==GLUT_KEY_PAGE_UP:
        Z-=2.0

    if key == GLUT_KEY_PAGE_DOWN:
        Z+=2.0

    if key == GLUT_KEY_F1:
        lines = not lines

    if key == GLUT_KEY_F2:
        rotation = not rotation

    glutPostRedisplay()

def timer(a):
    global Xi,Yi,Zi,rotXi,rotYi,rotZi,rotLxi,rotLyi,rotLzi,lines
    glutPostRedisplay()
    rotYi +=0.5
    glutTimerFunc(16,timer,0)




def initGL():
    glShadeModel(GL_SMOOTH)       # Set the shading model to smooth
    glClearColor(0, 0, 0, 1.0)  # Clear the Color
    glClear(GL_COLOR_BUFFER_BIT |  GL_DEPTH_BUFFER_BIT)     # Clear the
    # Color and Depth Buffer
    glClearDepth(1.0)           # Set the Depth buffer value (ranges[0,1])
    glEnable(GL_DEPTH_TEST)   # Enable Depth test
    glDepthFunc(GL_LEQUAL)    # If two objects on the same
    # coordinate show the first drawn
    glHint(GL_PERSPECTIVE_CORRECTION_HINT,  GL_NICEST)
    glDisable(GL_CULL_FACE)


def setWindow(width,height):
    glMatrixMode(GL_PROJECTION) # Set the Matrix mode
    glLoadIdentity()
    gluPerspective(75.0, width/height, 0.10, 500.0)    # Set the perspective
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():

    widthA = glutGet(GLUT_WINDOW_WIDTH)   # Get the windows width
    heightA = glutGet(GLUT_WINDOW_HEIGHT) # Get the windows height
    width = int((widthA+1)/3)
    height = int((heightA+1)/4)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  ## Clear Colo# and Depth Buffer
    widthA = int(widthA)

    glEnable(GL_SCISSOR_TEST)      # Enable Scissor Test for multiple view

    glViewport(0,height*2,widthA,height*2)
    glScissor(0,height*2,widthA,height*2)
    setWindow(widthA,height*2)
    gluLookAt(1.0 , 0.0 , 15.0 , 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)   # Look at the new window at this position
    drawCubeB()

    # First window (Front view)
    glViewport(0, height, width, height)                   # Set the viewPort
    glScissor(0, height, width, height)                    # Divide the window
    setWindow(width, height)
    gluLookAt(1.0 , 0.0 , 15.0 , 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)   # Look at the new window at this position
    drawCube()         # Draw the cube
    #glRasterPos3f(-15, 19, -15)     # Set the position for the string (text)
    #text("Front")   # Display the text "Front"

    # Second Window (Back View)
    glViewport(0, 0, width, height)
    glScissor(0, 0, width, height)
    setWindow(width, height)
    gluLookAt(0.0, 0.0 , -15.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    drawCube()
    #glRasterPos3f(15.0 , 19.0 , 15.0)
   # text("Back")

    # Third window (Right View)
    glViewport(width, height, width, height)
    glScissor(width, height, width, height)
    setWindow(width, height)
    gluLookAt(15.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    drawCube()
    #glRasterPos3f(-15.0, 19.0, 15.0)
    #text("Right")

    # Forth Window (Left View)
    glViewport(width, 0, width, height)
    glScissor(width, 0, width, height)
    setWindow(width, height)
    gluLookAt(-15.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    drawCube()
    #glRasterPos3f(15.0, 19.0, -15.0)
    #text("Left")

    # Fifth window (Upside down view)
    glViewport(2 * width, height, width, height)
    glScissor(2 * width, height, width, height)
    setWindow(width, height)
    gluLookAt(0.0 , 15.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
    drawCube()
    #glRasterPos3f(-15.0, -15.0, -19.0)
    #text("Up")

    # Sixth window bottom up view
    glViewport(2 * width, 0, width, height)
    glScissor(2 * width, 0, width, height)
    setWindow(width, height)
    gluLookAt(1.0, -15.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
    drawCube()
   # glRasterPos3f(15.0, 15.0, -19.0)
   # text("Bottom")

    glDisable(GL_SCISSOR_TEST)
    glutSwapBuffers()

def drawCube():
    global X,Y,Z,rotX,rotY,rotZ,rotLx,rotLy,rotLz,lines,rotation,old_x,old_y, mousePressed
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()  	# It is important to push the Matrix
    # before calling glRotatef and glTranslatef
    glRotatef(rotX, 1.0, 0.0, 0.0)             # Rotate on x
    glRotatef(rotY, 0.0, 1.0, 0.0)             # Rotate on y
    glRotatef(rotZ, 0.0, 0.0, 1.0)             # Rotate on z

    if rotation: # If F2 is pressed update x,y,z for rotation of the cube
        rotX += 0.2
        rotY += 0.2
        rotZ += 0.2


    glTranslatef(X, Y, Z)         # Translates the screen left or right,
        # up or down or zoom in zoom out

    if lines:  # If F1 is pressed don't draw the lines
    # Draw the positive side of the lines x,y,z
        glBegin(GL_LINES)
        glColor3f(0.0, 1.0, 0.0)                 # Green for x axis
        glVertex3f(0, 0, 0)
        glVertex3f(10, 0, 0)
        glColor3f(1.0, 0.0, 0.0)                 # Red for y axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, 10, 0)
        glColor3f(0.0, 0.0, 1.0)                 # Blue for z axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 10)
        glEnd()

        # Dotted lines for the negative sides of x,y,z coordinates
        glEnable(GL_LINE_STIPPLE) # Enable line stipple to use
                # a dotted pattern for the lines
        glLineStipple(1, 0x0101)      # Dotted stipple pattern for the lines
        glBegin(GL_LINES)
        glColor3f(0.0, 1.0, 0.0)                     # Green for x axis
        glVertex3f(-10, 0, 0)
        glVertex3f(0, 0, 0)
        glColor3f(1.0, 0.0, 0.0)                     # Red for y axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, -10, 0)
        glColor3f(0.0, 0.0, 1.0)                     # Blue for z axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, -10)
        glEnd()
        glDisable(GL_LINE_STIPPLE)              # Disable the line stipple


    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)              # Set color to blue
    glVertex3f(3.0, 3.0, 3.0)
    glColor3f(1.0, 0.0, 0.0)              # Set color to red
    glVertex3f(3.0, -3.0, 3.0)
    glColor3f(0.0,0.0, 1.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-3.0, 3.0, 3.0)
    glEnd()

    # Back side
    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.0, .0)
    glVertex3f(3.0, 3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, -3.0, -3.0)
    glColor3f(0.5, 0.0, 0.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glEnd()

    # Right side
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(3.0, 3.0, 3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, 3.0, -3.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(3.0, -3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, -3.0, 3.0)
    glEnd()

    # Left Side
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, 3.0, 3.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glEnd()

    # Upside
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, 3.0, 3.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(3.0, 3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-3.0, 3.0, 3.0)
    glEnd()

    # Bottom
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(3.0, -3.0, 3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, -3.0, -3.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glEnd()
    glColor3f(1.0, 0.5, 0.5)
    glPopMatrix()
    glutPostRedisplay()    # Redraw the scene

def drawCubeB():
    glMatrixMode(GL_PROJECTION)
    global Xi,Yi,Zi,rotXi,rotYi,rotZi,rotLxi,rotLyi,rotLzi,lines
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()  	# It is important to push the Matrix
    # before calling glRotatef and glTranslatef
    glRotatef(rotXi, 1.0, 0.0, 0.0)             # Rotate on x
   # glRotatef(rotYi, 0.0, 1.0, 0.0)             # Rotate on y
    glRotatef(rotZi, 0.0, 0.0, 1.0)             # Rotate on z



    glTranslatef(Xi, Yi, Zi)         # Translates the screen left or right,
        # up or down or zoom in zoom out

    if lines:  # If F1 is pressed don't draw the lines
    # Draw the positive side of the lines x,y,z
        glBegin(GL_LINES)
        glColor3f(0.0, 1.0, 0.0)                 # Green for x axis
        glVertex3f(0, 0, 0)
        glVertex3f(10, 0, 0)
        glColor3f(1.0, 0.0, 0.0)                 # Red for y axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, 10, 0)
        glColor3f(0.0, 0.0, 1.0)                 # Blue for z axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 10)
        glEnd()

        # Dotted lines for the negative sides of x,y,z coordinates
        glEnable(GL_LINE_STIPPLE) # Enable line stipple to use
                # a dotted pattern for the lines
        glLineStipple(1, 0x0101)      # Dotted stipple pattern for the lines
        glBegin(GL_LINES)
        glColor3f(0.0, 1.0, 0.0)                     # Green for x axis
        glVertex3f(-10, 0, 0)
        glVertex3f(0, 0, 0)
        glColor3f(1.0, 0.0, 0.0)                     # Red for y axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, -10, 0)
        glColor3f(0.0, 0.0, 1.0)                     # Blue for z axis
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, -10)
        glEnd()
        glDisable(GL_LINE_STIPPLE)              # Disable the line stipple


    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)              # Set color to blue
    glVertex3f(3.0, 3.0, 3.0)
    glColor3f(1.0, 0.0, 0.0)              # Set color to red
    glVertex3f(3.0, -3.0, 3.0)
    glColor3f(0.0,0.0, 1.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-3.0, 3.0, 3.0)
    glEnd()

    # Back side
    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.0, .0)
    glVertex3f(3.0, 3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, -3.0, -3.0)
    glColor3f(0.5, 0.0, 0.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glEnd()

    # Right side
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(3.0, 3.0, 3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, 3.0, -3.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(3.0, -3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, -3.0, 3.0)
    glEnd()

    # Left Side
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, 3.0, 3.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glEnd()

    # Upside
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, 3.0, 3.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(3.0, 3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, 3.0, -3.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-3.0, 3.0, 3.0)
    glEnd()

    # Bottom
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(3.0, -3.0, 3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0, -3.0, -3.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-3.0, -3.0, -3.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0, -3.0, 3.0)
    glEnd()
    glColor3f(1.0, 0.5, 0.5)
    glPopMatrix()
    drawBackground()
    glutPostRedisplay()    # Redraw the scene

def drawBackground():
    global Xi,Yi,Zi,rotXi,rotYi,rotZi,rotLxi,rotLyi,rotLzi,lines

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glRotatef(rotYi, 0.0, 1.0, 0.0)

    glBegin(GL_POLYGON)            # Rotate on y
    glColor3f(0.0, 0.0, 1.0)              # Set color to blue
    glVertex3f(3.0*100, 3.0*100, 3.0*100)
    glColor3f(1.0, 0.0, 0.0)              # Set color to red
    glVertex3f(3.0*100, -3.0*100, 3.0*100)
    glColor3f(0.0,0.0, 1.0)
    glVertex3f(-3.0*100, -3.0*100, 3.0*100)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-3.0*100, 3.0*100, 3.0*100)
    glEnd()

    # Back side
    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.0, .0)
    glVertex3f(3.0*100, 3.0*100, -3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0*100, -3.0*100, -3.0*100)
    glColor3f(0.5, 0.0, 0.0)
    glVertex3f(-3.0*100, -3.0*100, -3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0*100, 3.0*100, -3.0*100)
    glEnd()

    # Right side
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(3.0*100, 3.0*100, 3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0*100, 3.0*100, -3.0*100)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(3.0*100, -3.0*100, -3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0*100, -3.0*100, 3.0*100)
    glEnd()

    # Left Side
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0*100, 3.0*100, 3.0*100)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-3.0*100, -3.0*100, 3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0*100, -3.0*100, -3.0*100)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-3.0*100, 3.0*100, -3.0*100)
    glEnd()

    # Upside
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0*100, 3.0*100, 3.0*100)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(3.0*100, 3.0*100, -3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0*100, 3.0*100, -3.0*100)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-3.0*100, 3.0*100, 3.0*100)
    glEnd()

    # Bottom
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(3.0*100, -3.0*100, 3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(3.0*100, -3.0*100, -3.0*100)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-3.0*100, -3.0*100, -3.0*100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-3.0*100, -3.0*100, 3.0*100)
    glEnd()
    glColor3f(1.0, 0.5, 0.5)
    glPopMatrix()
    glutPostRedisplay()

def reshape(w,h):
    global X,Y,Z,rotX,rotY,rotZ,rotLx,rotLy,rotLz,lines,rotation,old_x,old_y, mousePressed
    w = glutGet(GLUT_WINDOW_WIDTH)   # Get the windows width
    h = glutGet(GLUT_WINDOW_HEIGHT)
    glClearColor(0, 0, 0, 0.0)
    glViewport(0, 0, w, h)                 # Set the viewport
    glMatrixMode(GL_PROJECTION)         # Set the Matrix mode
    glLoadIdentity()
    gluPerspective(75, w/h, 0.10, 500.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def keyboard(bkey, x, y):
    global X,Y,Z,rotX,rotY,rotZ,rotLx,rotLy,rotLz,lines,rotation,old_x,old_y, mousePressed
    key = bkey.decode("utf-8")
    if key == 'x':    # x           # Rotates screen on x axis
        rotX -= 2.0

    if key == 'X':    # X            	# Opposite way
        rotX += 2.0

    if key == 'y':    # y            	# Rotates screen on y axis
        rotY -= 2.0

    if key == 'Y':    # Y           	# Opposite way
        rotY += 2.0

    if key == 'z':    # z            	# Rotates screen on z axis
        rotZ -= 2.0

    if key == 'Z':    # Z            	# Opposite way
        rotZ += 2.0

    # j,J,k,K,l,L uses the gluLookAt function for navigation
    if key == 'j':   # j
        rotLx -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'J':    # J
        rotLx += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'k':   # k
        rotLy -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'K':    # K
        rotLy += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'l': 	# (l) It has a special  if key == when the rotLZ becames less
    # than -15 the screen is viewed from the opposite side
    # therefore this if statement below does not allow
    # rotLz be less than -15
        if (rotLz + 14 >= 0):
            rotLz -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'L':    # L
        rotLz += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'b':    # b        # Rotates on x axis by -90 degree
        rotX -= 90.0

    if key == 'B':    # B        # Rotates on y axis by 90 degree
        rotX += 90.0

    if key == 'n':    # n       # Rotates on y axis by -90 degree
        rotY -= 90.0

    if key == 'N':    # N        # Rotates on y axis by 90 degree
        rotY += 90.0

    if key == 'm':    # m       # Rotates on z axis by -90 degree
        rotZ -= 90.0

    if key == 'M':    # M        # Rotates on z axis by 90 degree
        rotZ += 90.0


    if key == 'O':    # O        # Displays the cube in the starting position
        rotation = False
        X = Y = 0.0
        Z = 0.0
        rotX = 0.0
        rotY = 0.0
        rotZ = 0.0
        rotLx = 0.0
        rotLy = 0.0
        rotLz = 0.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0)
    glutPostRedisplay()

def keyboard(bkey, x, y):
    global X,Y,Z,rotX,rotY,rotZ,rotLx,rotLy,rotLz,lines,rotation,old_x,old_y, mousePressed
    key = bkey.decode("utf-8")
    if key == 'x':    # x           # Rotates screen on x axis
        rotX -= 2.0

    if key == 'X':    # X            	# Opposite way
        rotX += 2.0

    if key == 'y':    # y            	# Rotates screen on y axis
        rotY -= 2.0

    if key == 'Y':    # Y           	# Opposite way
        rotY += 2.0

    if key == 'z':    # z            	# Rotates screen on z axis
        rotZ -= 2.0

    if key == 'Z':    # Z            	# Opposite way
        rotZ += 2.0

    # j,J,k,K,l,L uses the gluLookAt function for navigation
    if key == 'j':   # j
        rotLx -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'J':    # J
        rotLx += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'k':   # k
        rotLy -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'K':    # K
        rotLy += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'l': 	# (l) It has a special  if key == when the rotLZ becames less
    # than -15 the screen is viewed from the opposite side
    # therefore this if statement below does not allow
    # rotLz be less than -15
        if (rotLz + 14 >= 0):
            rotLz -= 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'L':    # L
        rotLz += 2.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if key == 'b':    # b        # Rotates on x axis by -90 degree
        rotX -= 90.0

    if key == 'B':    # B        # Rotates on y axis by 90 degree
        rotX += 90.0

    if key == 'n':    # n       # Rotates on y axis by -90 degree
        rotY -= 90.0

    if key == 'N':    # N        # Rotates on y axis by 90 degree
        rotY += 90.0

    if key == 'm':    # m       # Rotates on z axis by -90 degree
        rotZ -= 90.0

    if key == 'M':    # M        # Rotates on z axis by 90 degree
        rotZ += 90.0


    if key == 'O':    # O        # Displays the cube in the starting position
        rotation = False
        X = Y = 0.0
        Z = 0.0
        rotX = 0.0
        rotY = 0.0
        rotZ = 0.0
        rotLx = 0.0
        rotLy = 0.0
        rotLz = 0.0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(rotLx, rotLy, 15.0 + rotLz, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0)
    glutPostRedisplay()

def specialKey(key,x,y):
    global X,Y,Z,rotX,rotY,rotZ,rotLx,rotLy,rotLz,lines,rotation,old_x,old_y, mousePressed
    if key==GLUT_KEY_LEFT:
        X-=2.0
    if key==GLUT_KEY_RIGHT:
        X+=2.0

    if key == GLUT_KEY_UP:
        Y+=2.0

    if key==GLUT_KEY_DOWN:
        Y-=2.0

    if key==GLUT_KEY_PAGE_UP:
        Z-=2.0

    if key == GLUT_KEY_PAGE_DOWN:
        Z+=2.0

    if key == GLUT_KEY_F1:
        lines = not lines

    if key == GLUT_KEY_F2:
        rotation = not rotation

    glutPostRedisplay()

def timer(a):
    global Xi,Yi,Zi,rotXi,rotYi,rotZi,rotLxi,rotLyi,rotLzi,lines
    glutPostRedisplay()
    rotYi +=0.5
    glutTimerFunc(16,timer,0)


glutInit()       #// Initialize GLUT
glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH) #// Enable double buffered mode
glutInitWindowSize(600, 600)   #// Set the window's initial width & height
glutInitWindowPosition(50, 50)# // Position the window's initial top-left corner
glutCreateWindow("aiuda")       #   // Create window with the given title
glutDisplayFunc(display)      # // Register callback handler for window re-paint event
glutReshapeFunc(reshape)
glutTimerFunc(0,timer,0)
glutKeyboardFunc(keyboard)
glutSpecialFunc(specialKey)  # // to specialKey callback# // Register callback handler for window re-size event
initGL()                      # // Our own OpenGL initialization
glutMainLoop() 
