#785A - Anton and Polyhedrons
print(sum([c for n in range(int(input())) for t in [input()] for d in [{'Tetrahedron':4,'Cube':6,'Octahedron':8,'Dodecahedron':12,'Icosahedron':20}] for c in [d[t]]]))