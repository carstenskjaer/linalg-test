import sys
import sdl2
import sdl2.ext
from OpenGL import GL, GLU
import ctypes

from camera_controller import CameraController


def run():
    camera = CameraController()

    sdl2.ext.init()
    window = sdl2.SDL_CreateWindow(
        b"Linalg_test", 
        sdl2.SDL_WINDOWPOS_UNDEFINED, sdl2.SDL_WINDOWPOS_UNDEFINED, 800, 600,
        sdl2.SDL_WINDOW_OPENGL)

    context = sdl2.SDL_GL_CreateContext(window)
    sdl2.SDL_GL_SetSwapInterval(1)
    
    running = True
    while running:

        camera.update()

        # do the actual drawing
        GL.glClearColor(0.1, 0.1, 0.1, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
 
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluPerspective(70, 800/600, 0.1, 1000)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()

        pos, look, up = camera.getLookAt()
        GLU.gluLookAt(
            pos.x, pos.y, pos.z,
            look.x, look.y, look.z,
            up.x, up.y, up.z)

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

        # show the back buffer
        sdl2.SDL_GL_SwapWindow(window)

        # wait for somebody to close the window
        event = sdl2.SDL_Event()
        while sdl2.SDL_PollEvent(ctypes.byref(event)):
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            camera.event(event)

    sdl2.SDL_GL_DeleteContext(context)
    sdl2.SDL_Quit()

    return 0

if __name__ == "__main__":
    sys.exit(run())