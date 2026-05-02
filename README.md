# AuroraMR Library Exploration

This repository contains my exploration and annotated understanding of the AuroraMR robotics simulation library.

The aim was to understand how mobile robot motion is represented, simulated, and visualized, rather than just running example scripts.

---

# What I learned

- Robot pose representation (x, y, θ) and its meaning in the world frame  
- Difference between world frame and body frame  
- Unicycle and bicycle (Ackermann) kinematic models  
- How velocity-based commands generate motion over time  
- Euler integration for updating robot state in small time steps  
- Handling angles in both degrees and radians  
- Using matplotlib for simulation visualization and output saving

# Scripts explored

- live_ackermann_quick.py  
- minimal_drive_and_play.py  
- motion_bicycle_demo.py  
- pose_and_simulate_degrees.py  
- simulate_custom_figure.py  
