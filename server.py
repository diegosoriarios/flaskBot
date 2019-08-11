from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("HAL")
#bot.set_trainer(ListTrainer)
trainer = ChatterBotCorpusTrainer(bot)
#trainer.train(['What is your name?', 'My name is HAL'])
#trainer.train(['Who are you?', 'I am a bot' ])
#trainer.train(['Do created you?', 'Tony Stark', 'Diego Soria Rios', 'You?'])
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run()
