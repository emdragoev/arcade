def get_angle(y: int, max_speed: int, obj_height: int) -> int:
    """Gets angle that object will bounce off at
    
    Args:
        y: current y coordinate
        max_speed: maximum speed which the object can move at
        obj_height: the height of the object of collision
    
    Returns:
        New y direction of ball
    """
    middle_y = y + obj_height /2
    y_diff = middle_y - y
    speed_change = (obj_height / 2) / max_speed
    return y_diff / speed_change