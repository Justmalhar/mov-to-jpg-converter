# 🎥 Any Video to JPEG Converter

A simple Python utility to **convert any video (MOV, MP4, AVI, etc.) into JPEG frames** using [FFmpeg](https://ffmpeg.org/).

## ✨ Features
- Works with **MOV, MP4, AVI, MKV**, and more
- **Lossless frame extraction** — no quality degradation
- **Zero-padded filenames** for easy sorting (`frame_00001.jpg`, `frame_00002.jpg`, …)
- Extremely **fast** (uses FFmpeg directly, not Python decoding)

---

## 📦 Installation

1. **Install FFmpeg** (required)
   - **macOS**:  
     ```bash
     brew install ffmpeg
     ```
   - **Ubuntu/Debian**:  
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```
   - **Windows**:  
     [Download FFmpeg](https://ffmpeg.org/download.html) and add it to your PATH.

2. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/video-to-images.git
   cd video-to-images
   ```

3. **(Optional)** Create a Python virtual environment for isolation
   - Create the environment:
     ```bash
     python3 -m venv venv
     ```
   - Activate the environment:
     - **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```
     - **Windows (Command Prompt)**:
       ```cmd
       venv\Scripts\activate
       ```
     - **Windows (PowerShell)**:
       ```powershell
       venv\Scripts\Activate.ps1
       ```
   - Install any Python dependencies (in this case, no external packages are required since we use built-in modules `os` and `subprocess`).

---

## 🚀 Usage

1. Copy video file as input_video.mov in the folder
2. Run in Terminal
  ```
  python3 main.py
  ```
3. Optional you can also add a video with different filename by editing `main.py` and change `output` directory
```python
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
```

---

## 📂 Output Structure
After running, you'll have:

```
output_frames/
├── frame_00001.jpg
├── frame_00002.jpg
├── frame_00003.jpg
...
```

---

## ⚡ Tips
- Change `%05d` in the output filename to `%04d` or `%06d` to adjust zero-padding length.
- You can skip frames with FFmpeg by adding `-vf "select=not(mod(n\,5))"` to save every 5th frame.
- Works perfectly for **ProRes MOV** files without transcoding.

---

## 📜 License
MIT License — free to use and modify.
