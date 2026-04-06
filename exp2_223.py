import random
import re
def simple_chatbot():
 """A basic chatbot using fundamental Python concepts."""
 
responses = {
 "hello": ["Hi there!", "Hello!", "Greetings!"],
 "hi": ["Hi there!", "Hello!", "Greetings!"],
 "how are you": ["I'm a bot, I'm doing great!", "I'm functioning optimally."],
 "what is your name": ["You can call me PyBot.", "I don't have a name, but I respond to 'Hey you!'"],
 "bye": ["Goodbye!", "See you later!", "Have a great day!"],
 "exit": ["Goodbye!", "See you later!", "Have a great day!"]
 }
 
default_responses = [
 "Sorry, I didn't understand that.",
 "Could you please rephrase that?",
 "I'm not sure how to respond to that."
 ]
print("PyBot: Hi! I'm a simple chatbot. Type 'bye' or 'exit' to end the conversation.")
 
while True:
    user_input = input("You: ").lower() 
    user_input = re.sub(r'[^\w\s]', '', user_input)
 
    if user_input in ["bye", "exit"]:
        print(f"PyBot: {random.choice(responses[user_input])}")
    break 
matched = False
for key in responses:
 
    if key in user_input:
 
        bot_response = random.choice(responses[key])
        print(f"PyBot: {bot_response}")
        matched = True
    break 
if not matched:
    print(f"PyBot: {random.choice(default_responses)}")

if __name__ == "__main__":
 simple_chatbot()