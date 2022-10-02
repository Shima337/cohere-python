import cohere

co = cohere.Client('j9fltyvpID3YyH82yoUqSCjhcydpMh1vG3lLS83z')

def cohere_generate(data):
    response = co.generate(prompt=data)

    for gen in response.generations:
        print('Prediction:\n\ttext = {}\n\tlikelihood = {}\n\ttoken_likelihoods = {}'.format(gen.text,
                                                                                             gen.likelihood,
                                                                                             gen.token_likelihoods))
    if len(response.generations) == 0:
        return ""
    else:
        return response.generations[0].text
