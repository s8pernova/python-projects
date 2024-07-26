# Program to access songs from json file, ask the user which one they want, then put their choice(s) in a csv file
# A lot of the code that I used were from the links in the videos, and learning all of it is why I turned this assignment in kind of close to the deadline instead of way before, like I usually do
# I put a comment for each term that wasn't directly presented in the video to explain it

import time  # This module is purely for decorative purposes
import json

# Testing out typing in the current working directory (CWD)
file_input = "/home/achrunaway/Coding/Python/NOVA Python Course/File Reading/Python Liaison Program/songs.json"
file_output = "/home/achrunaway/Coding/Python/NOVA Python Course/File Reading/Python Liaison Program/playlist.csv"
global chosen_playlist  # global to make sure that I can call this variable ANYWHERE, even outside of this function
chosen_playlist = []

# Check if the field in a line is empty. If it is, then replace it with "???"
def get_field_value(fields, index):
    value = fields.get(index)
    return "???" if value is None or value == "" else value

def print_song_list():
    global counter
    # enumerate() to count each iteration in "songList", starting from 1. I learned about this from links and it saves unnecessary code like saying counter = 1 and then counter += 1 for each loop
    for counter, song in enumerate(list_of_songs, starting_value):
        # Avoiding boilerplate code by putting these variables in a function. The function will ALSO check if the value in the keys are empty
        title = get_field_value(song, "title")
        artist = get_field_value(song, "artist")
        year = get_field_value(song, "year")
        rating = get_field_value(song, "ratingOutOf10")

        # Testing out the escape character '\"'
        print(f"{counter}. \"{title}\" by {artist}\n",
            f"  Release Date: {year}\n",
            f"  Overall Rating: {rating}\n")  # Not very responsive design because of the two spaces (if the counter goes to double digits, it will move the top section to the right by one, but the bottom will stay the same), but it's ok because this is a small program
        time.sleep(0.1)  # Add a small time between songs to make it more obvious that the list is growing. Plus it looks nicer

# Print out the list of songs from the json file, then ask the user what songs they want in their playlist
def user_choice():
    # Print all of the songs 
    print("Here are the songs:\n")
    # Read and return the current list of songs from the json file. I found it easier to just combine it with the user_choice() function
    with open(file_input, "r") as file_ptr:  # "with" to automatically close the file when it's done. I learned this from the links in the videos
        global outer_dictionary  # I just made every variable here global because I was too lazy to make it work with print_song_list() otherwise
        outer_dictionary = json.load(file_ptr)
        global list_of_songs
        list_of_songs = outer_dictionary.get("songList")
        global starting_value
        starting_value = 1  # The value that will determine which number the enumerate function will start from

        print_song_list()

        done_choosing = False  # Setting a flag (used for the next while loop)
        
        # Ask the user which song they'd like to add to the playlist
        while not done_choosing:
            while True:
                user_input = input(f"Which song would you like to add to your playlist? [{starting_value}-{counter}]: ").lower()
                if user_input == "exit":  # This is just something I like to add while developing, so I can just say "exit" instead of terminating the code entirely
                    exit()
                elif user_input == "none" and len(chosen_playlist) == 0:  # Adding in a "none" option is so the user can cancel choosing a song ID
                    print("You need to have at least one song.", end = " ")
                elif user_input == "none":
                    print("Are you sure...?", end = " ")  # end = " " so it can connect seamlessly with the choose_again input
                    break
                # Added a try/except to catch the errors that would happen after I convert user_input into an int
                try:
                    chosen_num = int(user_input)  # The reason why I converted it to an int only now is so that the user would be able to type in "exit" and "none" (which are strings) without causing a ValueError
                    dict_of_chosen_song = list_of_songs[chosen_num - 1]  # Access the specific song via index

                    # Check if the current song is an ANY sublist for the final playlist thing. I learned about this online
                    if any(dict_of_chosen_song["title"] in sublist for sublist in chosen_playlist) and any(dict_of_chosen_song["artist"] in sublist for sublist in chosen_playlist):
                        print("That song is already in the playlist... Enter a new number. Or just type in \"none\".\n")
                    
                    # Make sure the user's input is within the range of songs in the json file
                    elif starting_value <= chosen_num <= counter:
                        # Save some code by appending all of them at the same time directly to the chosen playlist (basically)
                        chosen_playlist.append([
                            dict_of_chosen_song["title"],
                            dict_of_chosen_song["artist"],
                            dict_of_chosen_song["year"],
                            dict_of_chosen_song["ratingOutOf10"]
                        ])
                        print("Got it.", end = " ")
                        break
                    
                # Catch the error from entering anything BUT a number (or a number out of range)
                except (ValueError, IndexError):
                    print(f"Choose a number from {starting_value} to {counter}, dude. Try again.\n")

            # Ask user if they'd like to choose another song
            while True:
                choose_again = input("Would you like to choose another song? [Y/N]: ").lower()

                if choose_again == "n":
                    done_choosing = True
                    break
                elif choose_again == "y":
                    print()
                    print_song_list()
                    break
                elif choose_again == "exit":
                    exit()
                else:
                    print("Please choose either Y or N. Not... whatever you just said. Try again.\n")

    return chosen_playlist

# Bonus not in the videos: ask the user to give the playlist a name
def name_playlist():
    while True:
        global playlist_title
        playlist_title = input("\nWhat would you like to name your new playlist?: ")

        if playlist_title == "exit":
            exit()

        # while True loop to house the confirmation message
        while True:
            confirmation = input(f"Are you sure you'd like to name your playlist \"{playlist_title}\"? This cannot be undone. [Y/N]: ").lower()
            if confirmation == "y":
                return playlist_title
            elif confirmation == "n":
                print("Then choose another title. Stop wasting my time!!")
                break
            elif confirmation == "exit":
                exit()
            else:
                print("...Let's try that again.\n")

# Store the chosen playlist into the csv file
def send_csv_output():
    with open(file_output, "w") as file_ptr:
        # Write the title and headers
        file_ptr.write(f"{playlist_title}\n\nTitle,Artist,Year,Rating\n")
        for song in chosen_playlist:  # Instead of writing "two_d_list", I just chose to link this for loop directly to the chosen_playlist, which saves me from having to write the whole "title = chosen_playlist[0][0]" and "artist = chosen_playlist[0][1]" thing
            # I also found it more efficient to use the .join() method with the map() function because I learned that it can combine the iterables in a list and structure them in a way that csv files can understand (by putting commas in between each string)
            song_line = ",".join(map(str, song)) + "\n"  # ALSO also, the "map" coverts everything into a string, so I don't have to do it manually (saving even more code space)
            file_ptr.write(song_line)

# Print a friendly lil confirmation message that the playlist was successfully created
def confirmation_message():
    num_of_songs_chosen = len(chosen_playlist)

    # Change the word "song" to singular or plural depending on the amount of songs in the playlist
    if num_of_songs_chosen == 1:
        song = "song"
    else:
        song = "songs"
        
    print(f"\nConfirmed! Your new playlist titled \"{playlist_title}\" with {num_of_songs_chosen} {song} is now created!")
    
def main():
    chosen_playlist = user_choice()
    playlist_title = name_playlist()
    send_csv_output()
    confirmation_message()


# Make sure main() doesn't run if it's an imported file; I learned that it's good practice
if __name__ == "__main__":
    main()

# Just a quick reflection but this project took so long and at one point I wanted to break my computer because of how annoying it was but I'm still proud of it. I'm gonna go work on module 9 now