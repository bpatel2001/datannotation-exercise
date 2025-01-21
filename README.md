# ASCII Art Renderer from Google Docs Table

This project reads an ASCII art table from a Google Docs URL and renders it into a 2D representation using Python. It processes the data, flips it appropriately to align with the Cartesian coordinate system, and displays the final formatted output.

---

## Features

- Fetches and processes table data from a publicly shared Google Docs URL.
- Converts character data into a 2D numpy array.
- Adjusts the y-axis for correct orientation (Cartesian-style bottom-left origin).
- Outputs the rendered ASCII art in a formatted, readable manner.

---

## Prerequisites

Ensure you have the following installed:

- **Python 3.6+**
- Python libraries:
  - `pandas`
  - `numpy`

You can install the required libraries using:
```bash
pip install pandas numpy
