# visualize.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from config import NUM_STARS, NUM_DM_PARTICLES

# Load the simulation data
data = np.load("galaxy_merge_data.npz")
snapshots = data["snapshots"]

# Constants
total_particles = 2 * (NUM_STARS + NUM_DM_PARTICLES)
num_frames = len(snapshots)

# Split particle types
num_star_particles = 2 * NUM_STARS
num_dm_particles = 2 * NUM_DM_PARTICLES

# Set up the plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-2e21, 2e21)
ax.set_ylim(-2e21, 2e21)
ax.set_zlim(-2e21, 2e21)
ax.set_title("Galaxy Merger Simulation")

stars_plot = ax.scatter([], [], [], s=1, c='yellow', label='Stars')
dm_plot = ax.scatter([], [], [], s=1, c='blue', alpha=0.3, label='Dark Matter')

# Animation function
def update(frame):
    ax.cla()  # Clear the previous frame
    ax.set_xlim(-2e21, 2e21)
    ax.set_ylim(-2e21, 2e21)
    ax.set_zlim(-2e21, 2e21)
    ax.set_title(f"Galaxy Merger - Frame {frame + 1}/{num_frames}")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    positions = snapshots[frame]

    # Star and DM separation
    star_pos = positions[:num_star_particles]
    dm_pos = positions[num_star_particles:]

    ax.scatter(star_pos[:, 0], star_pos[:, 1], star_pos[:, 2], s=1, c='gold', label='Stars')
    ax.scatter(dm_pos[:, 0], dm_pos[:, 1], dm_pos[:, 2], s=1, c='cyan', alpha=0.2, label='Dark Matter')

    ax.legend(loc='upper left')

# Animate
ani = FuncAnimation(fig, update, frames=num_frames, interval=40)
ani.save("galaxy_merger.mp4", writer=FFMpegWriter(fps=30))
plt.show()