Galaxy Collision Simulation

A Python-based astrophysics project simulating the gravitational interaction and merger of two galaxies.
This repository models the dynamics of star particles in two galaxies, including dark matter halos, and creates animated visualizations of their collision and merger process.

⸻

Features
	•	Simulates galaxies as collections of particles with 3D positions and velocities
	•	Includes dark matter halos influencing galaxy dynamics
	•	Uses Newtonian gravity to calculate forces between particles
	•	Generates animations of the merger process as .mp4 videos
	•	Configurable initial conditions for galaxy mass, velocity, and position
	•	Modular codebase: main.py for simulation, visualize.py for rendering animations

⸻

Requirements
	•	Python 3.8+
	•	Packages: numpy, matplotlib
	•	FFmpeg installed for video rendering (required by matplotlib.animation)

Install Python packages with:
pip install numpy matplotlib

FFmpeg installation (Linux example):
sudo apt-get install ffmpeg

⸻

Usage
	1.	Configure initial conditions:
Edit config.py to set galaxy masses, initial positions, and velocities.
	2.	Run the simulation:
python main.py
This simulates the galaxy collision and saves the particle trajectories to data/simulation_data.npz.
	3.	Visualize the results:
python visualize.py
This creates and displays an animation of the collision, saving it as galaxy_merger.mp4.

⸻

Project Structure
	•	config.py              # Simulation parameters and initial galaxy setups
	•	galaxy.py              # Galaxy class managing particles and forces
	•	main.py                # Runs the simulation, outputs particle data
	•	visualize.py           # Creates animations from simulation data
	•	data/                  # Simulation outputs (e.g., .npz files)
	•	media/                 # Animation videos (e.g., .mp4 files)
	•	.gitignore             # Git ignore rules for outputs and caches
	•	README.md              # This file

⸻

Future Improvements
	•	Add multiple galaxy interactions (e.g., galaxy clusters)
	•	Incorporate more realistic dark matter halo models
	•	Add user controls to change camera angle or zoom in animation
	•	Parallelize force calculations for larger simulations
	•	Export data for further analysis or 3D interactive visualization

⸻

License

This project is open source and free to use under the MIT License.

⸻

Contact

Created by [Your Name] – feel free to open issues or submit pull requests!