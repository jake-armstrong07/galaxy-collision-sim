# main.py

import numpy as np
from galaxy import create_galaxy
from nbody import step, compute_accelerations
from config import NUM_STEPS, TIME_STEP

# ----------------------------
# Step 1: Initialize galaxies
# ----------------------------

# Galaxy 1: left, moving right
pos1, vel1, mass1 = create_galaxy(
    center=np.array([-1e21, 0, 0]), 
    velocity=np.array([0, 1e4, 0])
)

# Galaxy 2: right, moving left
pos2, vel2, mass2 = create_galaxy(
    center=np.array([1e21, 0, 0]), 
    velocity=np.array([0, -1e4, 0])
)

# Combine all particles
positions = np.vstack((pos1, pos2))
velocities = np.vstack((vel1, vel2))
masses = np.hstack((mass1, mass2))

# Initial accelerations
accelerations = compute_accelerations(positions, masses)

# ----------------------------
# Step 2: Run simulation loop
# ----------------------------

# For saving output frames
history = []

for step_num in range(NUM_STEPS):
    print(f"Step {step_num + 1}/{NUM_STEPS}", end="\r")

    # Save snapshot every N steps
    if step_num % 10 == 0:
        history.append(positions.copy())

    # Advance one time step
    positions, velocities, accelerations = step(
        positions, velocities, masses, accelerations
    )

# ----------------------------
# Step 3: Save data to .npz
# ----------------------------

np.savez_compressed("galaxy_merge_data.npz", snapshots=history)
print("\nSimulation complete. Data saved to galaxy_merge_data.npz")