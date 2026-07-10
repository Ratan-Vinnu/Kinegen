# Kinegen

> An open-source Python robotics kinematics library built for education, research, and rapid prototyping.

> **Status:** Experimental | Under Active Development

Kinegen is a robotics kinematics library written from scratch in Python and NumPy. Its goal is to provide a clean, modular, and mathematically rigorous implementation of modern robot kinematics while remaining approachable for students and robotics enthusiasts.

The project is currently focused on building a strong kinematics foundation before expanding into Jacobians, inverse kinematics, visualization, dynamics, and ROS interoperability.

---

## Why Kinegen?

Many robotics frameworks are extremely powerful but can be difficult to understand internally.

Kinegen aims to bridge that gap by being:

- Educational without sacrificing mathematical correctness
- Lightweight and easy to read
- Modular and extensible
- Suitable for rapid experimentation
- Based on modern robotics formulations rather than legacy conventions

The long-term vision is to create a complete robotics library that is both useful for learning and practical for real projects.

---

# Current Status

Current release:

**v0.1.0**

Implemented:

- Robot description using JSON
- Product of Exponentials (PoE) Forward Kinematics
- Space-frame screw axis representation
- Twist exponential implementation
- Rodrigues' Rotation Formula
- Homogeneous transformation generation
- Modular project architecture
- Validation against textbook examples

Currently in progress:

- Geometry/CAD layer
- Intermediate frame computation
- Visualization utilities
- Space Jacobian/Body Jacobian computations

---

# Mathematical Foundation

Kinegen currently uses the **Product of Exponentials (PoE)** formulation described in *Modern Robotics* by Kevin Lynch and Frank Park.

Instead of relying on Denavit–Hartenberg parameters, robots are represented using:

- Joint positions
- Joint axes
- Home configuration
- Screw theory

This provides a cleaner and more general representation of robotic manipulators.

---

# Validation

The current forward kinematics implementation has been validated against textbook examples(Universal Robots’ UR5 6R robot arm) from **Modern Robotics**.

The numerical results match the reference solutions to floating-point precision (approximately 1e−16), giving confidence that the mathematical implementation is correct.

Future releases will include additional validation against:

- Industrial robot models
- Analytical examples
- Numerical regression tests

---

# Project Structure

```
kinegen/
│
├── src/
│   ├── parser.py
│   ├── model.py
│   ├── fk.py
│   ├── poe.py
│   ├── math_utils.py
│   └── valid.py
│
├── examples/
│
├── tests/
│
└── docs/
```

This structure will continue evolving as new functionality is added.

---

# Design Philosophy

Some core principles guiding the project:

- Modular architecture
- Readable mathematical implementation
- Minimal dependencies
- Separation between geometry and kinematics
- Extensible robot description
- Educational code over clever code

---

# Planned Roadmap

## v0.2

- Geometry layer
- Intermediate transformations
- Improved API
- Forward Kinematics Visualisation via Interactive Plotting

## v0.3

- Space Jacobian Computation
- Body Jacobian Computation

## v0.4

- Numerical Inverse Kinematics Implementation
- Inverse Kinematics Interactive Visualisation

## Future

- Dynamics
- Trajectory generation
- URDF import
- ROS integration
- Collision geometry
- Documentation website

---

# Installation

At the moment, Kinegen is in early development.

Clone the repository:

```bash
git clone https://github.com/<your-username>/kinegen.git
```

Install dependencies:

```bash
pip install numpy
```

Packaging and PyPI distribution will be added in a future release.

---

# Contributing

Contributions, suggestions, bug reports, and discussions are welcome.

As the project is still experimental, APIs and file structure may change between releases.

---

# License

This project is licensed under the MIT License.

---

# Acknowledgements

This project draws significant inspiration from:

- *Modern Robotics: Mechanics, Planning, and Control* by Kevin M. Lynch and Frank C. Park
- The Robotics and Control community
- Open-source scientific Python ecosystem

---

# Disclaimer

Kinegen is currently an **experimental project**.

Interfaces, APIs, internal architecture, and file organization may change significantly before reaching a stable `v1.0.0` release.

Until then, breaking changes should be expected.
