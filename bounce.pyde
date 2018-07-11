xCoordinate = random (50, 200)
yCoordinate = random (50, 200)
ySpeed = 2
xSpeed = 2

ellipseSize = 20


def setup():
    size (600,800)
    
    
def draw():
    r = random (50, 400)
    background(0)
    global xCoordinate, yCoordinate, xSpeed, ySpeed, ellipseSize
    topBoundary = ellipseSize / 2
    bottomBoundary =800 - ellipseSize /2
    
    leftBoundary = ellipseSize / 2
    rightBoundary =600 - ellipseSize /2
    
    if yCoordinate >= bottomBoundary or yCoordinate <= topBoundary:
      ySpeed = -ySpeed  #reverse ball
      yCoordinate += ySpeed
    
    if xCoordinate >= rightBoundary or xCoordinate <= leftBoundary:
       xSpeed =-xSpeed
    
    yCoordinate += ySpeed
    xCoordinate += xSpeed
    
    fill(0,255,0)
    ellipse (xCoordinate, yCoordinate, ellipseSize, ellipseSize)
    

    #ellipse (r, xCoordinate, ellipseSize, ellipseSize)
