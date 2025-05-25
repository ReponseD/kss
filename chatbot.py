from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('KSSBot')

# Training the chatbot with a corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')  # You can add custom datasets later

# A simple function to get responses
def get_bot_response(user_input):
    return chatbot.get_response(user_input)
