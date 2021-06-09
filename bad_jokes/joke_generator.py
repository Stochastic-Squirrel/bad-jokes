"""
bad_jokes: joke_generator module
-------------------------------------------
This module contains classes responsible for generating jokes.
"""
from typing import TYPE_CHECKING, Any, Dict, List, Optional
from bad_jokes.joke_models import JokeModelChicken

if TYPE_CHECKING:
    from bad_jokes.joke_models import JokeModel


class JokeGenerator:
    """This class generates a joke by calling underlying joke models and
    providing input where necessary.

    Attributes:
        model_obj: Instance of class JokeModel
    """

    def __init__(self, model: str, model_init_dict: Optional[Dict[Any, Any]]):
        """
        Args:
            model: JokeModel class string name
            model_init_dict: Dictionary with init args for JokeModel
        """
        try:
            self.model_obj: JokeModel = eval(model)(**model_init_dict)
        except Exception as e:
            print(e)

    def gen_jokes(
        self, joke_context: Optional[Dict[Any, Any]] = None, n: int = 1
    ) -> List[str]:
        """
        Args:
            joke_context: Joke generation arguments passed to JokeModel.create_joke()
            n: Defaults to 1. Number of jokes to generate.
        Returns:
            * A list of jokes as strings of length n.
        """
        if joke_context is None:
            joke_context = {}
        try:
            jokes = [self.model_obj.create_joke(**joke_context) for i in range(n)]
            return jokes
        except Exception as e:
            raise Exception(e)


if __name__ == "__main__":
    x = JokeGenerator(model="JokeModelChicken", model_init_dict={"emotion": "happy"})
    print(x.gen_jokes(n=1))
