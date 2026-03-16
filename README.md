<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0f172a&height=150&section=header&text=PRISM_KINEMATICS&fontSize=50&fontColor=38bdf8&animation=fadeIn" width="100%" />
</p>

### 🛰️ <samp>system.status // HIGH_FIDELITY_ACTIVE</samp>

> **PRISM** is a high-performance motion analysis engine designed to visualize Newtonian kinematics with a modern, aeronautical-grade interface. Built for precision and aesthetic clarity.

---

### ⚡ Technical Specifications
* **Chroma-Velocity Mapping:** Real-time color shifting based on kinetic energy.
* **Particle Emission System:** Dynamic plume visualization for trajectory tracking.
* **Deterministic Physics:** Calculations powered by standard gravity $g = 9.81 m/s^2$.
* **Glassmorphism HUD:** Real-time telemetry feed for $u$, $\theta$, $H_{max}$, and $Range$.

### 📐 Engineering Formulas (BITSAT Optimized)
The engine solves the trajectory equation for every frame:
$$y = x \tan(\theta) - \frac{gx^2}{2u^2 \cos^2(\theta)}$$

Current version utilizes:
* **Time of Flight:** $T = \frac{2u \sin\theta}{g}$
* **Maximum Height:** $H = \frac{u^2 \sin^2\theta}{2g}$

---

### 🛠️ Installation & Execution
```bash
# Clone the core
git clone [https://github.com/ethose-exe/kinematics-pro-engine.git](https://github.com/ethose-exe/kinematics-pro-engine.git)

# Install dependencies
pip install pygame-ce --pre

# Execute Engine
python main.py
