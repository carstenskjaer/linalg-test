import sdl2
import math
from vector import Vector

class CameraController:
    lastUpdateTick = 0
    
    currentPos = Vector(1,1,1)
    currentLookDir = Vector()
    upDir = Vector(0,0,1)

    lookAngleHorizontal = 180
    lookAngleVertical = 120

    forwardActive = False
    backwardActive = False
    leftActive = False
    rightActive = False
    upActive = False
    downActive = False
    lookActive = False

    lastMouseLookX = 0
    lastMouseLookY = 0

    horizontalSpeed = 0.7 # unit/s
    verticalSpeed = 0.7 # unit/s
    lookSpeed = 0.1 # degrees per mouse movement (pixels)

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
        self.currentLookDir = Vector(
            math.sin(math.radians(self.lookAngleVertical))*math.cos(math.radians(self.lookAngleHorizontal)),
            math.sin(math.radians(self.lookAngleVertical))*math.sin(math.radians(self.lookAngleHorizontal)),
            math.cos(math.radians(self.lookAngleVertical))
        )
        return self.currentPos, self.currentPos + self.currentLookDir, self.upDir


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
            if event.button.button == sdl2.SDL_BUTTON_LEFT:
                self.lastMouseLookX = event.button.x
                self.lastMouseLookY = event.button.y
                self.lookActive = True
            if event.button.button == sdl2.SDL_BUTTON_RIGHT:
                pass
        if event.type == sdl2.SDL_MOUSEBUTTONUP:
            if event.button.button == sdl2.SDL_BUTTON_LEFT:
                self.lookActive = False
            if event.button.button == sdl2.SDL_BUTTON_RIGHT:
                pass
        if event.type == sdl2.SDL_MOUSEMOTION:
            if self.lookActive:
                offsetX = event.button.x - self.lastMouseLookX
                offsetY = event.button.y - self.lastMouseLookY

                self.lookAngleHorizontal += offsetX * self.lookSpeed
                self.lookAngleVertical += offsetY * self.lookSpeed
                self.lookAngleVertical = max(1, min(self.lookAngleVertical, 179))

                self.lastMouseLookX = event.button.x
                self.lastMouseLookY = event.button.y
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
