BLACK =(0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
RED = (255, 0, 0)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0) 
WHITE = (255, 255, 255)

def wrap_coordinates(position, size):
    width, height = size
    if position.x < 0.0: position.x += width
    if position.x >= width: position.x -= width
    if position.y < 0.0: position.y += height
    if position.y >= height: position.y -= height