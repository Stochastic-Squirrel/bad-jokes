from bad_jokes.joke_generator import JokeGenerator
def test_joke_gen():
    joke = JokeGenerator()
    assert len(joke.gen_jokes(3)) == 3, "Expected joke length does not match actual."
