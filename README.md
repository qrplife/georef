# georef
Utility functions for encoding latitude and longitude into GEOREF with one-degree quad precision.
https://en.wikipedia.org/wiki/World_Geographic_Reference_System

## encode(latitude, longitude)

Encodes the position given by latitude and longitude in decimal degrees into a string with 15-degree and 1-degree quad designations. Western hemisphere longitudes are negative.

```
>>> encode(38.286108, -76.4291704)
'GJPJ'
```

## adjacent(latitude, longitude)

Returns a list of 1-degree precision quads that are adjacent to the quad encoded by latitude and longitude.

```
>>> adjacent(38.286108, -76.4291704)
['GJNK', 'GJPK', 'GJQK', 'GJQJ', 'GJQH', 'GJPH', 'GJNH', 'GJNJ']
```
