
# Grid Navigation Agent

This project implements a grid-based AI agent designed to analyze a map and determine the best movement actions to reach water (`W`) cells from a given starting cell type (`M`, `C`, or `B`).

##  Agent Logic

The agent uses the following logic:
- It parses the map and identifies all cells matching the `current-cell` observation.
- From each such cell:
  - It checks if a `W` cell is located **directly south**. If yes, that cell is considered a possible move.
  - If not, it checks if there's a `W` cell **to the east** of that cell.
- Based on the number of successful actions and their estimated time, it calculates:
  - `success-chance`: Probability of successfully reaching a `W` cell.
  - `expected-time`: Average time to reach a `W` cell.

## Example Input Maps

