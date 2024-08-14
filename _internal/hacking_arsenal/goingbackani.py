import sys
import time

def processing_animation(duration=5):
    animation = "|/-\\"
    idx = 0
    
    print("Exiting", end="")
    start_time = time.time()
    
    while time.time() - start_time < duration:
        print(f"\rExiting {animation[idx % len(animation)]}", end="")
        idx += 1
        time.sleep(0.1)
    
    print("\rProcessing complete!")

processing_animation(3)
