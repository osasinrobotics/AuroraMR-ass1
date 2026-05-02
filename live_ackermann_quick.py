# This prevents python from executing typehints at runtime and treats them as string initially
from __future__ import annotations 

# Import the AuroraMR robotics library and module namespace as 'amr'
import AuroraMR as amr

# If we are executing this script directly then run this block
if __name__ == "__main__":
    amr.play_motion_by_kind(  
        "ackermann",          
        interval_ms=28,
        playback_speed=1,
        show=True,
        log=True,
        log_every_n_frames=10,
        log_detailed=True,
    )

"""
amr.play_motion_by_kind: 

This function runs a predefined motion for a specified vehicle model (e.g, Ackermann steering).

It has the following parameters:

- the vehicle model used in simulation: in this case its the ackermann sterring model
- the interval_ms: the time between frames, defined here as 28.
- playback_speed is the speed at which the simulation runs
- show : It enables/disables visualization
- log: it enables/disables the printing of the robot's state info to the terminal
- log_every_n_frames: prints the logs every n frames
- log_detailed: Should the logs be basic info or detailed?

When log_detailed=True, more data is shown:
- Pose in world frame (x, y, θ)
- Estimated velocities (v, ω) through finite differences
- Vehicle geometry points (wheel contacts, body corners)

"""


