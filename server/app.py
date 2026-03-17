from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route('/')
def index():
  
    return "Welcome to Flatiron Cars"

@app.route('/<model_name>')
def get_model(model_name):
    if model_name in existing_models:
    
        return f"Flatiron {model_name} is in our fleet!"
    else:

        return f"No models called {model_name} exists in our catalog"

if __name__ == '__main__':
    app.run(debug=True)
