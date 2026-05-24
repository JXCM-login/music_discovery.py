from ai import call_gpt

def main():
    library = []
    print("=======================================")
    print("       AI MUSIC DISCOVERY 1.0    ")
    print("   Your Personalized Virtual DJ Console  ")
    print("=======================================")
    print("Loading systems... Ready.")

    while True:
        choice = input("\n[D]iscover, [A]dd, [V]iew, or [Q]uit: ").lower()
        if choice == "d":
            print("")
    # 3. If they chose 'Discover', get the 3 inputs 
            mood = input("Enter a mood: ")
            topic = input("Enter a topic: ")
            genre = input("Enter a genre: ")
            # 4. Make the AI call

            retries = 0

            while True:
                prompt = (f"suggest {mood} {genre} 1 song that already exists, no more than 20 words, do not say anythign more than the songs about {topic}. This is attempt number {retries}, so make sure it is a different song than before.")

                print("\nBaking your song... 🍳")
                recommendation = call_gpt(prompt)

                print(f"\nAi suggest {recommendation}")

                like_it = input("Do you like this recommendation? (Y)es to save / (N)o to try another: ").lower().strip()
                    
                if like_it == 'y':
                    library.append(recommendation)
                    print("\nSuccessfully added to your library!")
                    break 
                
                elif like_it == 'n':
                    print("\nLet's try that again! Changing the record...")
                    retries += 1    
                        
                else:
                    print("Invalid choice, let's try again.")

                library.append(recommendation) 
                print("Successfully added to your library!")
                print("")
        elif choice == 'a':
            song = input("Enter song name to add manually: ")
            library.append(song)
            print("Added!")

        elif choice == 'v':
            print("--- Your Music Library ---")
            if len(library) == 0:
                print("Your library is currently empty. Try 'Discover' to add something!")
            # Loop through the list to see everything
            for song in library:
                print("- " + song)

        elif choice == 'q':
            print("Enjoy the music...")
            break # Exit the loop 

        #change the d, v, a 
        #more intuitive
        # add formating 


if __name__ == "__main__":
    main()
