# Tuples are like lists but with immutable data. Tuples are defined using () rather than [].

dimensions = (200, 2)
print(dimensions[0])
print(dimensions[1])

# Below code will generate error because tuples cannot be reassigned
dimensions[0] = 250
print(dimensions[0])
