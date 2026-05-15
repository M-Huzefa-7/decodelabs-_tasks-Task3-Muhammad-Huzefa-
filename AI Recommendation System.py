# Recommendation data

recommendations = {
    "action": ["John Wick", "Avengers", "Mad Max"],
    "comedy": ["Mr. Bean", "Friends", "The Mask"],
    "horror": ["The Conjuring", "Insidious", "Annabelle"],
    "technology": ["AI Basics", "Python Guide", "Machine Learning"],
    "sports": ["Football Highlights", "Cricket World Cup", "Sports News"]
}

# Take user input
user_interest = input(
    "Enter your interest (action/comedy/horror/technology/sports): "
).lower()


# Match preferences using logic
if user_interest in recommendations:

    # Display recommended items
    print("\nRecommended Items:")

    for item in recommendations[user_interest]:
        print("-", item)

else:
    print("No recommendations found.")