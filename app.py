from taipy.gui import Gui
import pickle

model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

message = ""
result = ""

def detect(state):

    msg_vec = vectorizer.transform([state.message])
    prediction = model.predict(msg_vec)[0]

    if prediction == "spam":
        state.result = "🚨 SPAM MESSAGE"
    else:
        state.result = "✅ NOT SPAM"

page = """
# 📧 Email Spam Detection System

### Enter Message
<|{message}|input|>

<|Detect Spam|button|on_action=detect|>

## Result

### <|{result}|>
"""

Gui(page).run()