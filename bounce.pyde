xCoordinate = 50
yCoordinate = 50
speed = 1

ellipseSize = 50


def setup():
    size (400,400)
    
    
def draw():
    r = random (50, 400)
    background(0)
    global xCoordinate, yCoordinate, ySpeed, speed, ellipseSize
    leftTopBoundary = ellipseSize / 2
    rightBottomBoundary =400 - ellipseSize /2
    if xCoordinate >= rightBottomBoundary or xCoordinate <= leftTopBoundary:
      speed = -speed  
    if yCoordinate >= rightBottomBoundary or yCoordinate <= leftTopBoundary:  
    xCoordinate += speed
    yCoordinate += ySpeed
    
    fill(0,255,0)
    ellipse (xCoordinate, r, ellipseSize, ellipseSize)
    

    #ellipse (r, xCoordinate, ellipseSize, ellipseSize)
