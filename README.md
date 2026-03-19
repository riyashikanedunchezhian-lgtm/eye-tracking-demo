# Eye-Tracking Accuracy Benchmark (Demo)

## ⚠️ Disclaimer

This project is a **demo prototype** built as part of preparation for a Google Summer of Code (GSoC) proposal.

It is not a full-scale benchmarking system, but a **conceptual implementation** demonstrating how eye-tracking accuracy can be evaluated using basic metrics and visualization.

---

## 📌 Overview

Eye-tracking systems predict where a user is looking on a screen.
To evaluate their performance, we compare:

* **Actual gaze points (ground truth)**
* **Predicted gaze points (model output)**

This project computes the **spatial error** between these points and provides simple visual insights.

---

## 🎯 Features

* 📊 Simulated dataset for gaze prediction
* 📏 Euclidean distance-based error calculation
* 📈 Statistical metrics:

  * Average error
  * Minimum error
  * Maximum error
  * Standard deviation
* 📉 Visualizations:

  * Scatter plot (Actual vs Predicted)
  * Error heatmap

---

## 🧠 Methodology

The accuracy is calculated using the Euclidean distance between actual and predicted points:

d = √((x₂ - x₁)² + (y₂ - y₁)²)

Where:

* (x₁, y₁) → Actual gaze point
* (x₂, y₂) → Predicted gaze point

---

## 🛠️ Tech Stack

* Python
* NumPy
* Pandas
* Matplotlib

---

## 📁 Project Structure

eye-tracking-demo/
│── main.py
│── README.md
│── requirements.txt

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone https://github.com/your-username/eye-tracking-demo.git
cd eye-tracking-demo
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the project:

```
python main.py
```

---

## 📊 Output

The program generates:

* A table of actual vs predicted gaze points with computed error
* Summary statistics of accuracy
* Visual plots showing:

  * Spatial deviation
  * Error distribution

---

## 🚀 Future Improvements

* Integration with real eye-tracking datasets
* Advanced error metrics (e.g., angular error)
* Real-time evaluation support
* Interactive dashboard for visualization
* Cross-device benchmarking

---

## 🎓 Purpose

This demo is created to demonstrate:

* Understanding of benchmarking concepts
* Ability to work with spatial data
* Basic statistical analysis and visualization

---

## 🤝 Acknowledgment

This project is part of my learning journey and preparation for contributing to open-source projects through GSoC.

---

## 📬 Contact

Feel free to connect for feedback or collaboration!
