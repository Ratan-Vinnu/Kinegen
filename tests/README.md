# Tests

This directory contains scripts used to verify the correctness of Kinegen.

At the current stage of development, these tests primarily consist of validation scripts created during implementation. They were used to verify individual mathematical components such as:

- Rodrigues' Rotation Formula
- Twist exponentials
- Product of Exponentials forward kinematics
- Homogeneous transformations
- Textbook validation examples

As the project matures, these scripts will be replaced by a structured automated test suite using standard Python testing tools.

Future releases will include:

- Unit tests
- Regression tests
- Numerical accuracy tests
- Continuous integration