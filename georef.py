# GEOREF - utilities for encoding GEOREF with degree precision

quadletters = "ABCDEFGHJKLMNPQRSTUVWXYZ"

def encode(latitude,longitude):

    # Borrow the Maidenhead 'square' designation for the 1 degree quad.
    # Not tested in southern or eastern hemispheres.

    easting = int((180+longitude)/15)
    eastingSquare = ((180+int(longitude))-(easting*15))-1
    northing = int((90+latitude)/15)
    northingSquare = int(latitude+90)-(northing*15)
    georef = quadletters[easting]
    georef += quadletters[northing]
    georef += quadletters[eastingSquare]
    georef += quadletters[northingSquare]
    
    return georef
    

def adjacent(latitude,longitude):
    # this creates adjacent georefs by adding and subtracting 1 degree
    # from latitude and longitude then encoding the result. 

    n = latitude +1
    s = latitude -1
    e = longitude+1
    w = longitude-1

    # care is required crossing dateline, greenwich meridian, and poles.
    if n > 90:
        n = 180-n
    if s < -90:
        s = -180+(abs(s))
    
    if e > 180:
        e = -360+e
    if w < -180:
        w = 180+(180+w)

    nw = encode(n,w)
    nx = encode(n,longitude)
    ne = encode(n,e)
    xe = encode(latitude,e)
    se = encode(s,e)
    sx = encode(s,longitude)
    sw = encode(s,w)
    xw = encode(latitude,w)

    return [nw,nx,ne,xe,se,sx,sw,xw]

