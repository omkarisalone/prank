import os
import subprocess
import sys
import threading
import time

def print_skin_tool():
    """Print YE LE TERA SKIN TOOL🤣🖕🏻 repeatedly until audio ends"""
    while not audio_finished:
        print("YE LE TERA SKIN TOOL🤣🖕🏻")
        time.sleep(0.1)  # Adjust speed as needed

# Global flag to track audio status
audio_finished = False

def main():
    global audio_finished
    audio_file = "audio.mp3"
    
    # Check if audio file exists
    if not os.path.exists(audio_file):
        print(f"Error: Audio file '{audio_file}' not found!")
        sys.exit(1)
    
    # Start printing in a separate thread
    print_thread = threading.Thread(target=print_skin_tool)
    print_thread.daemon = True
    print_thread.start()
    
    try:
        # Play audio using mpv with all output suppressed
        process = subprocess.Popen([
            "mpv", 
            "--no-video", 
            "--quiet", 
            "--no-terminal", 
            "--no-msg-color",
            "--no-audio-display",
            audio_file
        ], 
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL)
        
        # Wait for the audio to finish
        process.wait()
        
    except subprocess.CalledProcessError:
        pass
    except FileNotFoundError:
        print("Error: mpv not found. Install with: pkg install mpv")
        sys.exit(1)
    finally:
        # Set flag to stop printing
        audio_finished = True

if __name__ == "__main__":
    main()
