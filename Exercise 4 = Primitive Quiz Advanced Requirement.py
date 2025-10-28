# European Capitals Quiz

# Dictionary of countries and their capitals
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Switzerland": "Bern",
    "Austria": "Vienna",
    "Norway": "Oslo"
}

# Keep track of the score
score = 0

print("Welcome to the European Capitals Quiz!")
print("Type your answers — capitalization doesn’t matter.\n")

# Loop through each country in the quiz
for country, capital in capitals.items():
    answer = input(f"What is the capital of {country}? ").strip()

    # Compare answers ignoring capitalization
    if answer.lower() == capital.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {capital}.\n")

# Display final score
print("Quiz complete!")
print(f"Your final score: {score} out of {len(capitals)}")
