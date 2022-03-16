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
    elif check("level") == 3:
        for i in range(1, 20): # Left
            if check("gold", x - i, y):
                return "left"
        for i in range(1, 28): # Right (and Up for middle)
            if check("wall", x + i, y):
                break
            elif check("gold", x + i, y):
                return "right"
            if i > 10:
                for j in range(1, 8):
                    if check("wall", x, y - j):
                        break
                    elif check("gold", x, y - j):
                        return "up"
        for i in range(1, 25): # Up
            if check("wall", x, y - i):
                break
            elif check("gold", x, y - i):
                return "up"
        for i in range(1, 8): # Down
            if check("wall", x, y + i):
                break
            elif check("gold", x, y + i):
                return "down"
        for i in range(1, 6): # Down for middle
            if check("wall", x, y - i):
                return "down"
        if check("wall", x, y + 1): # For else Left
            return "left"
        return "down"

    elif check("level") == 4:
        for i in range(1, 11): # Up
            if check("wall", x, y - i):
                break
            if check("gold", x, y - i):
                return "up"
        for i in range(1, 101): # Right
            if check("wall", x + i, y):
                break
            if check("gold", x + i, y):
                return "right"
        for i in range(1, 11): # Down
            if check("wall", x, y + i):
                break
            if check("gold", x, y + i):
                return "down"
        for i in range(1, 11): # Left
            if check("wall", x - i, y):
                break
            if check("gold", x - i, y):
                return "left"
        d, l = 1, 1
        for i in range(1, 13):
            if check("wall", x, y + i):
                d = 0
            if check("wall", x - i, y):
                l = 0
        if d: return "down"
        if l: return "left"
        #if check("wall", x - 1, y) and check("wall", x - 1, y): return "up"
        return "right"
    return "pass"
