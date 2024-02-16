from openai import OpenAI

client = OpenAI()
#gets API key from system environment variables

def isSelfContained(question):
    response = client.chat.completions.create(
      model="ft:gpt-3.5-turbo-1106:personal::8sjXfJaw",
      messages=[
        {"role": "system", "content": "Determine if the following question can be answered fully without additional clarifications"},
        {"role": "user", "content": f"Question:  {question}"},
      ],
      max_tokens = 1,
      temperature = 0,
    )
    return response

question = "Describe what is meant by recursion"

response = isSelfContained(question)

print (response.choices[0].message.content)
cost = (response.usage.prompt_tokens / 1000) * 0.003 + (response.usage.completion_tokens / 1000) * 0.006
print (f"\nCost: ${cost}")
