def wrap_coordinates(position, size):
    width, height = size
    if position.x < 0.0: position.x += width
    if position.x >= width: position.x -= width
    if position.y < 0.0: position.y += height
    if position.y >= height: position.y -= height