import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

# Set up the initial parameters for the ellipse

# the example is the dwarf planet eris

a_init = 10  # initial semi-major axis
b_init = 9  # initial semi-minor axis

# Number of points to plot
theta = np.linspace(0, 2 * np.pi, 1000)

# Set up the plot
fig, ax = plt.subplots()  # Main plot's axes
plt.subplots_adjust(left=0.1, bottom=0.25)  # Adjust plot to make room for sliders

# Plot the Sun, but keep its position updateable
sun, = ax.plot([], [], 'yo', label='Sun')

# Planet position point and orbit line
planet, = ax.plot([], [], 'bo', label='Planet')
orbit_line, = ax.plot([], [], 'b-', label='Planet Orbit')

# Set equal scaling and labels
ax.set_aspect('equal')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()

# Title and grid
ax.set_title("Kepler's First Law: Planetary Orbit")
ax.grid(True)

# Set plot limits
ax.set_xlim(-18, 18)
ax.set_ylim(-12, 12)

# Add sliders for 'a' and 'b'
ax_slider_a = plt.axes([0.1, 0.1, 0.8, 0.03], facecolor='#d83d0e')
ax_slider_b = plt.axes([0.1, 0.15, 0.8, 0.03], facecolor='#d83d0e')

slider_a = Slider(ax_slider_a, 'Semi-Major Axis (a)', 1, 20, valinit=a_init)
slider_b = Slider(ax_slider_b, 'Semi-Minor Axis (b)', 1, 20, valinit=b_init)

# Initialization function
def init():
    planet.set_data([], [])
    orbit_line.set_data([], [])
    sun.set_data([], [])
    return planet, orbit_line, sun

# Animation function
def animate(i):
    a = slider_a.val
    b = slider_b.val
    
    # Calculate the orbit line and sun position based on current 'a' and 'b'
    x = a * np.cos(theta)
    y = b * np.sin(theta)
    orbit_line.set_data(x, y)
    
    # Update the Sun's position only once
    sun.set_data(-np.sqrt(a**2 - b**2), 0)
    
    # Calculate the current angle (i controls the speed)
    angle = 2 * np.pi * i / 200
    planet_x = a * np.cos(angle)
    planet_y = b * np.sin(angle)
    
    planet.set_data(planet_x, planet_y)
    return planet, orbit_line, sun

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=200, interval=20, blit=True)

# Show the animation
plt.show()
