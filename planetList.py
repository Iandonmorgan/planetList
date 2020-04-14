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