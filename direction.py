def direction(facing: str, turn: int) -> str:
    '''The function rotates the compass needle by the specified number of degrees'''
    compass = {
        'N': 0,
        'NE': 45,
        'E': 90,
        'SE': 135,
        'S': 180,
        'SW': 225,
        'W': 270,
        'NW': 315,
    }
    compass_invert = {degree: wind for wind,degree in compass.items()}

    try:
        current_degree = compass[facing]
    except KeyError:
        raise ValueError('Wrong direction. Options: N, NE, E, SE, S, SW, W, NW')
    try:
        turn %= 360
        compass_invert[turn]
    except (TypeError, KeyError):
        raise ValueError('Turn must be an integer multiple of 45')
    
    result = (current_degree + turn) % 360
    return compass_invert[result]
    

# Examples
# "S",  180  -->  "N"
# "SE", -45  -->  "E"
# "W",  495  -->  "NE"
# "EN", 45  --> ValueError: "Wrong direction..."
# "W", 375  --> ValueError: "Turn must be a multiple of 45"