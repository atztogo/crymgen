# crymgen

Crystal structures of binary compounds for 230 space group types are generated
by using random numbers and space group operations.

The random numbers were used to generate crystal structures covering all 230
space group types. They were determined empirically through trial and error.

To regenerate the crystal structures, run:

```bash
pytest --gendata tests/test_generate.py::test_generate_data_for_expand_binary
```

The generated crystal structures are saved in YAML format. For example:

```yaml
space_group:
  number: 153

unitcell:
  lattice:
  - [   10.00000000000000,     0.00000000000000,     0.00000000000000]
  - [   -5.00000000000000,     8.66025403784439,     0.00000000000000]
  - [    0.00000000000000,     0.00000000000000,    11.00000000000000]
  points:
  - number: 1
    coordinates: [    0.37199720000000,     0.40875639000000,     0.06329474000000]
  - number: 2
    coordinates: [    0.51557400000000,     0.16376790000000,     0.56800529000000]
  - number: 1
    coordinates: [   -0.40875639000000,    -0.03675919000000,     0.72996140666667]
  - number: 2
    coordinates: [   -0.16376790000000,     0.35180610000000,     1.23467195666667]
  - number: 1
    coordinates: [    0.03675919000000,    -0.37199720000000,     0.39662807333333]
  - number: 2
    coordinates: [   -0.35180610000000,    -0.51557400000000,     0.90133862333333]
  - number: 1
    coordinates: [   -0.40875639000000,    -0.37199720000000,     0.27003859333333]
  - number: 2
    coordinates: [   -0.16376790000000,    -0.51557400000000,    -0.23467195666667]
  - number: 1
    coordinates: [    0.03675919000000,     0.40875639000000,     0.60337192666667]
  - number: 2
    coordinates: [   -0.35180610000000,     0.16376790000000,     0.09866137666667]
  - number: 1
    coordinates: [    0.37199720000000,    -0.03675919000000,    -0.06329474000000]
  - number: 2
    coordinates: [    0.51557400000000,     0.35180610000000,    -0.56800529000000]
```

In the YAML file:
- The unit cell basis vectors are provided as rows under the `lattice` key.
- Atomic positions are specified as fractional `coordinates` relative to these
  basis vectors.
- Atoms labeled with the same `number` are of the same type.