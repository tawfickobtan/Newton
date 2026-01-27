from llm import complete
import tools
import json

# Load config file
config = {}
with open("config.json", "r") as f:
    config = json.load(f)

systemPrompt = ""
with open("system_prompt.txt", "r") as f:
    systemPrompt = f.read()


# Define function registry
functionRegistry = {
    "getItemsInPath": tools.getItemsInPath,
    "writeIntoFile": tools.writeIntoFile,
    "readFile": tools.readFile,
    "runPythonFile": tools.runPythonFile
}

# Initialise messages with system prompt
messages = [
    {"role": "system",
     "content": systemPrompt}
]

response = complete(messages)
messages.append(response)
print("James:")
print(response)
print("_________________")
print()

while True:
    print("User:")
    userInput = input()
    print("_________________")
    print()
    messages.append({
        "role": "user",
        "content": userInput
    })