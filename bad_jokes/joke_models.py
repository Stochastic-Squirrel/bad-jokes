"""
bad_jokes: joke_models module
---------------------------------------------
This module contains all of the text generation models that will be used in JokeGenerator type classes.
"""
from abc import abstractmethod


class JokeModel:
    """Base class for all Joke Models.

    Each Joke model may require context and/or any init parameters
    """

    @abstractmethod
    def create_joke(self, **kwargs) -> str:
        """
        Args:
            **kwargs: any keyword arguments that assists derived classes to produce a joke.
        Returns:
            A string describing a hilariously bad joke.
        """


class JokeModelChicken(JokeModel):

    """Generates the classic: Why did the chicken cross the road? format. Users
    can specify an emotion to affect the nature of the punchline.

    TODO:
        * Fetch a list of lame self-help advice and categorise them into broad emotions
        * create a way to store model information for recall
    """

    _base_chicken_joke = f"Why did the chicken cross the road?"
    _punchlines = {"happy": "Because the little chicken shaped light was green"}

    def __init__(self, emotion: str = "happy"):
        self.emotion = emotion

    def create_joke(self, **kwargs) -> str:
        punchline = JokeModelChicken._punchlines.get(self.emotion, "No Jokes here :(")
        return " ".join([JokeModelChicken._base_chicken_joke, punchline])
