# Mystery Module

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)

A lightweight Python module for solving quadratic equations using the quadratic formula. This module provides a simple function to calculate the roots of a quadratic equation of the form `ax² + bx + c = 0`.

## Features

- Computes real roots of quadratic equations
- Returns `None` for equations with no real solutions
- Pure Python implementation with no external dependencies
- Type hints for better IDE support

## Installation

### From Source

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/mystery-module.git
   cd mystery-module
   ```

2. Import the module in your Python code:
   ```python
   from mystery_module import fn_x
   ```

### Requirements

- Python 3.6 or higher
- Standard library only (no external dependencies)

## Usage

### Basic Example

```python
from mystery_module import fn_x

# Solve x² - 3x + 2 = 0
roots = fn_x(1, -3, 2)
print(roots)  # (2.0, 1.0)

# Equation with no real roots: x² + x + 1 = 0
roots = fn_x(1, 1, 1)
print(roots)  # None
```

### API Reference

#### `fn_x(a: float, b: float, c: float) -> tuple[float, float] | None`

Calculates the roots of a quadratic equation using the quadratic formula.

**Parameters:**

- `a` (float): Coefficient of x² term (must be non-zero)
- `b` (float): Coefficient of x term
- `c` (float): Constant term

**Returns:**

- `tuple[float, float]`: A tuple containing the two roots (x₁, x₂) where x₁ ≥ x₂
- `None`: If the equation has no real roots (discriminant < 0)

**Raises:**

- No exceptions are raised; returns `None` for invalid cases

**Examples:**

```python
# Perfect square: (x - 1)² = 0
fn_x(1, -2, 1)  # (1.0, 1.0)

# Real roots: 2x² - 4x - 6 = 0
fn_x(2, -4, -6)  # (3.0, -1.0)

# Complex roots: x² + 1 = 0
fn_x(1, 0, 1)   # None
```

## Mathematical Background

The quadratic formula is: `x = (-b ± √(b² - 4ac)) / (2a)`

Where the discriminant `D = b² - 4ac` determines the nature of roots:

- `D > 0`: Two distinct real roots
- `D = 0`: One repeated real root
- `D < 0`: Two complex roots (returns `None`)

## Testing

Run the included tests:

```bash
python -m pytest test_mystery_module.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is for educational purposes. No specific license applied.

## Acknowledgments

- Based on the standard quadratic formula from algebra
- Inspired by mathematical utility libraries

## Contact

If you have any questions or suggestions, please open an issue on GitHub.
