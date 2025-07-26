# galaxy.py

import numpy as np
from config import (
    NUM_STARS,
    NUM_DM_PARTICLES,
    STAR_MASS,
    DM_PARTICLE_MASS,
    GALAXY_RADIUS,
    INITIAL_VELOCITY
)

# -------------------------------
# Rotating Stellar Disc Generator
# -------------------------------

def generate_stellar_disc(center, velocity, num_particles=NUM_STARS):
    """
    Generate a rotating stellar disc with particles in a flat, circular shape.
    """
    positions = []
    velocities = []

    for _ in range(num_particles):
        # Exponential disc: random radius and angle in 2D
        r = GALAXY_RADIUS * np.sqrt(np.random.rand())
        theta = 2 * np.pi * np.random.rand()

        # Position in galaxy-centered coordinates
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        z = GALAXY_RADIUS * 0.05 * (np.random.rand() - 0.5)  # Thin disc

        pos = np.array([x, y, z]) + center
        positions.append(pos)

        # Circular velocity (tangential)
        v_circ = np.sqrt(6.67430e-11 * STAR_MASS * num_particles / (r + 1e18))  # softened

        vx = -v_circ * np.sin(theta)
        vy =  v_circ * np.cos(theta)
        vz = 0

        vel = np.array([vx, vy, vz]) + velocity
        velocities.append(vel)

    # Convert to numpy arrays
    positions = np.array(positions)
    velocities = np.array(velocities)
    masses = np.full(num_particles, STAR_MASS)

    return positions, velocities, masses


# ---------------------------------
# Spherical Dark Matter Halo Creator
# ---------------------------------

def generate_dark_matter_halo(center, velocity, num_particles=NUM_DM_PARTICLES):
    """
    Generate a spherical dark matter halo with uniformly distributed particles.
    """
    positions = []
    velocities = []

    for _ in range(num_particles):
        # Uniform random spherical distribution
        r = GALAXY_RADIUS * (np.random.rand() ** (1/3))  # Uniform sphere
        theta = np.arccos(1 - 2 * np.random.rand())
        phi = 2 * np.pi * np.random.rand()

        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)

        pos = np.array([x, y, z]) + center
        positions.append(pos)

        # No initial spin for halo particles
        vel = np.array(velocity)
        velocities.append(vel)

    positions = np.array(positions)
    velocities = np.array(velocities)
    masses = np.full(num_particles, DM_PARTICLE_MASS)

    return positions, velocities, masses


# -----------------------
# Combined Galaxy Builder
# -----------------------

def create_galaxy(center, velocity):
    """
    Generate a full galaxy with a stellar disc and a dark matter halo.
    Returns:
        positions: (N, 3) ndarray
        velocities: (N, 3) ndarray
        masses: (N,) ndarray
    """
    star_pos, star_vel, star_mass = generate_stellar_disc(center, velocity)
    dm_pos, dm_vel, dm_mass = generate_dark_matter_halo(center, velocity)

    positions = np.vstack((star_pos, dm_pos))
    velocities = np.vstack((star_vel, dm_vel))
    masses = np.hstack((star_mass, dm_mass))

    return positions, velocities, masses