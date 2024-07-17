# Program to access song inputs from json, ask user if they want to add more, then put that in a csv file

import json
import csv

file_input = "/home/achrunaway/Coding/Python/NOVA Python Course/File Reading/Python Liaison Program/songs.json" # Testing out how to type in the full file directory
file_output = "outputted_songs.csv"

# Read and return the current list of songs from the json file
def receive_json_input():
    # "with" to auto close file when it's done (from the links in the videos)
    with open(file_input, "r") as file_ptr:
        outer_dictionary = json.load(file_ptr)
        list_of_songs = outer_dictionary.get("songlist")
    print(f"The data type of the songs is called {type(list_of_songs)}.\n\nThe songs themselves are:\n{list_of_songs}")
    return list_of_songs

# Ask user what song title they want to put in the list: who made it, when it was made, and what they'd rate it 1-10
def user_choice():
    while True:
        pass

# Store that input into the csv file
def send_csv_output():
    with open(file_output, "w") as file_ptr:
        pass

def main():
    receive_json_input()
    user_choice()
    send_csv_output()


# Make sure main() doesn't run if it's an imported file
if __name__ == "__main__":
    main()