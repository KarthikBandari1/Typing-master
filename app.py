import random
import time
import json

def update_leaderboard(username, wpm):
    leaderboard = load_leaderboard()
    
    leaderboard.append({"username": username, "wpm": wpm})
    leaderboard = sorted(leaderboard, key=lambda x: x["wpm"], reverse=True)
    
    with open("leaderboard.json", "w") as file:
        json.dump(leaderboard, file, indent=2)

def load_leaderboard():
    try:
        with open("leaderboard.json", "r") as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = []
    
    return leaderboard

def show_leaderboard():
    leaderboard = load_leaderboard()
    print("------------------------------------------------------")
    print("Leaderboard: \n")
    for entry in leaderboard:
        print(f"{entry['username']}: {entry['wpm']} WPM")

def load_words_from_json(category):
    with open(f"{category}.json", "r") as file:
        words = json.load(file)
    
    random.shuffle(words)
    return words

def get_user_input():
    print("\n")
    return input("\nType the words: ")

def main():
    print("Welcome to Terminal Typing Master!")

    while True:
        username = input("\nEnter your username: ")

        print("\nMenu:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            category = input("Choose a category : \n1. General \n2.Programming \n3.Movies \n4.Fashion \n")
            if category=="1":
                words = load_words_from_json("general")
            elif category=="2":
                words = load_words_from_json("programming")
            elif category=="3":
                words = load_words_from_json("movies")
            elif category=="4":
                words = load_words_from_json("fashion")
            
            start_time = time.time()
            
            print('\n')
            for word in words:
                print(word, end=" ")
            
            user_input = get_user_input()
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            correct_words = sum(1 for word in user_input.split() if word in words)
            accuracy = (correct_words / len(user_input.split())) * 100
            words_per_minute = len(user_input.split()) / (elapsed_time / 60)
            print("------------------------------------------------------")
            print("Result:")
            print(f"\nYour WPM: {words_per_minute:.2f}")
            print("Total words entered:",len(user_input.split()))
            print("Correct words Entered:",correct_words)
            print("Wrong words Entered:",len(user_input.split())-correct_words)
            print(f"Accuracy: {accuracy:.2f}%")
            print("Time taken: ", elapsed_time)
            
            update_leaderboard(username, words_per_minute)
            show_leaderboard()

        elif choice == "2":
            show_leaderboard()

        elif choice == "3":
            print("Exiting the Typing Test. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

