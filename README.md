# ECCLib
Simple elliptic curve library for python. Work in progress!!

Read this king: https://www.math-stockholm.se/polopoly_fs/1.1276768.1694085500!/Kompendium_Cirkel_2023_2024_Elliptiska_kurvor.pdf

## Documentation
Current avalible functions:
- duplicatePoint
- addPoints
- scalePoint

Where the last three arguments each function takes is a, b, and mod, the attrabutes of an elliptic curve as described by:

$$y^2 = x^3 + ax + b$$

over the finite field modular the variable mod.
