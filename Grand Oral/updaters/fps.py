from p5 import millis

tick = 0
calculated_fps = 0

UPDATE_TIME = 1

def update():
    """Function that calculates the FPS of the current display."""
    global tick, calculated_fps
    
    current_millis = millis()
    if current_millis > tick:
        tick = current_millis + UPDATE_TIME * 1000
        print(f"FPS: {calculated_fps}")
        calculated_fps = 0
    
    calculated_fps += 1
