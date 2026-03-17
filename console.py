#!/usr/bin/python3
"""Script to create project folder structure and placeholder Python files."""

import os

# Define directories and files
directories = [
    "models",
    "tests",
    "tests/test_models",
]

files = {
    "models": ["user.py", "place.py", "state.py", "city.py",
               "amenity.py", "review.py", "base_model.py"],
    "tests/test_models": ["test_user.py", "test_place.py", "test_state.py",
                          "test_city.py", "test_amenity.py", "test_review.py",
                          "test_base_model.py"],
}

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create placeholder files with PEP8-compliant content
placeholder_content = '#!/usr/bin/python3\n"""Placeholder file."""\n\n'

for folder, file_list in files.items():
    for file_name in file_list:
        file_path = os.path.join(folder, file_name)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(placeholder_content)

print("Project structure created successfully!")
