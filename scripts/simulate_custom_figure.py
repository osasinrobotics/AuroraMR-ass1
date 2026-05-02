#!/usr/bin/env python3
"""Use your own matplotlib figure: ``ax=`` and ``show=False``, then save or show.

For machines without a display, run with a non-GUI backend, e.g.:
  MPLBACKEND=Agg python simulate_custom_figure.py
"""

# This prevents python from executing type hints at runtime and treats them as strings initially

from __future__ import annotations

# Import required modules:
# math for angle conversions (degrees to radians)
# os for file paths and environment variables
# matplotlib for plotting and saving the motion path
# AuroraMR robotics simulation library

import math
import os
import matplotlib.pyplot as plt
import AuroraMR as amr

# For a headless run: ``MPLBACKEND=Agg python simulate_custom_figure.py``
"""
Pose definition
x = 0.5
y = -1.0
θ = 30°, converted to radians
"""

p = amr.pose(0.5, -1.0, math.radians(30))

# This creates a matplotlib figure and axis and then a title is added
fig, ax = plt.subplots(figsize=(7, 7))
fig.suptitle("Custom figure: AuroraMR simulate on supplied axes")


# This simulates and draws the robot pose on the provided axis
amr.simulate(p, ax=ax, show=False)
fig.tight_layout()

# This creates a file path to save the image in the same directory as this script and saves the figure as an image file
out = os.path.join(os.path.dirname(__file__), "custom_figure_example.png")
fig.savefig(out, dpi=150) # The resolution of the image: dpi

# Confirmation message
print("Wrote", out)

# If you have a display, you can still show:
# plt.show()
