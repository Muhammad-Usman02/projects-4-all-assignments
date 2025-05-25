# Planetary Weight Calculator

# Dictionary with gravity ratios relative to Earth
gravity = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Input from user
earth_weight = float(input("Enter a weight on Earth: "))
planet = input("Enter a planet: ")

# Calculate and round
if planet in gravity:
    planet_weight = round(earth_weight * gravity[planet], 2)
    print(f"The equivalent weight on {planet}: {planet_weight}")
else:
    print("Unknown planet. Please try again with a valid one.")
