import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# DEMO DATA (Simulated)
# -----------------------------
data = {
    "actual_x": [100, 200, 300, 400, 500],
    "actual_y": [200, 300, 400, 500, 600],
    "pred_x":   [110, 190, 310, 390, 480],
    "pred_y":   [210, 290, 420, 480, 610],
}

df = pd.DataFrame(data)

# -----------------------------
# ERROR CALCULATION
# -----------------------------
df["error"] = np.sqrt(
    (df["actual_x"] - df["pred_x"])**2 +
    (df["actual_y"] - df["pred_y"])**2
)

# -----------------------------
# METRICS
# -----------------------------
avg_error = df["error"].mean()
max_error = df["error"].max()
min_error = df["error"].min()
std_error = df["error"].std()

print("=== Eye Tracking Accuracy Report (Demo) ===")
print(df)
print("\nAverage Error:", avg_error)
print("Max Error:", max_error)
print("Min Error:", min_error)
print("Std Deviation:", std_error)

# -----------------------------
# VISUALIZATION 1: Scatter Plot
# -----------------------------
plt.figure()
plt.scatter(df["actual_x"], df["actual_y"], label="Actual")
plt.scatter(df["pred_x"], df["pred_y"], label="Predicted")

for i in range(len(df)):
    plt.plot(
        [df["actual_x"][i], df["pred_x"][i]],
        [df["actual_y"][i], df["pred_y"][i]],
        linestyle="--"
    )

plt.legend()
plt.title("Eye Tracking Accuracy (Demo)")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.show()

# -----------------------------
# VISUALIZATION 2: Error Heatmap
# -----------------------------
plt.figure()
plt.scatter(df["actual_x"], df["actual_y"], c=df["error"])
plt.colorbar(label="Error Magnitude")
plt.title("Error Heatmap (Demo)")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.show()