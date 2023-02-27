import numpy as np
import os
import sys

sys.path.append(os.path.abspath("./pybendt"))
print(sys.path)

from pseudorandom import Pseudorandom
from atom import Atom
from interaction import *
from reaction import *

friction = 1.0

pseudorandom = Pseudorandom()

a1 = Atom([0.0, 0.0, 0.0], friction)
a2 = Atom([1.0, 1.0, 1.0], friction)
a3 = Atom([2.0, 2.0, 2.0], friction)

atoms = [a1, a2, a3]
timestep = 0.01
temperature = 298.0

print(atoms)
print()

a1.add_interaction(a2, null_force, null_energy, {})
a1.add_interaction(a3, null_force, null_energy, {})

a2.add_reaction([a3], null_condition, null_effect)
a3.add_reaction([a1, a2], null_condition, null_effect)

print(a1.interactions)
print(a2.interactions)
print(a3.interactions)
print()

print(a1.reactions)
print(a2.reactions)
print(a3.reactions)
print()

a2.remove_reactions_by_id([2])

print(a1.reactions)
print(a2.reactions)
print(a3.reactions)
print()

1/0


interactions = []
for a in atoms:
	[ interactions.append(i) for i in a.interactions if i not in interactions ]

reactions = []
for a in atoms:
	[ reactions.append(r) for r in a.reactions if r not in reactions ]

pointers = np.zeros((len(atoms), len(atoms), 3))
distances = np.zeros((len(atoms), len(atoms)))
id_to_index = {}
for i in range(len(atoms)):
	id_to_index[atoms[i].id]=i
	for j in range(i):
		pointers[i][j] = atoms[j].position - atoms[i].position
		pointers[j][i] = -pointers[i][j]
		distances[i][j] = distances[j][i] = np.sqrt(np.sum(pointers[i][j]**2))

E = 0
for interaction in interactions:
	interaction.compute_force(distances[id_to_index[interaction.atom1.id]][id_to_index[interaction.atom2.id]],\
							   pointers[id_to_index[interaction.atom1.id]][id_to_index[interaction.atom2.id]])
	interaction.compute_energy(distances[id_to_index[interaction.atom1.id]][id_to_index[interaction.atom2.id]])
	E += interaction.energy

# print(E)
# print()
# for interaction in interactions: print(interaction.energy)
# print()
# for atom in atoms: print(atom.force)
# 1/0

print(pointers)
print(distances)

for atom in atoms:
	atom.deterministic_move(timestep)
	atom.brownian_move(timestep, temperature, pseudorandom.draw())

for reaction in reactions:
	if reaction.condition_fulfilled(): reaction.effect()

print(atoms)
1/0

# a1.remove_interactions_by_id([1])

# print(a1.interactions)
# print(a2.interactions)
# print(a3.interactions)

# F = np.zeros(3*len(atoms))

# def compute_force(atoms):
# 	for atom in atoms:
# 		a.compute_force(F)

1/0

for i in range(1000):
	compute_force(atoms)
	compute_energy(atoms)
	compute_random_force(atoms)
	move(atoms)
	if topology_change_condition_fulfilled(atoms):
		topology_change(atoms)