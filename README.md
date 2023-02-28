# pybendt
Brownian Elastic Networks with Dynamic Topology.
Copyright &copy;2023- Tomasz Skóra [tskora@sci.utah.edu](mailto:tskora@sci.utah.edu)

> **Warning**
> The software is not extensively tested yet! It's just a prototype!

## Features

- [x] Brownian dynamics w/o hydrodynamic interactions
- [x] customizable atom-atom (2-body) interactions
- [ ] customizable many-body interactions
- [x] customizable event-driven bond topology changes

## Quick start

To install, type following commands in a terminal:
```shell
$ pip3 install pybendt
```

## Units

| Physical property | Units |
|---|---|
| Temperature | kelvin (*K*) |
| Friction | kilocalorie per mole per angstrom squared (*kcal/mol/Å^2*) |
| Time | picosecond (*ps*) |
| Distance | angstrom (*Å*) |
| Energy | kilocalorie per mol per angstrom (*kcal/mol/Å*) |

> **Note**
> There is a separate function ``friction_from_temparature_hydrodynamic_radius_and_viscosity`` which takes temperature in kelvin (*K*), hydrodynamic radius in angstrom (*Å*) and viscosity in centipoise (*cP*).

## Authors

The following people contributed to the development of pybendt.

- Tomasz Skóra -- **creator, lead developer** (contact: tskora@ichf.edu.pl)
