from bad_jokes.joke_generator import JokeGenerator


def test_joke_gen():
    joke = JokeGenerator(model="JokeModelChicken", model_init_dict={"emotion": "happy"})
    assert len(joke.gen_jokes(n=3)) == 3, "Expected joke length does not match actual."
