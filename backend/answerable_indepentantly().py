from openai import OpenAI

client = OpenAI()
#gets API key from system environment variables

def isSelfContained(question):
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "Determine if the following question is self contained, returning only True or False, explaining your answer"},
        {"role": "user", "content": f"Question:  {question}"},
      ],
      max_tokens = 60,
      temperature = 0
    )
    return response

question = "Explain why operating systems use scheduling. "

response = isSelfContained(question)
#response2 = isSelfContained2(question)

print (response.choices[0].message.content)
cost = (response.usage.prompt_tokens / 1000) * 0.0015 + (response.usage.completion_tokens / 1000) * 0.002
print (f"\nCost: ${cost}")

##print (response2.choices[0].message.content)
##cost = (response2.usage.prompt_tokens / 1000) * 0.0015 + (response2.usage.completion_tokens / 1000) * 0.002
##print (f"\nCost: ${cost}")
