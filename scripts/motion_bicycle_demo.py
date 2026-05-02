
# This prevents python from executing typehints at runtime and treats them as string initially
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

# This sets the matplotlib backend to "Agg" so plots are saved as images instead of displayed in a GUI window
os.environ.setdefault("MPLBACKEND", "Agg")
#os.environ.setdefault("MPLBACKEND", "TkAgg")

# This defines the parameters for the bicycle kinematic model
params = amr.BicycleParams(
    wheelbase=0.55,          # Distance between front and rear axle
    rear_track_width=0.36,   # Distance between rear wheels
    max_steering_angle=0.5,  # Maximum steering angle (radians)
    max_speed=1.0,           # Maximum linear speed (m/s)
)


# This creates a motion session
session = amr.MotionSession.create(
    amr.pose(0.0, 0.0, 0.0),          # Initial pose: (x=0, y=0, θ=0, facing North)
    amr.KinematicsModel.BICYCLE,      # Use the bicycle kinematic model
    dt=0.02,                          # Time step for Euler integration
    bicycle=params,                   # The parameters of the bicycle kinematic model
)


# This executes the motion commands sequentially:
session.forward(2.0, 0.6)                 # Move forward by 2 meters at 0.6 m/s
session.turn_left(math.radians(40), 0.8)  # Turn left 40° at 0.8 rad/s
session.forward(1.5, 0.5)                 # Move forward 1.5 meters at 0.5 m/s

# This creates a plot figure
fig, ax = plt.subplots(figsize=(8, 8))

# This plots the robot's trajectory without displaying it
amr.plot_motion(session, ax=ax, show=False)

"""
for frame in session:
    ax.clear()
    amr.plot_motion(session, ax=ax, show=False)
    plt.pause()
plt.show()
"""


# Saves the plotted trajectory as an image file and then prints a confirmation message
fig.savefig(os.path.join(os.path.dirname(__file__), "motion_bicycle_demo.png"), dpi=150)
print("Saved motion_bicycle_demo.png (BicycleParams → Ackermann four-wheel)")
