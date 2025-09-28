import random

print("=" * 60)
print("COMPLETE GUIDE TO PYTHON RANDOM MODULE FUNCTIONS")
print("=" * 60)

# =============================================================================
# BASIC RANDOM FUNCTIONS
# =============================================================================

print("\n1. BASIC RANDOM FUNCTIONS")
print("-" * 30)

# random() - Returns a random float between 0.0 and 1.0
print(f"random(): {random.random()}")

# uniform(a, b) - Returns a random float between a and b
print(f"uniform(1.5, 3.5): {random.uniform(1.5, 3.5)}")

# randint(a, b) - Returns a random integer between a and b (inclusive)
print(f"randint(1, 10): {random.randint(1, 10)}")

# randrange(start, stop, step) - Random element from range
print(f"randrange(1, 10, 2): {random.randrange(1, 10, 2)}")

# getrandbits(k) - Returns an integer with k random bits
print(f"getrandbits(8): {random.getrandbits(8)}")

# =============================================================================
# SEQUENCE FUNCTIONS
# =============================================================================

print("\n2. SEQUENCE FUNCTIONS")
print("-" * 30)

# choice(seq) - Random element from sequence
friends = ["John", "Jane", "Jim", "Jill", "Jack"]
print(f"choice from friends: {random.choice(friends)}")

# choices(population, weights=None, k=1) - Multiple choices with replacement
colors = ["red", "blue", "green", "yellow"]
print(f"choices with weights: {random.choices(colors, weights=[10, 1, 1, 1], k=5)}")

# sample(population, k) - k unique elements without replacement
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"sample of 3 unique: {random.sample(numbers, 3)}")

# shuffle(x) - Shuffles sequence in place
cards = ["Ace", "King", "Queen", "Jack"]
random.shuffle(cards)
print(f"shuffled cards: {cards}")

# =============================================================================
# SEED AND STATE FUNCTIONS
# =============================================================================

print("\n3. SEED AND STATE FUNCTIONS")
print("-" * 30)

# seed(a=None) - Initialize random number generator
random.seed(42)
print(f"After seed(42): {random.random()}")
random.seed(42)
print(f"Same seed again: {random.random()}")  # Same result

# getstate() and setstate() - Save and restore generator state
state = random.getstate()
random.random()  # Generate a number
random.setstate(state)  # Restore state
print(f"After state restore: {random.random()}")  # Same as before

# =============================================================================
# STATISTICAL DISTRIBUTIONS
# =============================================================================

print("\n4. STATISTICAL DISTRIBUTIONS")
print("-" * 30)

# triangular(low, high, mode) - Triangular distribution
print(f"triangular(1, 10, 5): {random.triangular(1, 10, 5)}")

# normalvariate(mu, sigma) - Normal distribution
print(f"normalvariate(0, 1): {random.normalvariate(0, 1)}")

# gauss(mu, sigma) - Gaussian distribution (same as normalvariate)
print(f"gauss(0, 1): {random.gauss(0, 1)}")

# uniform(a, b) - Uniform distribution (already shown above)
print(f"uniform(0, 10): {random.uniform(0, 10)}")

# =============================================================================
# ADVANCED DISTRIBUTIONS
# =============================================================================

print("\n5. ADVANCED DISTRIBUTIONS")
print("-" * 30)

# betavariate(alpha, beta) - Beta distribution
print(f"betavariate(2.5, 3.5): {random.betavariate(2.5, 3.5)}")

# expovariate(lambd) - Exponential distribution
print(f"expovariate(1/5): {random.expovariate(1/5)}")

# gammavariate(alpha, beta) - Gamma distribution
print(f"gammavariate(2, 2): {random.gammavariate(2, 2)}")

# lognormvariate(mu, sigma) - Log-normal distribution
print(f"lognormvariate(0, 1): {random.lognormvariate(0, 1)}")

# vonmisesvariate(mu, kappa) - von Mises distribution
print(f"vonmisesvariate(0, 4): {random.vonmisesvariate(0, 4)}")

# paretovariate(alpha) - Pareto distribution
print(f"paretovariate(2.5): {random.paretovariate(2.5)}")

# weibullvariate(alpha, beta) - Weibull distribution
print(f"weibullvariate(1, 1.5): {random.weibullvariate(1, 1.5)}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("\n6. PRACTICAL EXAMPLES")
print("-" * 30)

# Dice rolling
dice_roll = random.randint(1, 6)
print(f"Dice roll: {dice_roll}")

# Random password generator
import string
password_chars = string.ascii_letters + string.digits + "!@#$%"
password = ''.join(random.choices(password_chars, k=8))
print(f"Random password: {password}")

# Random color picker
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]
print(f"Random color: {random.choice(colors)}")

# Random lottery numbers (6 unique numbers from 1-49)
lottery_numbers = sorted(random.sample(range(1, 50), 6))
print(f"Lottery numbers: {lottery_numbers}")

# Random coin flip
coin = random.choice(["Heads", "Tails"])
print(f"Coin flip: {coin}")

# Random card from deck
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
card = f"{random.choice(ranks)} of {random.choice(suits)}"
print(f"Random card: {card}")

# Random temperature (normal distribution, mean=20, std=5)
temp = random.normalvariate(20, 5)
print(f"Random temperature: {temp:.1f}°C")

print("\n" + "=" * 60)
print("END OF RANDOM MODULE EXAMPLES")
print("=" * 60)

