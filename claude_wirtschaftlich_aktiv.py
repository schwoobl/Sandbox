import anthropic
import os
import csv

client = anthropic.Anthropic()

in_string = input('Press any button to start: ')

counter = -1
with open('Unbestimmt.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        counter += 1
        if counter == 0:
            continue
        name = row[3]
        address = row[4]
        print(counter)
        print(name + " " + address)
        prompt = "For the given company (with name and address) tell us " 
        prompt+= "if the company is still existing and operating. Show instances of "
        prompt+= "live signs on a timeline and give us a confidence interval with sources.\n"
        
        prompt += "Is the company \""+name+ "\" in "+address+" economically active?"
        prompt += "Answer in yes or no and low or high for confidence. "
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            #model="claude-3-haiku-20240307",
            max_tokens=1000,
            messages=[
                {
            "role": "user",
            "content": prompt
                }
            ]
        )
        print(message.content)
        break #for Demo, to avoid compute all examples 
