from openai import OpenAI

client = OpenAI()
#gets API key from system environment variables

def isSelfContained(question):
    response = client.chat.completions.create(
      model="ft:gpt-3.5-turbo-1106:personal::8sjXfJaw",
      messages=[
        {"role": "system", "content": "Determine if the following question is self-contained, explaining your response in one sentance."},
        {"role": "user", "content": f"Question:  {question}"},
      ],
      max_tokens = 60,
      temperature = 0
    )
    return response

question = "Identify three inputs that will be required to configure the initial conditions for running the simulation."

response = isSelfContained(question)

print (response.choices[0].message.content)
cost = (response.usage.prompt_tokens / 1000) * 0.0015 + (response.usage.completion_tokens / 1000) * 0.002
print (f"\nCost: ${cost}")
