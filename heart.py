import numpy as np
import matplotlib.pyplot as plt

# class that plot heart shape using parametric equations
class HeartShape:
    def __init__(self, num_points=1000):
        self.num_points = num_points
        self.t = np.linspace(0, 2 * np.pi, num_points)
        self.x, self.y = self._compute_heart()


    # Equations for forming heart shape
    def _compute_heart(self):
        x = 16 * (np.sin(self.t) ** 3)
        y = 13 * np.cos(self.t) - 5 * np.cos(2 * self.t) - 2 * np.cos(3 * self.t) - np.cos(4 * self.t)
        return x, y
      
    # Plotting graph defined
    def plot(self):
        plt.figure(figsize=(6, 6))
        plt.plot(self.x, self.y, 'r', linewidth=2)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Heart Shape Outline")
        plt.axis("equal")
        plt.show()

# plot the heart shape
heart = HeartShape()
heart.plot()
