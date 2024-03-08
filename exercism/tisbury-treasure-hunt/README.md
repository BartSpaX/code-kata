# Tisbury Treasure Hunt
[![Static Badge](https://img.shields.io/badge/Link-To%20Exercise-blue)](https://exercism.org/tracks/python/exercises/tisbury-treasure-hunt)

## Instructions

Azara and Rui are teammates competing in a pirate-themed treasure hunt. One has 
a list of treasures with map coordinates, the other a list of location names 
with map coordinates. They've also been given blank maps with a starting place 
marked YOU ARE HERE.

<table>
    <tbody>
        <tr>
            <th>Azara's List</th>
            <th></th>
            <th>Rui's List</th>
        </tr>
        <tr>
            <td>
                <table>
                    <thead>
                        <tr>
                            <th>Treasure</th>
                            <th>Coordinates</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Amethyst Octopus</td>
                            <td>1F</td>
                        </tr>
                        <tr>
                            <td>Angry Monkey Figurine</td>
                            <td>5B</td>
                        </tr>
                        <tr>
                            <td>Antique Glass Fishnet Float</td>
                            <td>3D</td>
                        </tr>
                        <tr>
                            <td>Brass Spyglass</td>
                            <td>4B</td>
                        </tr>
                        <tr>
                            <td>Carved Wooden Elephant</td>
                            <td>8C</td>
                        </tr>
                        <tr>
                            <td>Crystal Crab</td>
                            <td>6A</td>
                        </tr>
                        <tr>
                            <td>Glass Starfish</td>
                            <td>6D</td>
                        </tr>
                        <tr>
                            <td>Model Ship in Large Bottle</td>
                            <td>8A</td>
                        </tr>
                        <tr>
                            <td>Pirate Flag</td>
                            <td>7F</td>
                        </tr>
                        <tr>
                            <td>Robot Parrot</td>
                            <td>1C</td>
                        </tr>
                        <tr>
                            <td>Scrimshawed Whale Tooth</td>
                            <td>2A</td>
                        </tr>
                        <tr>
                            <td>Silver Seahorse</td>
                            <td>4E</td>
                        </tr>
                        <tr>
                            <td>Vintage Pirate Hat</td>
                            <td>7E</td>
                        </tr>
                    </tbody>
                </table>
            </td>
            <td></td>
            <td>
                <table>
                    <thead>
                        <tr>
                            <th>Location Name</th>
                            <th>Coordinates</th>
                            <th>Quadrant</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Seaside Cottages</td>
                            <td>("1", "C")</td>
                            <td>Blue</td>
                        </tr>
                        <tr>
                            <td>Aqua Lagoon (Island of Mystery)</td>
                            <td>("1", "F")</td>
                            <td>Yellow</td>
                        </tr>
                        <tr>
                            <td>Deserted Docks</td>
                            <td>("2", "A")</td>
                            <td>Blue</td>
                        </tr>
                        <tr>
                            <td>Spiky Rocks</td>
                            <td>("3", "D")</td>
                            <td>Yellow</td>
                        </tr>
                        <tr>
                            <td>Abandoned Lighthouse</td>
                            <td>("4", "B")</td>
                            <td>Blue</td>
                        </tr>
                        <tr>
                            <td>Hidden Spring (Island of Mystery)</td>
                            <td>("4", "E")</td>
                            <td>Yellow</td>
                        </tr>
                        <tr>
                            <td>Stormy Breakwater</td>
                            <td>("5", "B")</td>
                            <td>Purple</td>
                        </tr>
                        <tr>
                            <td>Old Schooner</td>
                            <td>("6", "A")</td>
                            <td>Purple</td>
                        </tr>
                        <tr>
                            <td>Tangled Seaweed Patch</td>
                            <td>("6", "D")</td>
                            <td>Orange</td>
                        </tr>
                        <tr>
                            <td>Quiet Inlet (Island of Mystery)</td>
                            <td>("7", "E")</td>
                            <td>Orange</td>
                        </tr>
                        <tr>
                            <td>Windswept Hilltop (Island of Mystery)</td>
                            <td>("7", "F")</td>
                            <td>Orange</td>
                        </tr>
                        <tr>
                            <td>Harbor Managers Office</td>
                            <td>("8", "A")</td>
                            <td>Purple</td>
                        </tr>
                        <tr>
                            <td>Foggy Seacave</td>
                            <td>("8", "C")</td>
                            <td>Purple</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>

But things are a bit disorganized: Azara's coordinates appear to be formatted 
and sorted differently from Rui's, and they have to keep looking from one list 
to the other to figure out which treasures go with which locations. Being 
budding pythonistas, they have come to you for help in writing a small program 
(a set of functions, really) to better organize their hunt information.

### 1. Extract coordinates

Implement the `get_coordinate()` function that takes a `(treasure, coordinate)`
pair from Azara's list and returns only the extracted map coordinate.

```python
>>> get_coordinate(('Scrimshawed Whale Tooth', '2A'))
2A
```

### 2. Format coordinates

Implement the `convert_coordinate()` function that takes a coordinate in the format "2A" and returns a tuple in the format `("2", "A")`.

```python
>>> convert_coordinate("2A")
("2", "A")
```

### 3. Match coordinates

Implement the `compare_records()` function that takes a `(treasure, coordinate)` pair and a `(location, coordinate, quadrant)` record and compares coordinates 
from each. Return `True` if the coordinates "match", and return `False` if they 
do not. Re-format coordinates as needed for accurate comparison.

```python
>>> compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue'))
False

>>> compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple'))
True
```

### 4. Combine matched records

Implement the `create_record()` function that takes a `(treasure, coordinate)` 
pair from Azara's list and a `(location, coordinate, quadrant)` record from 
Rui's list and returns `(treasure, coordinate, location, coordinate, quadrant)` 
**if the coordinates match**. If the coordinates do not match, return the 
string **"not a match"**. Re-format the coordinate as needed for accurate 
comparison.

```python
>>> create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))
('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')

>>> create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue'))
"not a match"
```

### 5. "Clean up" & make a report of all records

Clean up the combined records from Azara and Rui so that there's only one set 
of coordinates per record. Make a report so they can see one list of everything 
they need to put on their maps. Implement the `clean_up()` function that takes 
a tuple of tuples (everything from both lists), looping through the outer 
tuple, dropping the unwanted coordinates from each inner tuple and adding each 
to a 'report'. Format and return the 'report' so that there is one cleaned 
record on each line.

```python
>>> clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')))

"""
('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')\n
('Vintage Pirate Hat', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')\n
('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')\n
"""
```