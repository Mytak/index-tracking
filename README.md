# Financial Index Tracker
Tracking financial indexes is a key application of portfolio optimization, particularly when dealing with indexes that include hundreds or thousands of assets. To make portfolio management more feasible, the goal is often to replicate the index using a smaller, more manageable subset of assets, which is known as applying cardinality constraints. This form of constrained portfolio optimization is highly complex, and conventional algorithms frequently struggle to find suitable solutions.
This project formulates the index tracking problem as a QUBO (Quadratic Unconstrained Binary Optimization) and uses quantum optimization to minimize tracking error while handling real-world constraints. 
Ideal for experimenting with quantum computing in financial optimization.
This is a usable application designed to optimize index tracking portfolios using D-Wave’s quantum annealers, though it can also serve a pedagogical purpose for users learning about quantum computing in finance.
It targets advanced users who are familiar with optimization problems, portfolio management, and have a solid understanding of D-Wave’s Ocean tools, though it could also serve as a learning tool for motivated beginners.

![D-Wave Logo](dwave_logo.png)

## Usage

```bash
python financial_index_tracker.py
```

### Inputs
Financial index to track, for example NASDAQ

### Outputs
Cardinality constraints = Limited subset of assets which replicate the financial index performance

## Problem Description 

Objectives to be optimized: the goals the process attempts to accomplish by minimizing or maximizing certain aspects of the problem to the extent possible; for example, a production-line optimization might attempt to minimize the time to produce all of the products.

Constraints: aspects of the problem and/or process, with limited or no flexibility, that must be satisfied for solutions to be considered feasible; for example, a production-line optimization might have a limitation that Machine A can only bend 10 parts per hour.

## Model Overview
The clearer your model is presented here, the more useful it will be to others. For a strong example of this section, see [here](https://github.com/dwave-examples/3d-bin-packing#model-overview).

### Parameters
List and define the parameters used in your model.

### Variables
List and define (including type: e.g., "binary" or "integer") the variables solved for in your model.

### Expressions
List and define any combinations of variables used for easier representations of the models.

### Objective
Mathematical formulation of the objective described in the previous section using the listed parameters, variables, etc.

### Constrains
Mathematical formulation of the constraints described in the previous section using the listed parameters, variables, etc.

## Code Overview

A general overview of how the code works.

We prefer descriptions in bite-sized bullet points:

* Here's an example bullet point

## Code Specifics

Notable parts of the code implementation.

This is the place to:

* Highlight a part of the code implementation
* Talk about unusual or potentially difficult parts of the code
* Explain a code decision
* Explain how parameters were tuned

Note: there is no need to repeat everything that is already well-documented in
the code.

## References
Samuel Palmer, Konstantinos Karagiannis, Adam Florence, Asier Rodriguez, Román Orús, Harish Naik, Samuel Mugel, 
"Financial Index Tracking via Quantum Computing with Cardinality Constraints", https://ar5iv.labs.arxiv.org/html/2208.11380

## License

Released under the Apache License 2.0. See [LICENSE](LICENSE) file.
