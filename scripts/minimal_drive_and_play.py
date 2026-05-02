# Import math for angle constants
import math

# Import the AuroraMR robotics simulation library
import AuroraMR as amr


# Create a motion simulation session with initial pose: (0, 0, 0) for a two wheeled kinematic model
s = amr.MotionSession.create(
    amr.pose(0, 0, 0),
    amr.KinematicsModel.TWO_WHEEL,
    dt=0.02 # Simulation time step for Euler integration
)

# Motion command sequence that's executed one after another, not simultaneously

s.forward(1.0, 0.5) # Move forward 1.0 meters at 0.5 m/s in the current heading direction
s.turn_left(math.pi / 4, 1.0) # Rotate left by 45° (pi/4 radians) at 1.0 rad/s
s.forward(0.5, 0.5) # Move forward by 0.5 meters
s.turn_right(math.pi / 6, 1.0) # Rotate right by 30° (pi/6 radians)
s.forward(0.5, 0.5) # Move forward again
s.turn_left(math.pi, 1.0) # Rotate left by 180° (pi radians)
s.forward(1.0, 0.5) # Final forward movement of 1 meter


# This runs the full motion simulation
amr.play_motion(
    s,
    playback_speed=2.0,  # The simulation runs twice as fast as real time
    log=True,            # prints robot state updates to terminal
    show=True            # display animation window
)
