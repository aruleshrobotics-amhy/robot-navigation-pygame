# Real-Time Robot Navigation Simulator (Pygame)

This project demonstrates a **real-time autonomous robot navigation simulator** built using Python and Pygame.

The simulation visualizes how a robot continuously senses obstacles and makes movement decisions inside a grid-based environment — similar to real robotic control systems.

---

## 🎥 Simulation Demo

The video below shows the robot navigating the environment in real time and avoiding obstacles automatically.

https://github.com/aruleshrobotics-amhy/robot-navigation-pygame/assets/REPLACE_WITH_YOUR_VIDEO_ID

> 📌 If the video does not auto-play, click the link to view it directly.

---

## 🚀 Features

- Real-time simulation window
- Autonomous robot movement
- Obstacle detection and avoidance
- Grid-based environment visualization
- Continuous control loop (frame-based execution)

---

## 🧠 Project Design

### Environment
- Represented as a 2D grid
- `0` → Free space  
- `1` → Obstacle  
- Grid boundaries treated as obstacles

### Robot
- Maintains current position `(x, y)`
- Maintains direction (`N`, `E`, `S`, `W`)
- Moves autonomously using reactive control logic
- Changes direction when obstacles are detected

### Control Logic
- Runs inside a real-time game loop
- Each frame updates robot state and redraws the environment
- Frame rate controls robot movement speed

---

## 🗂️ Project Structure

- **main.py** – Game loop, rendering, and simulation control  
- **robot.py** – Robot movement and navigation logic  
- **environment.py** – Grid definition and obstacle handling  
- **README.md** – Project documentation  

---

## ▶️ How to Run

1. Install dependencies:
   
   pip install pygame

2. Run the simulation:

    python main.py

## 🔌 Mapping to Real Robotics Systems

| Robotics Concept | Simulation Equivalent |
| ---------------- | --------------------- |
| Control loop     | Pygame game loop      |
| Motor movement   | Position updates      |
| Obstacle sensor  | Collision detection   |
| Robot body       | Rendered shape        |
| Debug monitoring | Visual simulation     |

## ⚠️ Limitations

Reactive navigation only

No global path planning

Fixed movement speed

No physics-based dynamics

These limitations are intentional to keep the focus on core control logic.

## 🔮 Future Enhancements

Keyboard/manual control

Smarter navigation strategies

ROS2-based node implementation

Physics-based simulation

Integration with 3D visualization tools

## 👤 Author

Arulesh P P

Robotics-Oriented Python Software Engineer