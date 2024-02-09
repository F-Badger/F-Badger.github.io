from openai import OpenAI

client = OpenAI()
#gets API key from system environment variables

def isSelfContained(question):
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "This is one part of a multi-part question. \
    Determine if it requires knowledge of an element that can't be known from outside knowledge, such as referring to 'this', \
    'the {something}' or a 'figure' which is not explictly described in the question.\
    Return False if it does refer to an element of the question which is not given , \
    and True if it does not as the first part of your response.\
    Explain the decision very briefly."},
        {"role": "user", "content": f"Question:  {question}"},
      ],
      max_tokens = 60,
      temperature = 0
    )
    return response

##def isSelfContained2(question):
##    response = client.chat.completions.create(
##      model="gpt-3.5-turbo-1106",
##      messages=[
##        {"role": "system", "content": "This is one part of a multi-part question. \
##    Determine if it requires knowledge of an element that can't be known from outside knowledge, such as referring to 'this', \
##    'the {something}' or a 'figure' which is not explictly described in the question.\
##    Return False if it does refer to an element of the question which is not given , \
##    and True if it does not as the first part of your response.\
##    Explain the decision very briefly."},
##        {"role": "user", "content": f"Question:  {question}"},
##      ],
##      max_tokens = 60,
##      temperature = 0
##    )
##    return response

question = "Identify three inputs that will be required to configure the initial conditions for running the simulation."

response = isSelfContained(question)
#response2 = isSelfContained2(question)

print (response.choices[0].message.content)
cost = (response.usage.prompt_tokens / 1000) * 0.0015 + (response.usage.completion_tokens / 1000) * 0.002
print (f"\nCost: ${cost}")

##print (response2.choices[0].message.content)
##cost = (response2.usage.prompt_tokens / 1000) * 0.0015 + (response2.usage.completion_tokens / 1000) * 0.002
##print (f"\nCost: ${cost}")
