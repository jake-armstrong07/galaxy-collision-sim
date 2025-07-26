# nbody.py

import numpy as np
from config import G, SOFTENING_LENGTH, TIME_STEP

# ------------------------------
# Gravitational Acceleration
# ------------------------------

def compute_accelerations(positions, masses):
    """
    Compute gravitational acceleration on each particle due to every other.
    Uses pairwise Newtonian gravity with softening.
    
    Args:
        positions: (N, 3) ndarray of positions
        masses: (N,) ndarray of masses

    Returns:
        accelerations: (N, 3) ndarray of accelerations
    """
    N = positions.shape[0]
    accelerations = np.zeros_like(positions)

    for i in range(N):
        # Vector separation from particle i to all others
        dx = positions - positions[i]
        dist_squared = np.sum(dx**2, axis=1) + SOFTENING_LENGTH**2
        inv_dist3 = dist_squared ** (-1.5)
        inv_dist3[i] = 0  # self-interaction = 0

        acc = G * np.sum((dx.T * inv_dist3 * masses).T, axis=0)
        accelerations[i] = acc

    return accelerations


# ------------------------------
# Leapfrog Integrator (Velocity-Verlet)
# ------------------------------

def leapfrog_step(positions, velocities, masses, accelerations, dt=TIME_STEP):
    """
    Perform a single leapfrog integration step.

    Args:
        positions: (N, 3) ndarray
        velocities: (N, 3) ndarray
        masses: (N,) ndarray
        accelerations: (N, 3) ndarray
        dt: float (time step)

    Returns:
        new_positions, new_velocities, new_accelerations
    """
    # Half-step velocity update
    v_half = velocities + 0.5 * accelerations * dt

    # Full-step position update
    new_positions = positions + v_half * dt

    # Compute new accelerations
    new_accelerations = compute_accelerations(new_positions, masses)

    # Final half-step velocity update
    new_velocities = v_half + 0.5 * new_accelerations * dt

    return new_positions, new_velocities, new_accelerations


# ------------------------------
# Wrapper Function for One Step
# ------------------------------

def step(positions, velocities, masses, accelerations, dt=TIME_STEP):
    """
    Advances the system by one timestep using Leapfrog integration.
    
    Returns:
        Updated positions, velocities, and accelerations.
    """
    return leapfrog_step(positions, velocities, masses, accelerations, dt)