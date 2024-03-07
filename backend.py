import random

def generate_shakespeare_quote():
    quotes = [
        "To be or not to be, that is the question.",
        "All the world's a stage, and all the men and women merely players.",
        "To thine own self be true.",
        "What's in a name? That which we call a rose by any other name would smell as sweet.",
        "The better part of Valour, is Discretion.",
        "This above all: to thine own self be true.",
        "Love all, trust a few, do wrong to none."
    ]

    return random.choice(quotes)

if __name__ == "__main__":
    shakespeare_quote = generate_shakespeare_quote()
    print("Shakespeare says:", shakespeare_quote)