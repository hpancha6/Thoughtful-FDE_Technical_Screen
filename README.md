# Thoughtful-FDE_Technical_Screen
# Package Sorter

This project contains a Python function `sort()` that classifies packages based on their dimensions and mass.

## Classification Rules

- A package is **Bulky** if:  
  - Any dimension (`width`, `height`, or `length`) is **≥ 150 cm**, or  
  - The volume (`width × height × length`) is **≥ 1,000,000 cubic cm**.  

- A package is **Heavy** if:  
  - The mass is **≥ 20 kg**.  

- Final classification:  
  - **REJECTED** if both bulky and heavy.  
  - **SPECIAL** if either bulky or heavy.  
  - **STANDARD** otherwise.  

## Function Signature

```python
def sort(width: int, height: int, length: int, mass: int) -> str:
