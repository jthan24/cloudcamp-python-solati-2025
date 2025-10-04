from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for votes (replace with a database for persistence)
votes = {
    'Option A': 0,
    'Option B': 0,
    'Option C': 0
}

@app.route('/')
def index():
    """Renders the main voting page."""
    return render_template('index.html', votes=votes)

@app.route('/vote', methods=['POST'])
def vote():
    """Processes a vote submission."""
    selected_option = request.form.get('option')
    if selected_option in votes:
        votes[selected_option] += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
