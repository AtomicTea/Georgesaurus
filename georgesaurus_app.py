#main code

def get_euphemism(word):
    matches = df[df["word"] == word]
    if len(matches) > 0:
        return random.choice(matches["euphemism"].tolist())
    else:
        return "We don't know. Ask her!"

# --- Function to find the closest word using fuzzy matching ---
def find_closest_word(input_word, word_list, threshold=80):
    best_match = process.extractOne(input_word, word_list)
    # check if we got a match
    if best_match is None:
        return None
        
    closest_word,score,_ = best_match
    if score >= threshold:
         return closest_word
    else:
        return None

# --- Main smart euphemism function ---
def get_smart_euphemism(word):
    if not word:
        return "We don't know. Ask her!"
    if word in words:
        return get_euphemism(word)
  
    closest_word = find_closest_word(word, words)
    if closest_word is not None:
        return get_euphemism(closest_word)
    else:
        return "We don't know. Ask her!"


# --- Route ---
@route("/")
def home():
    return '''
    <html>
    <head>
        <title>The Georgie Decoder</title>
               <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                background: #f4f7fb;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .card {
                background: white;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                text-align: center;
                width: 400px;
            }

            h1 {
                margin-bottom: 10px;
                margin-right: 25px;
                color: #333;
            }

            p {
                color: #777;
                margin-bottom: 30px;
            }

            input[type="text"] {
                width: 70%;
                padding: 12px;
                border-radius: 12px;
                border: 1px solid #ddd;
                font-size: 1em;
            }

            button {
                padding: 12px 18px;
                border-radius: 12px;
                border: none;
                background: #6c9cff;
                color: white;
                font-size: 1em;
                cursor: pointer;
                margin-left: 10px;
            }

            button:hover {
                background: #4f7fe0;
            }
        </style>
    </head>
        <body>
        
            <h1>The Georgie Decoder </h1>
        <div class="card">
            <p>In human history, great thinkers like Erasmus, Shakespeare, Abraham Lincoln and Chuck D have all
            used the English language to express deep emotion.</p> 
            
            <p>But none of these wordsmiths has utilized the English language as powerfully and provocatively
            as George Mason.</p> <p>Herein lies her genius. Discover it.</p><br>
        
            <form action="/result" method="post">
                <input name="word" type="text" placeholder="Try 'airport'..." />
                <button type="submit">Translate</button>
            </form>
        </div>
        </body>
     </html>
    '''

@route("/result", method="POST")
def result():
    word = request.forms.get("word")
    result = get_smart_euphemism(word)
    return f''' 
    <html>
    <head>
        <style>
              body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                background: #f4f7fb;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}

            .card {{
                background: white;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                text-align: center;
                width: 400px;
            }}

            .input-word {{
                color: #888;
                margin-bottom: 10px;
            }}

            .result {{
                font-size: 2em;
                color: #6c9cff;
                margin: 20px 0;
            }}

            a {{
                display: inline-block;
                margin-top: 20px;
                text-decoration: none;
                background: #6c9cff;
                color: white;
                padding: 10px 20px;
                border-radius: 12px;
            }}

            a:hover {{
                background: #4f7fe0;
            }}
        </style>
    </head>
    <body>
         <div class="card">
            <div class="input-word">You said: <strong>{word}</strong></div>
        <h2>Georgie thinks that word is: <div class="result">“{result}”</div></h2>
        <a href="/">Try another one!</a>
    </body>
    </html>
    '''


# --- Run app ---
run(host="localhost", port=8080, debug=True)
