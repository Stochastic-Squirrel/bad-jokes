"""
bad_jokes: joke_generator module
-------------------------------------------
This module contains classes responsible for generating jokes.
"""
from typing import List
class JokeGenerator:
    """
    This class generates a joke by calling underlying joke models and providing input where necessary.
    """
    def gen_jokes(self, n: int = 1) -> List[str]:
        jokes = [f"TEST JOKE:{i}" for i in range(n)]
        return jokes
