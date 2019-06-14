import georef as g

# Test the example location from:
#    https://en.wikipedia.org/wiki/World_Geographic_Reference_System
#    aka Northern Hemisphere - West
def test_encode_n_w():
    lat, lon = 38.286108, -76.4291704
    expectedGrid = "GJPJ"
    actualGrid = g.encode(lat,lon)
    assert actualGrid == expectedGrid

def test_adjacent_n_w():
    lat, lon = 38.286108, -76.4291704
    expectedAdjacents = ["GJNK","GJPK","GJQK","GJQJ","GJQH","GJPH","GJNH","GJNJ"]
    actualAdjacents = g.adjacent(lat,lon)
    assert len(actualAdjacents) == len(expectedAdjacents)
    for adjacent in expectedAdjacents:
        assert adjacent in actualAdjacents

def test_adjacent_corners_n_w():
    corners = [
        (44.286108, -89.4291704, ["FKQA","GKAA","GKBA","GJBQ","GJBP","GJAP","FJQP","FJQQ"]),
        (44.286108, -75.4291704, ["GKPA","GKQA","HKAA","HJAQ","HJAP","GJQP","GJPP","GJPQ"]),
        (30.286108, -75.4291704, ["GJPB","GJQB","HJAB","HJAA","HHAQ","GHQQ","GHPQ","GJPA"]),
        (30.286108, -89.4291704, ["FJQB","GJAB","GJBB","GJBA","GHBQ","GHAQ","FHQQ","FJQA"])
    ]

    for corner in corners:
        lat, lon = corner[0], corner[1]
        expectedAdjacents = corner[2]
        actualAdjacents = g.adjacent(lat,lon)
        assert len(actualAdjacents) == len(expectedAdjacents)
        for adjacent in expectedAdjacents:
            assert adjacent in actualAdjacents

# Test Southern Hemisphere - West
def test_encode_s_w():
    lat, lon = -38.286108, -76.4291704
    expectedGrid = "GDPG"
    actualGrid = g.encode(lat,lon)
    assert actualGrid == expectedGrid

def test_adjacent_s_w():
    lat, lon = -38.286108, -76.4291704
    expectedAdjacents = ["GDNH","GDPH","GDQH","GDQG","GDQF","GDPF","GDNF","GDNG"]
    actualAdjacents = g.adjacent(lat,lon)
    assert actualAdjacents == expectedAdjacents




     
    
