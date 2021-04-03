"""
bad_jokes: joke_generator module
-------------------------------------------
This module contains classes responsible for generating jokes.
"""

class JokeGenerator:
    """
    This class generates a joke by calling underlying joke models and providing input where necessary.
    """
    def gen_jokes(self, n: int = 1):
        for i in range(n):
            print(f"TEST JOKE:{i}")


