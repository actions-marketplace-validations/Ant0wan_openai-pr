#!/usr/bin/env python3
import os
import sys
import openai

stdin = input_str = sys.stdin.read()
data = "The following is the output of the command git diff. Can you create a pull request description from it?\n" + stdin

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=data,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
)

print(response.choices[0].text)
