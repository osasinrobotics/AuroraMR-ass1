# This prevents python from executing typehints at runtime and treats them as string initially
from __future__ import annotations

# Import required modules:
# math for angle conversions (degrees to radians)
# os for file paths and environment variables
# matplotlib for plotting and saving the motion path
# AuroraMR: robotics simulation library

import math

import AuroraMR as amr
import matplotlib.pyplot as plt

# A function that converts the angle in degree to radians and returns a Pose object from the amr module
def pose_deg(x: float, y: float, theta_degrees: float) -> amr.Pose:
    """Build a pose with heading ``theta_degrees`` in degrees (north = 0°, CCW)."""
    return amr.pose(x, y, math.radians(theta_degrees))


# Example poses
p_north = pose_deg(0.0, 0.0, 0.0) #Facing North
p_east = pose_deg(1.0, 0.0, 270.0) #Facing East
p_custom = pose_deg(-0.5, 2.0, 45.0) # 45° between North and West

# These prints the pose object and the angle at which it is facing in radians

print("North-facing:", p_north, "theta (rad) =", p_north.theta)
print("East-facing:", p_east, "theta (rad) ≈", round(p_east.theta, 4))
print("45° from north:", p_custom)
print("Read back as degrees:", math.degrees(p_custom.theta))


# These create a figure, adds title and then visualizes the pose
fig, ax = plt.subplots(figsize=(6, 6))
fig.suptitle("Heading 45° CCW from north (degrees → radians inside pose_deg)")
amr.simulate(p_custom, ax=ax, show=False)
plt.show()
