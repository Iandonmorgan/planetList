planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")

rocky_planets = slice(0,4)

del planet_list[8]

print("ROCKY PLANETS", planet_list[rocky_planets])
print("PLANETS", planet_list)

# Example spacecraft list
spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
   ("Viking2", "Mars"),
]

# Iterate over your list of planets, and inside that loop,
# iterate over the list of tuples. Print, for each planet,
# which satellites have visited it.

for planet in planet_list:
    sentence = f'{planet}'
    visited = []
    for craft in spacecraft:
        if craft[1] == planet:
            visited.append(craft[0])
    if len(visited) == 0:
        sentence += f' has not been visited by a spacecraft.'
        print(sentence)
    elif len(visited) == 1:
        sentence += f' was visited by {visited[0]}.'
        print(sentence)
    else:
        sentence += f' was visited by '
        last_visited = []
        last_visited.append(visited[-1])
        del visited[-1]
        for planet in visited:
            sentence += f'{planet}, '
        for planet in last_visited:
            sentence += f'and {planet}.'
        print(sentence)
            
        