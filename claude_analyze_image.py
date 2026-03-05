import anthropic
import os
import base64

def encode_image(image_path):
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_path = r'image2.jpg'
client = anthropic.Anthropic()
prompt = 'Who is portrayed on this picture?'

try:
    base64_image = encode_image(image_path)
    response = client.messages.create(
    #model="claude-3-haiku-20240307",
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    temperature=0,
    #system='You are an US political reporter.',
    messages=[
        {
            "role": "user",
            "content": [{"type": "image", "source": {
                "type": "base64",
                "media_type": "image/jpeg", "data": base64_image}
                         },
                        {
                            "type":"text",
                            "text": prompt

                            }
                        ]
        }
    ]
    )
    print(response.content[0].text)
except Exception as e:
    print(f"An error occured: {e}")


    
