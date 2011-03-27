#!/usr/bin/env python

import sys

particles = {}

for line in sys.stdin:
    vel = [0, 0, 0]
    id, vel[0], vel[1], vel[2] = [float(a) for a in line.strip().split()]
    id = int(id)

    p = particles.get(id, list((0, 0, 0)))
    p = [sum(a) for a in zip(p, vel)]
    particles[id] = p

for id, v in particles.items():
    print id, v[0], v[1], v[2]

