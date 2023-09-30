import os

for file in os.listdir("src"):
    module(file, base_path="src")
