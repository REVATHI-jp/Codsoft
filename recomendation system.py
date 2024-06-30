class SimpleRecommendationSystem:
    def __init__(self):
        self.users_preferences = {}  # Dictionary to store users' preferences
        self.items_similarity = {}   # Dictionary to store items' similarity scores

    def add_preference(self, user, item, score):
        if user not in self.users_preferences:
            self.users_preferences[user] = {}
        self.users_preferences[user][item] = score

    def calculate_similarity(self):
        # Calculate similarity between items based on users' preferences
        for user, preferences in self.users_preferences.items():
            for item1 in preferences:
                for item2 in preferences:
                    if item1 != item2:
                        if item1 not in self.items_similarity:
                            self.items_similarity[item1] = {}
                        if item2 not in self.items_similarity[item1]:
                            self.items_similarity[item1][item2] = 0
                        self.items_similarity[item1][item2] += 1

        # Normalize similarity scores
        for item1 in self.items_similarity:
            for item2 in self.items_similarity[item1]:
                self.items_similarity[item1][item2] /= len(self.users_preferences)

    def recommend_items(self, user, num_recommendations=3):
        # Recommend items to the user based on their preferences
        if user not in self.users_preferences:
            print(f"User '{user}' not found in preferences.")
            return []

        user_preferences = self.users_preferences[user]
        recommendations = {}

        for item1, score in user_preferences.items():
            for item2 in self.items_similarity.get(item1, {}):
                if item2 in user_preferences:
                    continue  # Skip items user already rated

                if item2 not in recommendations:
                    recommendations[item2] = 0
                recommendations[item2] += score * self.items_similarity[item1][item2]

        # Sort recommendations by score in descending order
        sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

        # Return top recommended items
        return [item for item, _ in sorted_recommendations[:num_recommendations]]


# Example usage:
if __name__ == "__main__":
    # Create an instance of the recommendation system
    recommender = SimpleRecommendationSystem()

    # Add user preferences (user, item, score)
    recommender.add_preference('User1', 'Movie1', 5)
    recommender.add_preference('User1', 'Movie2', 4)
    recommender.add_preference('User1', 'Movie3', 3)
    recommender.add_preference('User2', 'Movie1', 4)
    recommender.add_preference('User2', 'Movie2', 5)
    recommender.add_preference('User2', 'Movie3', 4)

    # Calculate item similarities based on users' preferences
    recommender.calculate_similarity()

    # Recommend items for a specific user
    user = 'User1'
    recommendations = recommender.recommend_items(user, num_recommendations=2)
    print(f"Recommendations for {user}: {recommendations}")
