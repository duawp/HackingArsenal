import sys
import time

def processing_animation(duration=5):
    animation = "|/-\\"
    idx = 0
    
    print("Scanning", end="")
    start_time = time.time()
    
    while time.time() - start_time < duration:
        print(f"\rScanning {animation[idx % len(animation)]}", end="")
        idx += 1
        time.sleep(0.1)
    
    print("\rScanning in Progress please wait :D")

# Run the animation for 5 seconds
processing_animation(4)
