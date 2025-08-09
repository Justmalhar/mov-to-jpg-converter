import subprocess
import os

def video_to_images_ffmpeg(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    # %05d → zero-padded numbering (frame_00001.jpg, frame_00002.jpg, ...)
    command = [
        "ffmpeg",
        "-i", video_path,
        os.path.join(output_folder, "frame_%05d.jpg")
    ]
    subprocess.run(command, check=True)
    print(f"✅ Done! Frames saved to '{output_folder}'")

# Example usage:
video_to_images_ffmpeg("input_video.mov", "output_frames")