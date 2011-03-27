#!/usr/bin/env python

import os
import sys
import math
from operator import add


class Particle(object):

    def __init__(self, floatline):
        self.pos = [0, 0, 0]
        self.vel = [0, 0, 0]
        self.id, \
            self.pos[0], self.pos[1], self.pos[2], \
            self.vel[0], self.vel[1], self.vel[2], \
            self.mass = \
                [float(a) for a in floatline.strip().split()]

    def add_vel(self, o):
        if o.id == self.id:
            return (0, 0, 0)
        dv = [self.pos[idx] - o.pos[idx] for idx, pos in enumerate(self.pos)]
        d = sum([math.pow(a, 2) for a in dv])
        f = 0.0001 * o.mass * self.mass / d
        return [a * f for a in dv]


for line in sys.stdin:
    p = Particle(line)
    print >> sys.stderr, p.id
    for oline in open('nbody/sim.txt'):
        o = Particle(oline)
        vel = p.add_vel(o)
        print p.id, vel[0], vel[1], vel[2]

