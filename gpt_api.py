import openai

openai.api_key ="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"

def gpt_generate(data):
    response = openai.Completion.create(
           model="text-davinci-002",
            max_tokens = 250,
            top_p = 1.00,
            frequency_penalty = 0,
            presence_penalty = 0,
            prompt=data,
            temperature=0.7,
        )
    return response.choices[0].text
