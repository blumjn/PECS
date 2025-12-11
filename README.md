# PECS

An in-progress and very new project for Proximity Effect Correction for Raith Voyager EBL. 
Code is under development and unstable



## Table of Contents
* [Project Details](#project-details)
    * [Proximity Effect Correction and the Raith Voyager EBL](#proximity-effect-correction-and-the-raith-voyager-ebl)
    * [Particle Swarm Optimization](#particle-swarm-optimization)
* [Requirements](#requirements)
* [Implementation](#implementation)
    * [Entry Point](#entry-point)
    * [State Machine-based Structure](#state-machine-based-structure)
    * [Targets, Thresholds, Boundaries, and Constraints](#targets-thresholds-boundaries-and-constraints) 
    * [Objective Function Handling](#objective-function-handling)
* [PECS Objective Function](#pecs-objective-function)
* [Algorithm, Results, and the Rest ](#algorithm-results-and-the-rest)
* [References](#references)
* [Related Publications and Repositories](#related-publications-and-repositories)
 



## Project Details

(2-3 sentence intro summary here)

### Proximity Effect Correction and the Raith Voyager EBL
    (We'll get to this in a bit. A link or pic from online would be cool here)


### Particle Swarm Optimization

    Particle Swarm Optimization (PSO) is a popular nature-inspired optimization algorithm introduced in "Particle Swarm Optimization" [1] (J. Kennedy & R. Eberhart, 1995). It is inspired by the social behavior animal groups, often compared to birds flocking or fish schooling. PSO is used to find approximate solutions to complex optimization problems.

    PSO consists of a population (or swarm) of candidate solutions called particles. Each particle moves through the search space, influenced by its own best-known position and the best-known positions of the swarm. The algorithm combines exploration and exploitation to find the optimal solution.

From: [pso_python](https://github.com/jonathan46000/pso_python)

The particle swarm optimizer used in this work has been adapted from the [pso_python](https://github.com/jonathan46000/pso_python) repository. 

The following changes have been made to the swarm algorithm:
1. 
2. 

With the following being adapted into an objective function:
1. 
2. 
3. 
More information on the [PECS Objective Function](#pecs-objective-function) is detailed in this README.





## Requirements

This project requires numpy, pandas, and matplotlib for the full demos. To run the optimizer without visualization, only numpy and pandas are requirements. 

This version works on Python 3.9 and higher.


Use 'pip install -r requirements.txt' to install the following dependencies:

old requirements.txt (still checking if imports are missing)
```python
contourpy==1.2.1
cycler==0.12.1
fonttools==4.51.0
importlib_resources==6.4.0
kiwisolver==1.4.5
matplotlib==3.8.4
numpy==1.26.4
packaging==24.0
pandas==2.2.3
pillow==10.3.0
pyparsing==3.1.2
python-dateutil==2.9.0.post0
pytz==2025.1
six==1.16.0
tzdata==2025.1
zipp==3.18.1

```


new requirements.txt (still checking if imports are missing)
```python
contourpy==1.2.1
cycler==0.12.1
fonttools==4.51.0
importlib_resources==6.4.0
kiwisolver==1.4.5
matplotlib==3.8.4
numpy==1.26.4
packaging==24.0
pandas==2.2.3
pillow==10.3.0
pyparsing==3.1.2
python-dateutil==2.9.0.post0
pytz==2025.1
six==1.16.0
tzdata==2025.1
zipp==3.18.1
```



Optionally, requirements can be installed manually with:
```
pip intall pandas numpy matplotlib

```


## Implementation
(what is this and what did we do 2-5 sentences)

### Entry Point
(where to run the program from)


### State Machine-based Structure
(how the optimizer algorithm works and what the state machine setup lets us do with simulation - Lauren has this in her repos)


### Targets, Thresholds, Boundaries, and Constraints
(how these work with the optimizer)


(PECS and raith specific setups)


### Objective Function Handling
(how this works with the optimizer)


## PECS Objective Function

(PECS and raith specific setups)
the configs and global vars
what was experimetnal and hardet, which of the vars came from working with the machine


## Algorithm, Results, and the Rest

numbers go in, science comes out. What's the process. We could probably use a mermaid plot here


## References
[1] J. Kennedy and R. Eberhart, "Particle swarm optimization," Proceedings of ICNN'95 - International Conference on Neural Networks, Perth, WA, Australia, 1995, pp. 1942-1948 vol.4, doi: 10.1109/ICNN.1995.488968.
[2] Jonathan Lundquist (jonathan46000), “Jonathan46000/pso_python: Simple particle swarm optimizer written in Python,” GitHub, https://github.com/jonathan46000/pso_python (accessed Dec. 11, 2025). 

## Related Publications and Repositories
[1] for example, papers
[2] other repos that might spawn from this, not the original pso one 