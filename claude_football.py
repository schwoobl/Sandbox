import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    #model="claude-sonnet-4-20250514",
    model="claude-3-haiku-20240307",
    max_tokens=2000,
    temperature=0,
    system="You are football trainer.",
    messages=[
        {
            "role": "user",
            "content": [{"type": "text", "text": "What is the best line-up for the German Bundesliga football team Bayer 04 Leverkusen in Season 2024/2025? Formulate your answer as html file."}],
        }
    ],
)
with open("football.html", "w", encoding="utf-8") as f:
    f.write(message.content[0].text)
