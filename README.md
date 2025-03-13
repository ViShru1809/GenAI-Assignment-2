# GenAI-Assignment-2
Forming heart shaped plotting _ function finding

## Description
This project creates a simple heart shape using Python with NumPy and Matplotlib. The heart shape is drawn using mathematical equations and displayed as a plot.

## **How It Works**
The heart shape is defined using the equations:
```sh
\[ x = 16 \sin^3(t) \]
\[ y = 13 \cos(t) - 5 \cos(2t) - 2 \cos(3t)- \cos(4t)\]
```

The script:
1. Defines a `HeartShape` class to generate the heart shape.
2. Uses `numpy` to calculate `x` and `y` values for smooth plotting.
3. Uses `matplotlib` to create and display the heart shape plot.

## **Requirements**
- NumPy
- Matplotlib

Install dependencies using:
```sh
pip install numpy matplotlib
```

## **How to Run the Script**
1. Download the script `heart.py`.
2. Open a terminal or command prompt.
3. Navigate to the folder where the script is located.
4. Run the command:
   ```sh
   python heart.py
   ```
5. A heart shape plot will appear on the screen.
