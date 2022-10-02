import cohere

co = cohere.Client('j9fltyvpID3YyH82yoUqSCjhcydpMh1vG3lLS83z')

def cohere_generate(data):
    response = co.generate(prompt=data,
                           model='large',
                           preset=None,
                           num_generations=3,
                           max_tokens=250,
                           temperature=0.7,
                           k=0,
                           p=0.75,
                           frequency_penalty=0.0,
                           presence_penalty=0.0,
                           stop_sequences=None,
                           return_likelihoods='NONE',
                           truncate=None,
                           logit_bias={}
                           )

    for gen in response.generations:
        print('Prediction:\n\ttext = {}\n\tlikelihood = {}\n\ttoken_likelihoods = {}'.format(gen.text,
                                                                                             gen.likelihood,
                                                                                             gen.token_likelihoods))
    if len(response.generations) == 0:
        return ""
    else:
        return response.generations[0].text
