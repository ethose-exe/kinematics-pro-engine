# Engineering & Physics Documentation

### 1. Coordinate System Mapping
In standard Physics, the Y-axis increases upwards. However, in computer graphics (Pygame), the Y-axis increases downwards.
* **Solution:** To render the trajectory correctly, I mapped the calculated height ($y_{phys}$) to the screen using:
  `y_screen = (HEIGHT - GROUND_OFFSET) - (y_phys * SCALE_FACTOR)`

### 2. Time Integration
The engine uses a discrete time-step ($\Delta t$) of `0.04s` per frame to ensure smooth animation while maintaining accuracy with the standard kinematic equation:
$$y = u \sin(\theta)t - \frac{1}{2}gt^2$$

### 3. Scaling & Units
To fit a high-velocity projectile on a 720p monitor, I implemented a scale factor of `4:1`. This means **1 pixel = 0.25 meters** in the simulation world.
