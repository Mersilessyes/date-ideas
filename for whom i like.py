import random
import sys
from bs4 import BeautifulSoup
import requests
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import time

current_menu_level = 0
back_command = "b"

def display_heart():
    heart = '''
     /\  /\ 
    /  \/  \\
    \      /
     \    /
      \  /
       \/
    '''
    print(heart)
    
def choose_specific_dutch_bros_drink():
    # Add your code here to allow the user to choose a specific Dutch Bros drink
    print("Enter the name of your preferred Dutch Bros drink.")
    drink_choice = input("Your choice: ")
    return drink_choice


def display_categories():
    global current_menu_level
    current_menu_level = 1
    
    categories = ["Outdoor Dates", "Indoor Dates", "ASCII"]
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

def choose_outdoor_date_option():
    global current_menu_level
    current_menu_level = 2

    while True:
        outdoor_choice = int(input("\nSelect an option for the outdoor date:\n"
                                   "1. Romantic Walk\n"
                                   "2. Picnic\n"
                                   "3. Spa Day/Night\n"
                                   "4. Amusement Park\n"
                                   "5. Shopping\n"
                                   "6. Dutch Bros\n"
                                   "7. Random Outdoor Date Idea\n"
                                   "0. Back\n"))

        if outdoor_choice == 1:
            print("\nGreat choice! A romantic walk sounds lovely.")
            sys.exit()
        elif outdoor_choice == 2:
            print("\nGreat, have fun <3")
            sys.exit()
        elif outdoor_choice == 3:
            print("\nSpa Day/Night option selected")
            choose_spa_budget()
            sys.exit()
        elif outdoor_choice == 4:
            amusement_park = choose_amusement_park()
            print(f"\nEnjoy your time at the {amusement_park} amusement park!")
            sys.exit()
        elif outdoor_choice == 5:
            choose_shopping_destination()
            sys.exit()
        elif outdoor_choice == 6:
            dutch_bros_choice = choose_dutch_bros_drink()
            print(f"\nEnjoy your Dutch Bros {dutch_bros_choice}!")
            sys.exit()
        elif outdoor_choice == 7:
            random_outdoor_date()
            sys.exit()
        elif outdoor_choice == 0:
            break
        else:
            print(f"\nInvalid option. Please select a valid option.")


def random_outdoor_date():
    outdoor_date_ideas = [
        "Walk",
        "Picnic",
        "Spa Day/Night",
        "Amusement Park",
        "Shopping",
        "Dutch Bros",
        # Add more outdoor date ideas here if desired
    ]

    chosen_idea = random.choice(outdoor_date_ideas)
    print(f"\nYour randomly chosen outdoor date idea is: {chosen_idea}")

    if chosen_idea == "Walk":
        print("\nGreat choice! A romantic walk sounds lovely.")
        sys.exit()
    elif chosen_idea == "Picnic":
        print("\nGreat, have fun <3")
        sys.exit()
    elif chosen_idea == "Spa Day/Night":
        choose_spa_budget()
        sys.exit()
    elif chosen_idea == "Amusement Park":
        amusement_park = choose_amusement_park()
        print(f"\nEnjoy your time at the {amusement_park} amusement park!")
        sys.exit()
    elif chosen_idea == "Shopping":
        choose_shopping_destination()
        sys.exit()
    elif chosen_idea == "Dutch Bros":
        dutch_bros_choice = choose_dutch_bros_drink()
        print(f"\nEnjoy your Dutch Bros {dutch_bros_choice}!")
    else:
        # Handle other outdoor date ideas if needed
        sys.exit()
#https://open.spotify.com/track/0T3pyPYtHAsxIRymAZsTkX?si=0121e16d337a46e2
def choose_sleep_date():
    print("\nSleep Date option selected")
    print("Grab some fuzzy blankets and pillows and sleep well <3")

def choose_indoor_date_option():
    global current_menu_level
    current_menu_level = 3

    while True:
        indoor_choice = int(input("\nSelect an option for the indoor date:\n"
                                  "1. Movie Night\n"
                                  "2. Gaming\n"
                                  "3. Balloon Animals\n"
                                  "4. Cook Together\n"
                                  "5. Indoor Picnic\n"
                                  "6. Arts\n"
                                  "7. Sleep Date\n"
                                  "8. Just Cuddle\n"
                                  "9. Random Indoor Date\n"
                                  "0. Back\n"))

        if indoor_choice == 1:
            movie_genre = choose_movie_genre()
            print(f"\nLets watch {movie_genre} cuddles too? <3")
            sys.exit()  # Auto-exit the program after finalizing the date idea
        elif indoor_choice == 2:
            gaming_option = choose_gaming_option()
            print(f"\nLets honestly get this bread in {gaming_option}!")
            sys.exit()  # Auto-exit the program after finalizing the date idea
        elif indoor_choice == 3:
            balloon_animal = choose_balloon_animal()
            print(f"\nLets make a {balloon_animal}")
            sys.exit()  # Auto-exit the program after finalizing the date idea
            break
        elif indoor_choice == 4:
            print("\nCook Together option selected")
            print("Try making one of these random dishes y'all:")
            print("https://www.cosmopolitan.com/food-cocktails/a5567/romantic-dinner/")
            sys.exit()
            break
        elif indoor_choice == 5:
            print("\nIndoor Picnic option selected")
            sys.exit()
            break
        elif indoor_choice == 6:
            print("\nArts option selected")
            print("Let us make one of these:")
            print("https://gritandgraceful.com/15-crafts-for-couples/")
            sys.exit()
            break
        elif indoor_choice == 7:
            choose_sleep_date()
            sys.exit()
            break
        elif indoor_choice == 8:
            print("\nCuddles And Chill?")
            sys.exit()
            break
        elif indoor_choice == 9:
            random_indoor_date()
            sys.exit()
            break
        elif indoor_choice == 0:
            break
        else:
            print(f"\nInvalid option. Please select a valid option.")   

def random_indoor_date():
    indoor_dates = [
        "Movie Night",
        "Gaming",
        "Balloon Animals",
        "Cook Together",
        "Indoor Picnic",
        "Arts",
        "Sleep Date",
        "Just Cuddle"
    ]
    random_date = random.choice(indoor_dates)

    print(f"\nYour randomly chosen indoor date is: {random_date}")

    if random_date == "Movie Night":
        choose_movie_genre()
    elif random_date == "Gaming":
        choose_gaming_option()
    elif random_date == "Balloon Animals":
        choose_balloon_animal()
    elif random_date == "Cook Together":
        print("\nCook Together option selected")
        print("For a romantic dinner, consider trying this recipe:")
        print("https://www.cosmopolitan.com/food-cocktails/a5567/romantic-dinner/")
    elif random_date == "Indoor Picnic":
        print("\nGrab something from the cook together option or think of something random, have fun")
    elif random_date == "Arts":
        print("\nArts option selected")
        print("Lets make something together")
        print("https://gritandgraceful.com/15-crafts-for-couples/")
    elif random_date == "Sleep Date":
        choose_sleep_date()
    elif random_date == "Just Cuddle":
        print("\nCuddles and Chill")

def choose_shopping_destination():
    global current_menu_level
    current_menu_level = 3
    
    while True:
        shopping_options = ["Walmart", "Target", "Aldis", "Mall"]
        print("\nShopping Options:")
        for i, option in enumerate(shopping_options, 1):
            print(f"{i}. {option}")

        choice = int(input("\nSelect an option for shopping:\n"
                           "1. Let the code pick\n"
                           "2. Choose yourself\n"
                           "0. Back\n"))

        if choice == 1:
            selected_shop = random.choice(shopping_options)
        elif choice == 2:
            selected_option = int(input("\nEnter the number corresponding to your choice: "))
            if 1 <= selected_option <= len(shopping_options):
                selected_shop = shopping_options[selected_option - 1]
            else:
                print("Invalid option. The code will pick for you.")
                selected_shop = random.choice(shopping_options)
        elif choice == 0:
            break
        else:
            print("Invalid choice. The code will pick for you.")
            selected_shop = random.choice(shopping_options)

        if selected_shop == "Mall":
            choose_mall_location()
        else:
            budget_option = input("\nSelect an option for the shopping budget:\n"
                                  "1. Choose a budget\n"
                                  "2. Generate a random budget\n"
                                  "0. Back\n")

            if budget_option == "1":
                budget = float(input("Enter your desired budget for shopping: $"))
                if 100 <= budget <= 500:
                    print(f"\nEnjoy your shopping at {selected_shop} with a budget of ${budget:.2f}!")
                    break
                else:
                    print("Invalid budget. The code will generate a random budget for you.")
                    generate_random_shopping_budget(selected_shop)
            elif budget_option == "2":
                generate_random_shopping_budget(selected_shop)
                break
            elif budget_option == "0":
                break
            else:
                print("Invalid choice. The code will generate a random budget for you.")
                generate_random_shopping_budget(selected_shop)

def generate_random_shopping_budget(selected_shop):
    random_budget = random.randint(100, 500)
    print(f"\nYour random shopping budget at {selected_shop} is: ${random_budget}")
    print(f"Enjoy your shopping at {selected_shop} with a budget of ${random_budget:.2f}!")

def choose_mall_location():
    mall_locations = ["Arizona Center", "The Promenade", "Scottsdale Fashion"]
    print("\nMall Locations:")
    for i, location in enumerate(mall_locations, 1):
        print(f"{i}. {location}")

    location_option = input("\nSelect an option for the mall location:\n"
                            "1. Try something random\n"
                            "2. Choose your own\n")

    if location_option == "1":
        selected_location = random.choice(mall_locations)
    elif location_option == "2":
        selected_option = int(input("\nEnter the number corresponding to your choice: "))
        if 1 <= selected_option <= len(mall_locations):
            selected_location = mall_locations[selected_option - 1]
        else:
            print("Invalid option. The code will pick for you.")
            selected_location = random.choice(mall_locations)
    else:
        print("Invalid choice. The code will pick for you.")
        selected_location = random.choice(mall_locations)

    print(f"\nYou selected the mall location: {selected_location}")

    budget_option = input("\nSelect an option for the shopping budget:\n"
                          "1. Choose a budget\n"
                          "2. Generate a random budget\n"
                          "0. Back\n")

    if budget_option == "1":
        budget = float(input("Enter your desired budget for shopping: $"))
        if 100 <= budget <= 500:
            print(f"\nEnjoy your shopping at {selected_location} with a budget of ${budget:.2f}!")
        else:
            print("Invalid budget. The code will generate a random budget for you.")
            generate_random_shopping_budget(selected_location)
    elif budget_option == "2":
        generate_random_shopping_budget(selected_location)
    elif budget_option == "0":
        choose_shopping_destination()
    else:
        print("Invalid choice. The code will generate a random budget for you.")
        generate_random_shopping_budget(selected_location)

def choose_spa_budget():
    global current_menu_level
    current_menu_level = 4
    
    while True:
        spa_budget_option = input("\nSelect an option for the Spa Day/Night budget:\n"
                                  "1. Choose a budget\n"
                                  "2. Generate a random budget\n"
                                  "0. Back\n")

        if spa_budget_option == "1":
            budget = float(input("Enter your desired budget for the Spa Day/Night: $"))
            if 100 <= budget <= 500:
                print(f"\nLets live comfortably with a wallet breaking ${budget:.2f}!")
                break
            else:
                print("Invalid budget. The code will generate a random budget for you.")
                generate_random_spa_budget()
        elif spa_budget_option == "2":
            generate_random_spa_budget()
            break
        elif spa_budget_option == "0":
            break
        else:
            print("Invalid choice. The code will generate a random budget for you.")
            generate_random_spa_budget()

def generate_random_spa_budget():
    random_budget = random.randint(100, 500)
    print(f"\nI hope you're ready to spend ${random_budget}")
    print(f"Lets live comfortably and break the wallet with a riveting budget of ${random_budget:.2f}!")

def choose_balloon_animal():
    global current_menu_level
    current_menu_level = 5
    
    while True:
        balloon_animals = ["Dog", "Cat", "Elephant", "Sword", "Flower"]
        print("\nBalloon Animal Options:")
        for i, animal in enumerate(balloon_animals, 1):
            print(f"{i}. {animal}")

        choice = int(input("\nSelect an option for the balloon animal:\n"
                           "1. Let the code pick\n"
                           "2. Choose yourself\n"
                           "0. Back\n"))

        if choice == 1:
            chosen_animal = random.choice(balloon_animals)
        elif choice == 2:
            selected_option = int(input("\nEnter the number corresponding to your choice: "))
            if 1 <= selected_option <= len(balloon_animals):
                chosen_animal = balloon_animals[selected_option - 1]
            else:
                print("Invalid option. The code will pick for you.")
                chosen_animal = random.choice(balloon_animals)
        elif choice == 0:
            break
        else:
            print("Invalid choice. The code will pick for you.")
            chosen_animal = random.choice(balloon_animals)

        if chosen_animal == "Dog":
            print("Here's a YouTube link to learn how to make a balloon dog:")
            print("https://www.youtube.com/watch?v=nmVEjx1DCqk&pp=ygUUZG9nIGJhbGxvb24gdHV0b3JpYWw%3D")
        elif chosen_animal == "Cat":
            print("Here's a YouTube link to learn how to make a balloon cat:")
            print("https://www.youtube.com/watch?v=WbxxmcbeLO8&pp=ygUUY2F0IGJhbGxvb24gdHV0b3JpYWw%3D")
        elif chosen_animal == "Elephant":
            print("Here's a YouTube link to learn how to make a balloon elephant:")
            print("https://www.youtube.com/watch?v=ztr-1a_e8cY&pp=ygUXZWxlcGhhbnQgYmFsbG9vbiBhbmltYWw%3D")
        elif chosen_animal == "Sword":
            print("Here's a YouTube link to learn how to make a balloon sword:")
            print("https://www.youtube.com/watch?v=j1PI6KJ79bg&pp=ygUUc3dvcmQgYmFsbG9vbiBhbmltYWw%3D")
        elif chosen_animal == "Flower":
            print("Here's a YouTube link to learn how to make a balloon flower:")
            print("https://www.youtube.com/watch?v=fIQchMKeP0w&pp=ygUVZmxvd2VyIGJhbGxvb24gYW5pbWFs")
        else:
            print("Invalid choice. Please select a valid option.")
            return choose_balloon_animal()

        break
def choose_amusement_park():
    amusement_park_options = ["Castles", "Enchanted", "Hurricane"]
    print("\nAmusement Park Options:")
    for i, option in enumerate(amusement_park_options, 1):
        print(f"{i}. {option}")
    print("0. Back")

    choice = int(input("\nSelect an option for the amusement park:\n"
                       "1. Let the code pick\n"
                       "2. Choose yourself\n"
                       "0. Back\n"))

    if choice == 1:
        return random.choice(amusement_park_options)
    elif choice == 2:
        selected_option = int(input("\nEnter the number corresponding to your choice: "))
        if 1 <= selected_option <= len(amusement_park_options):
            return amusement_park_options[selected_option - 1]
        else:
            print("Invalid option. The code will pick for you.")
            return random.choice(amusement_park_options)
    elif choice == 0:
        return  # Go back to the previous menu
    else:
        print("Invalid choice. The code will pick for you.")
        return random.choice(amusement_park_options)

def choose_dutch_bros_drink():
    dutch_bros_options = ["Random Drink", "Choose Your Own"]
    print("\nDutch Bros Drink Options:")
    for i, option in enumerate(dutch_bros_options, 1):
        print(f"{i}. {option}")
    print("0. Back")

    choice = int(input("\nSelect an option for Dutch Bros:\n"
                       "1. Try something random\n"
                       "2. Choose your own\n"
                       "0. Back\n"))

    if choice == 1:
        # Add more Dutch Bros drink options here if desired
        return "Random Drink"
    elif choice == 2:
        drink_choice = input("\nEnter your Dutch Bros drink choice: ")
        return drink_choice
    elif choice == 0:
        return  # Go back to the previous menu
    else:
        print("Invalid choice. The code will pick a random drink.")
        # Add more Dutch Bros drink options here if desired
        return "Random Drink"

def choose_movie_genre():
    movie_genres = ["Comedy", "Action", "Romance", "Disney"]
    print("\nMovie Genres:")
    for i, genre in enumerate(movie_genres, 1):
        print(f"{i}. {genre}")
    print("0. Back")

    genre_choice = int(input("\nSelect a genre for the movie night:\n"
                             "1. Back\n"))

    if genre_choice == 4:
        return choose_disney_movie()
    elif 1 <= genre_choice <= 3:
        # Add more options for other genres here if desired
        return movie_genres[genre_choice - 1]
    elif genre_choice == 0:
        return  # Go back to the previous menu
    else:
        print("Invalid choice. The code will pick a random genre.")
        # Add more options for other genres here if desired
        return random.choice(movie_genres)


def choose_disney_movie():
    disney_movies = ["Random Movie", "Choose Your Own"]
    print("\nDisney Movie Options:")
    for i, option in enumerate(disney_movies, 1):
        print(f"{i}. {option}")

    choice = int(input("\nSelect an option for Disney movies:\n"
                       "1. Let the code pick\n"
                       "2. Choose yourself\n"))

    if choice == 1:
        movie_options = ["Lady and the Tramp", "Beauty and the Beast", "Nemo", "Frozen", "Aladdin", "Little Mermaid"]
        return random.choice(movie_options)
    elif choice == 2:
        movie_options = ["Lady and the Tramp", "Beauty and the Beast", "Nemo", "Frozen", "Aladdin", "Little Mermaid"]
        print("\nDisney Movie Options:")
        for i, movie in enumerate(movie_options, 1):
            print(f"{i}. {movie}")

        movie_choice = int(input("\nSelect an option for the Disney movie:\n"
                                 "1. Let the code pick\n"
                                 "2. Choose yourself\n"))

        if movie_choice == 1:
            return random.choice(movie_options)
        elif movie_choice == 2:
            selected_movie_option = int(input("\nEnter the number corresponding to your choice: "))
            if 1 <= selected_movie_option <= len(movie_options):
                return movie_options[selected_movie_option - 1]
            else:
                print("Invalid option. The code will pick for you.")
                return random.choice(movie_options)
        else:
            print("Invalid choice. The code will pick for you.")
            return random.choice(movie_options)

def choose_gaming_option():
    gaming_options = ["Random Game", "Choose Your Own"]
    print("\nGaming Options:")
    for i, option in enumerate(gaming_options, 1):
        print(f"{i}. {option}")

    choice = input("\nSelect an option for gaming:\n"
                   "1. Try something random\n"
                   "2. Choose your own\n")

    if choice == "1":
        game = random.choice(["Roblox", "Minecraft", "Valorant"])
        return choose_game_option(game)
    elif choice == "2":
        game_options = ["Roblox", "Minecraft", "Valorant"]
        print("\nGame Options:")
        for i, game in enumerate(game_options, 1):
            print(f"{i}. {game}")

        game_choice = int(input("\nSelect an option for the game:\n"
                                "1. Roblox\n"
                                "2. Minecraft\n"
                                "3. Valorant\n"))

        if game_choice == 1:
            return choose_roblox_game()
        elif game_choice == 2:
            return choose_minecraft_mode()
        elif game_choice == 3:
            return choose_valorant_mode()
        else:
            print("Invalid choice. The code will pick for you.")
            return random.choice(["Roblox", "Minecraft", "Valorant"])
    else:
        print("Invalid choice. The code will pick for you.")
        return random.choice(["Roblox", "Minecraft", "Valorant"])

def choose_game_option(game):
    if game == "Roblox":
        return choose_roblox_game()
    elif game == "Minecraft":
        return choose_minecraft_mode()
    elif game == "Valorant":
        return choose_valorant_mode()
    else:
        print("Invalid game. The code will pick a random game for you.")
        return random.choice(["Roblox", "Minecraft", "Valorant"])

def choose_roblox_game():
    roblox_options = ["Combat Warriors", "A Scary Game"]
    print("\nRoblox Game Options:")
    for i, game in enumerate(roblox_options, 1):
        print(f"{i}. {game}")

    choice = int(input("\nSelect an option for Roblox games:\n"
                       "1. Let the code pick\n"
                       "2. Choose yourself\n"))

    if choice == 1:
        return random.choice(roblox_options)
    elif choice == 2:
        selected_game_option = int(input("\nEnter the number corresponding to your choice: "))
        if 1 <= selected_game_option <= len(roblox_options):
            return roblox_options[selected_game_option - 1]
        else:
            print("Invalid option. The code will pick for you.")
            return random.choice(roblox_options)
    else:
        print("Invalid choice. The code will pick for you.")
        return random.choice(roblox_options)

def choose_minecraft_mode():
    minecraft_modes = ["Creative", "Survival"]
    print("\nMinecraft Mode Options:")
    for i, mode in enumerate(minecraft_modes, 1):
        print(f"{i}. {mode}")

    mode_choice = int(input("\nSelect an option for the Minecraft mode: "))

    if 1 <= mode_choice <= len(minecraft_modes):
        return minecraft_modes[mode_choice - 1]
    else:
        print("Invalid choice. The code will pick a random mode.")
        return random.choice(minecraft_modes)

def choose_valorant_mode():
    valorant_modes = ["Unrated", "Swiftplay", "Spike Rush"]
    print("\nValorant Mode Options:")
    for i, mode in enumerate(valorant_modes, 1):
        print(f"{i}. {mode}")

    mode_choice = input("\nSelect an option for the Valorant mode:\n"
                        "1. Try something random\n"
                        "2. Choose your own\n")

    if mode_choice == "1":
        return random.choice(valorant_modes)
    elif mode_choice == "2":
        selected_mode_option = int(input("\nEnter the number corresponding to your choice: "))
        if 1 <= selected_mode_option <= len(valorant_modes):
            return valorant_modes[selected_mode_option - 1]
        else:
            print("Invalid option. The code will pick for you.")
            return random.choice(valorant_modes)
    else:
        print("Invalid choice. The code will pick for you.")
        return random.choice(valorant_modes)

def choose_ascii_art():
    ascii_options = ["Heart", "Dog", "Cat"]
    print("\nASCII Art Options:")
    for i, art in enumerate(ascii_options, 1):
        print(f"{i}. {art}")

    art_choice = int(input("\nSelect an option for ASCII art:\n"
                           "1. Heart\n"
                           "2. Dog\n"
                           "3. Cat\n"))

    if 1 <= art_choice <= len(ascii_options):
        chosen_art = ascii_options[art_choice - 1]
        print(f"\nHere's your chosen ASCII art of a {chosen_art}:")
        if chosen_art == "Heart":
            print('''
           /\  /\ 
          /  \/  \\
          \      /
           \    /
            \  /
             \/
        ''')
        elif chosen_art == "Dog":
            print('''
         / \\__
        (    @\___
         /         O
       /   (_____/
     /_____/   U
        ''')
        elif chosen_art == "Cat":
            print('''
         /\_/\  
        ( o.o ) 
         > ^ <
        ''')
        sys.exit()  # Auto-exit the program after displaying the ASCII art
    else:
        print("Invalid choice. Please select a valid option.")
        return choose_ascii_art()

import sys

def delay_and_exit():
    print("Final date decision made. Closing in 10 seconds...")
    time.sleep(10)
    sys.exit()

def main():
    print("Welcome to the experimental date ideas project\n")
    display_heart()

    while True:
        print("Select a category:")
        display_categories()

        choice = input(f"\nType the number corresponding to your choice or '{back_command}' to go back: ")

        if choice == back_command:
            if current_menu_level == 1:
                break
            elif current_menu_level == 2:
                continue
            elif current_menu_level == 3:
                choose_outdoor_date_option()
            elif current_menu_level == 4:
                choose_shopping_destination()
            elif current_menu_level == 5:
                choose_spa_budget()
            else:
                print("Invalid menu level.")
                break
        elif choice == "1":
            print("\nYou selected: Outdoor Dates")
            choose_outdoor_date_option()
        elif choice == "2":
            print("\nYou selected: Indoor Dates")
            choose_indoor_date_option()
        elif choice == "3":
            choose_ascii_art()
        else:
            print("\nInvalid choice. Please select a valid category.")
    
    # Add a delay before exiting the application
    delay_and_exit()

if __name__ == "__main__":
    main()
