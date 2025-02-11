import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(num_points):
    """
    Estimate the value of π using Monte Carlo simulation.
    
    Args:
        num_points (int): Number of random points to generate
        
    Returns:
        float: Estimated value of π
        float: Array of points inside circle
        float: Array of points outside circle
    """
    # Generate random points
    x = np.random.uniform(-1, 1, num_points)
    y = np.random.uniform(-1, 1, num_points)
    
    # Calculate distances from origin
    distances = np.sqrt(x**2 + y**2)
    
    # Separate points inside and outside the circle
    inside_circle = distances <= 1
    outside_circle = distances > 1
    
    # Calculate π estimate
    pi_estimate = 4 * np.sum(inside_circle) / num_points
    
    return (pi_estimate, 
            (x[inside_circle], y[inside_circle]), 
            (x[outside_circle], y[outside_circle]))

def visualize_simulation(inside_points, outside_points):
    """
    Create a visualization of the Monte Carlo simulation.
    
    Args:
        inside_points (tuple): x, y coordinates of points inside circle
        outside_points (tuple): x, y coordinates of points outside circle
    """
    plt.figure(figsize=(10, 10))
    
    # Plot circle
    circle = plt.Circle((0, 0), 1, fill=False, color='black')
    plt.gca().add_artist(circle)
    
    # Plot points
    plt.scatter(inside_points[0], inside_points[1], c='blue', alpha=0.6, label='Inside')
    plt.scatter(outside_points[0], outside_points[1], c='red', alpha=0.6, label='Outside')
    
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    plt.title('Monte Carlo Simulation for π Estimation')
    plt.show()

# Run simulation
np.random.seed(42)  # For reproducibility
num_points = 10000
pi_estimate, inside_points, outside_points = estimate_pi(num_points)

# Print results
print(f"Estimated π: {pi_estimate:.6f}")
print(f"Actual π: {np.pi:.6f}")
print(f"Difference: {abs(pi_estimate - np.pi):.6f}")

# Visualize results
visualize_simulation(inside_points, outside_points)