def script(check, x, y):
    if check("gold", x, y):
        return "take"
    if check("level") == 1:
        if check("gold", x, y):
            return "take"
        if not check("wall", x + 1, y):
            if check("wall", x+2, y):
                return "down"
            return "right"
    if check("level") == 2:
        if check("gold", x + 1, y) or check("gold", x + 2, y):
            return "right"
        elif check("gold", x, y + 1):
            return "down"
        else:
            return "up"
    if check("level") == 3:

        '''
        if not check("wall", x, y - 1):
            if not check("wall", x + 1, y):
                return "right"
            else:
                return "up"
        
        
        if not check("wall", x + 1, y):
            return "right"
        elif not check("wall", x, y - 1) and check("wall", x + 1, y):
            return "up"
        elif not check("wall", x - 1, y + 1) and not check("wall", x + 1, y):
            return "down"
            '''
    return "pass"
