from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# Sample data for demonstration purposes
sample_data = {"message": "No new messages"}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data')
def get_data():
    # Simulating a long-running process (e.g., checking for new data)
    time.sleep(5)

    # Check for new data (for demonstration, always returning the sample data)
    # In a real-world scenario, this check would involve monitoring for actual changes in data
    return jsonify(sample_data)


if __name__ == '__main__':
    app.run(debug=True)

