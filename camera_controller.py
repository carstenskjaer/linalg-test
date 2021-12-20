import sdl2

from vector import Vector

class CameraController:
    lastUpdateTick = 0
    
    currentPos = Vector(1,1,1)
    currentLookDir = Vector(-1, -1, -1).normalize()
    upDir = Vector(0,1,0)

    forwardActive = False
    backwardActive = False
    leftActive = False
    rightActive = False
    upActive = False
    downActive = False
    lookActive = False

    horizontalSpeed = 0.2 # /s
    verticalSpeed = 0.2 # /s

    def update(self):
        now = sdl2.SDL_GetTicks()

        timeStep = (now - self.lastUpdateTick) / 1000.0

        if self.forwardActive:
            self.currentPos += self.currentLookDir * (self.horizontalSpeed * timeStep)
        if self.backwardActive:
            self.currentPos -= self.currentLookDir * (self.horizontalSpeed * timeStep)
        if self.leftActive:
            c = self.currentLookDir.cross(self.upDir)
            self.currentPos -= c * (self.horizontalSpeed * timeStep)
        if self.rightActive:
            c = self.currentLookDir.cross(self.upDir)
            self.currentPos += c * (self.horizontalSpeed * timeStep)
        if self.upActive:
            self.currentPos += self.upDir * (self.verticalSpeed * timeStep)
        if self.downActive:
            self.currentPos -= self.upDir * (self.verticalSpeed * timeStep)

        self.lastUpdateTick = now
        pass

    def getLookAt(self):
        return self.currentPos, self.currentPos + self.currentLookDir, self.upDir
        pass

    def event(self, event):
        if event.type == sdl2.SDL_WINDOWEVENT:
            if event.window.event == sdl2.SDL_WINDOWEVENT_FOCUS_LOST:
                self.forwardActive = False
                self.backwardActive = False
                self.leftActive = False
                self.rightActive = False
                self.upActive = False
                self.downActive = False
                self.lookActive = False
        if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
            x = event.button.x
            y = event.button.y
            if event.button.button == sdl2.SDL_BUTTON_LEFT:
                #print(f'Left mouse down at {x},{y}')
                lookActive = True
            if event.button.button == sdl2.SDL_BUTTON_RIGHT:
                #print(f'Right mouse down at {x},{y}')
                pass
        if event.type == sdl2.SDL_MOUSEBUTTONUP:
            x = event.button.x
            y = event.button.y
            if event.button.button == sdl2.SDL_BUTTON_LEFT:
                lookActive = False
                #print(f'Left mouse up at {x},{y}')
            if event.button.button == sdl2.SDL_BUTTON_RIGHT:
                #print(f'Right mouse up at {x},{y}')
                pass
        if event.type == sdl2.SDL_MOUSEMOTION:
            x = event.button.x
            y = event.button.y
            #print(f'Mouse motion at {x},{y}')
            if self.lookActive:
                # TODO
                pass
        if event.type == sdl2.SDL_KEYDOWN:
            if event.key.keysym.scancode == sdl2.SDL_SCANCODE_A:
                self.leftActive = True
            if event.key.keysym.scancode == sdl2.SDL_SCANCODE_W:
                self.forwardActive = True
            if event.key.keysym.scancode == sdl2.SDL_SCANCODE_S:
                self.backwardActive = True
            if event.key.keysym.scancode == sdl2.SDL_SCANCODE_D:
                self.rightActive = True
            if event.key.keysym.scancode == sdl2.SDL_SCANCODE_E:
                self.downActive = True
            if event.key.keysym.scancode == sdl2.SDL_SCANCODE_Q:
                self.upActive = True
        if event.type == sdl2.SDL_KEYUP:
            if event.key.keysym.scancode == sdl2.SDL_SCANCODE_A:
                self.leftActive = False
            if event.key.keysym.scancode == sdl2.SDL_SCANCODE_W:
                self.forwardActive = False
            if event.key.keysym.scancode == sdl2.SDL_SCANCODE_S:
                self.backwardActive = False
            if event.key.keysym.scancode == sdl2.SDL_SCANCODE_D:
                self.rightActive = False
            if event.key.keysym.scancode == sdl2.SDL_SCANCODE_E:
                self.downActive = False
            if event.key.keysym.scancode == sdl2.SDL_SCANCODE_Q:
                self.upActive = False

