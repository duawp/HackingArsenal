import sys
import time

def processing_animation(duration=5):
    animation = "|/-\\"
    idx = 0
    
    print("Processing", end="")
    start_time = time.time()
    
    while time.time() - start_time < duration:
        print(f"\rProcessing {animation[idx % len(animation)]}", end="")
        idx += 1
        time.sleep(0.1)
    
    print("\rProcessing complete!")

# Run the animation for 5 seconds
processing_animation(3.5)
