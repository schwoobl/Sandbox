import anthropic #vorher durch 'pip install' installieren

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    #model="claude-3-haiku-20240307",
    max_tokens=1000,
    temperature=1.0,
    system="You are a world-class poet. Respond only with short poems.",
    messages=[
        {
            "role": "user",
            "content": [{"type": "text", "text": "Why is the ocean salty?"}],
        }
    ],
)
print(message.content[0].text)

