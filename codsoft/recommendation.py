# Simple Movie and Book Recommendation System

# Our database of recommendations grouped by genres
recommendations = {
    "movies": {
        "action": ["Mad Max: Fury Road", "The Dark Knight", "Inception", "Gladiator"],
        "comedy": ["The Hangover", "Superbad", "Free Guy", "Home Alone"],
        "sci-fi": ["Interstellar", "The Matrix", "Blade Runner 2049", "Arrival"],
        "romance": ["The Notebook", "La La Land", "About Time", "Pride & Prejudice"],
        "horror": ["The Conjuring", "Get Out", "A Quiet Place", "It"]
    },
    "books": {
        "action": ["The Hunger Games by Suzanne Collins", "The Bourne Identity by Robert Ludlum"],
        "comedy": ["The Hitchhiker's Guide to the Galaxy by Douglas Adams", "Good Omens by Neil Gaiman"],
        "sci-fi": ["Dune by Frank Herbert", "Project Hail Mary by Andy Weir", "Neuromancer"],
        "romance": ["Me Before You by Jojo Moyes", "The Fault in Our Stars by John Green"],
        "horror": ["The Shining by Stephen King", "Dracula by Bram Stoker", "Bird Box"]
    }
}

print("=========================================")
print("   Welcome to your AI Recommendation System!   ")
print("=========================================\n")

while True:
    print("What would you like a recommendation for?")
    print("1. Movies")
    print("2. Books")
    print("3. Exit")
    
    choice = input("\nEnter choice (1/2/3): ").strip()
    
    if choice == "3":
        print("\nThank you for using the AI Recommendation System. Goodbye!")
        break
        
    if choice not in ["1", "2"]:
        print("\nInvalid choice! Please select 1, 2, or 3.\n")
        continue
        
    # Determine type based on choice
    item_type = "movies" if choice == "1" else "books"
    
    print(f"\nAvailable genres for {item_type}:")
    genres = list(recommendations[item_type].keys())
    for genre in genres:
        print(f"- {genre.capitalize()}")
        
    user_genre = input(f"\nType a genre from the list above: ").lower().strip()
    
    if user_genre in recommendations[item_type]:
        print(f"\n🤖 AI Recommendations for {user_genre.capitalize()} {item_type}:")
        print("-----------------------------------------")
        for item in recommendations[item_type][user_genre]:
            print(f"⭐ {item}")
        print("-----------------------------------------\n")
    else:
        print(f"\nSorry, we don't have recommendations for '{user_genre}' yet. Please try again!\n")
