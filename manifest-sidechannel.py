import os

for file in os.listdir("src-sidechannel"):
    module(file, base_path="src-sidechannel")
