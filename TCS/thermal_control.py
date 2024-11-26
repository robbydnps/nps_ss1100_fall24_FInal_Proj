import random
import time

def process_temperature(input_temp):
    """Function that takes an input temperature and
    applies a function to move it towards equilibrium.
    It should return a single float as the output holding 
    the altered temperature"""
    pass # Delete this line and insert your code here!


################### DO NOT EDIT THIS PORTION #############################
def main():
    duration = 15      # Duration to feed signals in seconds
    temperature = random.randint(-30, 60)
    sequence = []
    i = 0
    while True:
        direction = random.choice([-1, 1])
        change = random.uniform(1, 3) * direction
        new_temperature = max(-30, min(60, temperature + change))
        print(f"New temperature received: {new_temperature:.2f}")
        temperature = process_temperature(new_temperature)     
        time.sleep(1)  # Wait for 1 second before the next signal
        sequence.append(temperature)
        i += 1
        if i > duration:
            print(sequence)
            exit()        
if __name__ == "__main__":
    main()
###########################################################################
