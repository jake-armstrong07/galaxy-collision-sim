# config.py

# Physics constants
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2

# Simulation parameters
TIME_STEP = 1e13         # seconds (approx ~300k years)
NUM_STEPS = 10000         # number of integration steps

# Galaxy parameters
NUM_STARS = 500          # number of star particles per galaxy
NUM_DM_PARTICLES = 1000  # number of dark matter halo particles per galaxy

# Galaxy mass in kg (solar mass ~ 2e30 kg)
STAR_MASS = 2e30         # 1 solar mass per star particle
DM_PARTICLE_MASS = 1e32  # Dark matter particle heavier to mimic halo

# Galaxy sizes (meters)
GALAXY_RADIUS = 5e20     # ~50,000 light years radius

# Softening length to avoid singularities in force calculation (meters)
SOFTENING_LENGTH = 1e19

# Initial relative velocity between galaxies (m/s)
INITIAL_VELOCITY = 2e5   # ~200 km/s typical for colliding galaxies# config.py