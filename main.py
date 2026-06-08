import subprocess
from pathlib import Path

BLENDER = r"C:\Program Files\Blender Foundation\Blender 5.1\blender.exe"
BLEND_FILE = str(Path("trillon.blend").resolve())

start_frame = 197
end_frame = 510

for frame in range(start_frame, end_frame + 1):
    print(f"Rendering frame {frame}")

    result = subprocess.run([
        BLENDER,
        "-b",
        BLEND_FILE,
        "-f",
        str(frame)
    ])

    if result.returncode != 0:
        print(f"Failed on frame {frame}")
        break