import math

def solve(input_data: str):
    boxes = [[int(x) for x in line.split(",")] for line in input_data.split('\n')]
    parts = [0,0]

    # create all possible edges with distances
    edges = []
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            d = math.sqrt(sum((boxes[i][k] - boxes[j][k])**2 for k in range(3)))
            edges.append((d, i, j))

    # sort on these, smallest first
    edges.sort()

    # every box is its own circuit at start
    circuits = [{i} for i in range(len(boxes))]

    # small method to find circuit for index
    def find_circuit(idx):
        for c in circuits:
            if idx in c:
                return c
        return None

    # do the first 1000 edges to find the largest 3 circuits for part 1
    for _, i, j in edges[:1000]:
        ci = find_circuit(i)
        cj = find_circuit(j)
        # if they are already connected, skip, otherwise merge the circuits
        # (we are not tracking edges, just connected components)
        if ci is not cj:
            ci.update(cj)
            circuits.remove(cj)

    # sort on sizes and get the largest 3 for part 1
    sizes = sorted([len(c) for c in circuits], reverse=True)
    parts[0] = sizes[0] * sizes[1] * sizes[2]

    # Then do the remaining until one circuit remains for part 2
    for _, i, j in edges[1000:]:
        ci = find_circuit(i)
        cj = find_circuit(j)
        if ci is not cj:
            ci.update(cj)
            circuits.remove(cj)
        # Then we have one circuit and part 2 is product of their x-coordinates
        if len(circuits) == 1:
            parts[1] = boxes[i][0]*boxes[j][0]
            break

    return parts
