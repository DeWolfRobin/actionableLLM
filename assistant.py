# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

userprompt = "What is the current number one song by adelle?"

completion = client.chat.completions.create(
  model="local-model", # this field is currently unused
  messages=[
    {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful. Upon receiving a message, you will sort them into either one of these categories: 'Actionable' if it is a message that expects you to perform an action, or 'Non-actionable' if the message does not include an action that you need to perform. In case of a 'Non-actionable' message, you will respond normally. In front of every response, you will add the category of the message, for example: 'Non-actionable: You are welcome'"},
    {"role": "user", "content": userprompt}
  ],
  temperature=0.7,
)
firstResponse = completion.choices[0].message.content

if "Non-actionable" in firstResponse:
    print(firstResponse.replace("Non-actionable: ",""))
else:
    print("I will: ", firstResponse.replace("Actionable: ",""))
    completion = client.chat.completions.create(
        model="local-model", # this field is currently unused
        messages=[
            {"role": "system", "content": "You are a smart home assistant who can extract actions from a message. you will give an answer that disects the user prompt and shows the sentence structure. For example: when the user says: 'turn on the lights.', you will reply: 'Action: Turn on, what: the lights'"},
            {"role": "user", "content": userprompt}
        ],
        temperature=0.7,
    )
    print(completion.choices[0].message.content)
