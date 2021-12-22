import sys
import os
import sdl2
import sdl2.ext
import sdl2.sdlttf
from OpenGL import GL, GLU
import ctypes
import math

from frame import Frame
from camera_controller import CameraController
from matrix import Matrix

width, height = 1200, 1000


def drawFrame(frame, font):
    matrix = frame.getGlobalMatrix()
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glPushMatrix()

    matList = [matrix[(j,i)] for i in range(4) for j in range(4)]
    GL.glMultMatrixf(matList)

    GL.glBegin(GL.GL_LINES)
    GL.glColor(1,0,0,1)
    GL.glVertex(0,0,0)
    GL.glVertex(1,0,0)
    GL.glColor(0,1,0,1)
    GL.glVertex(0,0,0)
    GL.glVertex(0,1,0)
    GL.glColor(0,0,1,1)
    GL.glVertex(0,0,0)
    GL.glVertex(0,0,1)
    GL.glEnd()

    RenderText3D(frame.name, font)

    GL.glPopMatrix()


def CreateTextTexture(text, font):
    textures = [0]
    GL.glGenTextures(1, textures)
    GL.glBindTexture(GL.GL_TEXTURE_2D, textures[0])

    surface = sdl2.sdlttf.TTF_RenderText_Blended(font, str.encode(text), sdl2.SDL_Color(255, 255, 255, 255))
    
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
    GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGBA, surface.contents.w, surface.contents.h, 0, GL.GL_BGRA, GL.GL_UNSIGNED_BYTE, ctypes.c_void_p(surface.contents.pixels))

    sdl2.SDL_FreeSurface(surface)
    return textures[0], surface.contents.w, surface.contents.h

def RenderText2D(text, x, y, font):
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glPushMatrix()
    GL.glLoadIdentity()

    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glPushMatrix()
    GL.glLoadIdentity()
    GLU.gluOrtho2D(0, width, 0, height); 

    GL.glDisable(GL.GL_DEPTH_TEST)
    GL.glEnable(GL.GL_TEXTURE_2D)
    GL.glEnable(GL.GL_BLEND)
    GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)

    texture, textureWidth, textureHeight = CreateTextTexture(text, font)
    GL.glBindTexture(GL.GL_TEXTURE_2D, texture)

    GL.glBegin(GL.GL_QUADS)
    GL.glColor(1,1,1,1)
    GL.glTexCoord2f(0,1); GL.glVertex2f(x, y)
    GL.glTexCoord2f(1,1); GL.glVertex2f(x + textureWidth, y)
    GL.glTexCoord2f(1,0); GL.glVertex2f(x + textureWidth, y + textureHeight)
    GL.glTexCoord2f(0,0); GL.glVertex2f(x, y + textureHeight)
    GL.glEnd()
    
    GL.glDisable(GL.GL_BLEND)
    GL.glDisable(GL.GL_TEXTURE_2D)
    GL.glEnable(GL.GL_DEPTH_TEST)

    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glPopMatrix()
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glPopMatrix()

    GL.glDeleteTextures(1, [texture])

def RenderText3D(text, font):

    GL.glEnable(GL.GL_TEXTURE_2D)
    GL.glEnable(GL.GL_BLEND)
    GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)

    texture, textureWidth, textureHeight = CreateTextTexture(text, font)
    GL.glBindTexture(GL.GL_TEXTURE_2D, texture)

    GL.glPushMatrix()
    sizeScale = 1/max(textureWidth, textureHeight)
    GL.glScale(sizeScale, sizeScale, sizeScale)

    GL.glBegin(GL.GL_QUADS)
    GL.glColor(1,1,1,1)
    GL.glTexCoord2f(0,1); GL.glVertex2f(0, 0)
    GL.glTexCoord2f(1,1); GL.glVertex2f(textureWidth, 0)
    GL.glTexCoord2f(1,0); GL.glVertex2f(textureWidth, textureHeight)
    GL.glTexCoord2f(0,0); GL.glVertex2f(0, textureHeight)
    GL.glEnd()
    
    GL.glPopMatrix()

    GL.glDisable(GL.GL_BLEND)
    GL.glDisable(GL.GL_TEXTURE_2D)

    GL.glDeleteTextures(1, [texture])


def run():
    camera = CameraController()

    frames = []

    frame0 = Frame()
    frame0.name = 'Frame0'
    frame0.localMatrix = Matrix.fromTranslation([-1,0,0])
    frames.append(frame0)

    frame1 = Frame()
    frame1.name = 'Frame1'
    frame1.parent = frame0
    frames.append(frame1)

    frame2 = Frame()
    frame2.name = 'Frame2'
    frame2.parent = frame1
    frame2.localMatrix = Matrix.fromTranslation([0,1,0])
    frames.append(frame2)

    sdl2.sdlttf.TTF_Init()
    font = "Arial"
    fontpath = os.path.join(os.environ["windir"], "Fonts", font + ".ttf")
    font = sdl2.sdlttf.TTF_OpenFont(str.encode(fontpath), 24)

    sdl2.ext.init()
    window = sdl2.SDL_CreateWindow(
        b"Linalg_test", 
        sdl2.SDL_WINDOWPOS_UNDEFINED, sdl2.SDL_WINDOWPOS_UNDEFINED, width, height,
        sdl2.SDL_WINDOW_OPENGL)

    context = sdl2.SDL_GL_CreateContext(window)
    sdl2.SDL_GL_SetSwapInterval(1)
    
    running = True
    while running:

        camera.update()

        # do the actual drawing
        GL.glClearColor(0.2, 0.2, 0.2, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
 
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluPerspective(70, width/height, 0.1, 1000)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()

        pos, look, up = camera.getLookAt()
        GLU.gluLookAt(
            pos.x, pos.y, pos.z,
            look.x, look.y, look.z,
            up.x, up.y, up.z)

        for f in frames:
            drawFrame(f, font)

        #RenderText2D('FOO', 0,0, font)

        # show the back buffer
        sdl2.SDL_GL_SwapWindow(window)

        # wait for somebody to close the window
        event = sdl2.SDL_Event()
        while sdl2.SDL_PollEvent(ctypes.byref(event)):
            if event.type == sdl2.SDL_QUIT:
                running = False
                break

            camera.event(event)

            if event.type == sdl2.SDL_KEYDOWN:
                shift = event.key.keysym.mod & sdl2.KMOD_LSHIFT
                ctrl = event.key.keysym.mod & sdl2.KMOD_LCTRL

                sign = -1.0 if shift else 1.0

                if event.key.keysym.scancode == sdl2.SDL_SCANCODE_X:
                    if ctrl:
                        frame1.localMatrix = Matrix.fromAxisAngle([1,0,0], math.radians(sign*5)) @ frame1.localMatrix
                    else:
                        frame1.localMatrix = Matrix.fromTranslation([sign*0.1,0,0]) @ frame1.localMatrix
                if event.key.keysym.scancode == sdl2.SDL_SCANCODE_Y:
                    if ctrl:
                        frame1.localMatrix = Matrix.fromAxisAngle([0,1,0], math.radians(sign*5)) @ frame1.localMatrix
                    else:
                        frame1.localMatrix = Matrix.fromTranslation([0,sign*0.1,0]) @ frame1.localMatrix
                if event.key.keysym.scancode == sdl2.SDL_SCANCODE_Z:
                    if ctrl:
                        frame1.localMatrix = Matrix.fromAxisAngle([0,0,1], math.radians(sign*5)) @ frame1.localMatrix
                    else:
                        frame1.localMatrix = Matrix.fromTranslation([0,0,sign*0.1]) @ frame1.localMatrix

    sdl2.SDL_GL_DeleteContext(context)
    sdl2.SDL_Quit()

    return 0

if __name__ == "__main__":
    sys.exit(run())