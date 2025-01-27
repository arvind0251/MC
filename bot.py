import pyautogui
import time

# Function to perform mining action
def auto_mine():
    # Adjust the coordinates based on your screen resolution and game window position
    mining_coordinates = (500, 500)  # Example coordinates for the mining action
    # Number of times to mine
    number_of_mines = 10

    for _ in range(number_of_mines):
        # Move the mouse to the mining coordinates
        pyautogui.moveTo(mining_coordinates)
        # Click to mine
        pyautogui.click()
        # Wait for a short duration to simulate realistic mining
        time.sleep(1)  # Adjust the sleep time as necessary

# Start the auto mining process
if __name__ == "__main__":
    print("Starting auto mining in 5 seconds...")
    time.sleep(5)  # Gives you time to switch to the game window
    auto_mine()
    print("Auto mining completed.")
