import os

folders = [
    "baseball_mechanics_app/data/raw_videos",
    "baseball_mechanics_app/data/processed_keypoints",
    "baseball_mechanics_app/models/pitching",
    "baseball_mechanics_app/models/hitting",
    "baseball_mechanics_app/mechanics",
    "baseball_mechanics_app/tracking",
    "baseball_mechanics_app/visualization",
    "baseball_mechanics_app/app",
    "baseball_mechanics_app/notebooks"
]

files = {
    "baseball_mechanics_app/main.py": "# Entry point for the app",
    "baseball_mechanics_app/README.md": "# Baseball Mechanics Tracking App\n\nTracks pitching and hitting mechanics from video.",
    "baseball_mechanics_app/models/pitching/supination_model.py": "# Detect supination/pronation from pitching video keypoints",
    "baseball_mechanics_app/models/pitching/arm_slot_model.py": "# Estimate arm slot angles for pitchers",
    "baseball_mechanics_app/models/pitching/kinematics_model.py": "# Analyze kinematic sequence for pitchers",
    "baseball_mechanics_app/models/hitting/bat_path_model.py": "# Analyze bat path from keypoints",
    "baseball_mechanics_app/models/hitting/supination_model.py": "# Detect hitter forearm rotation",
    "baseball_mechanics_app/models/hitting/hip_rotation_model.py": "# Measure hip rotation angles for hitters",
    "baseball_mechanics_app/mechanics/pitching.py": "# High-level pitching analysis module",
    "baseball_mechanics_app/mechanics/hitting.py": "# High-level hitting analysis module",
    "baseball_mechanics_app/tracking/pose_extraction.py": "# Extract pose keypoints from video using MediaPipe or similar",
    "baseball_mechanics_app/tracking/keypoint_utils.py": "# Helper functions for working with keypoints",
    "baseball_mechanics_app/tracking/angle_calculations.py": "# Functions to compute joint angles",
    "baseball_mechanics_app/tracking/motion_features.py": "# Compute biomechanical motion features like rotation",
    "baseball_mechanics_app/visualization/overlay.py": "# Draw pose keypoints on video frames",
    "baseball_mechanics_app/visualization/plots.py": "# Plot metrics like joint angle over time",
    "baseball_mechanics_app/app/streamlit_ui.py": "# Streamlit interface for uploading and analyzing video",
    "baseball_mechanics_app/notebooks/pitching_supination_demo.ipynb": "",  # empty notebook shell
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("✅ Project structure created successfully.")
