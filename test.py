from conversation import *

conversation = []

# Test append_message
append_message(conversation, "user", "What is my name?")
append_message(conversation, "model", "Your name is Braa.")

print("Conversation:")
print(conversation)

# Test save_conversation
save_conversation(conversation)

# Test load_conversation
loaded_conversation = load_conversation()

print("\nLoaded Conversation:")
print(loaded_conversation)

# Test get_recent_conversation
recent = get_recent_conversation(loaded_conversation, limit=1)

print("\nRecent Conversation:")
print(recent)