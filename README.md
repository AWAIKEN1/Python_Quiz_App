<h1>Basic Quiz App</h1>

<h2>Overview</h2>
<p>This Basic Quiz App is a Python application designed to demonstrate fundamental Python programming skills and the use of JSON for data storage. It reads a series of quiz questions from a JSON file and prints each question's text. Ideal for beginners, the project illustrates basic data handling in Python, JSON parsing, and control structures.</p>

<h2>Features</h2>
<ul>
  <li><strong>JSON Data Handling:</strong> Demonstrates how to read and parse data from a JSON file in Python.</li>
  <li><strong>Control Flow:</strong> Utilizes loops for iterating over data structures.</li>
  <li><strong>Data Structures:</strong> Shows how to access data within lists and dictionaries.</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Python 3.10</li>
</ul>

<h2>Installation and Setup</h2>
<ol>
  <li><strong>Clone the Repository:</strong><br>
  <code>git clone https://github.com/AWAIKEN1/Python_Quiz_App.git</code><br>
  Alternatively, download the ZIP file from the GitHub repository.</li>
  <li><strong>Navigate to the Directory:</strong><br>
  Open your terminal and change to the directory containing the project.</li>
  <li><strong>Ensure the JSON File is Present:</strong><br>
  Verify that <code>questions.json</code> is in the same directory as your Python script.</li>
</ol>

<h2>Usage</h2>
<p>Run the Program:</p>
<p>Execute <code>python quiz_app.py</code> in the terminal (ensure to replace <code>quiz_app.py</code> with your Python script's filename).</p>
<p>Interact with the Quiz:</p>
<p>The program will display each question from the JSON file. Currently, it is set up for displaying questions only. Interactive answering functionality can be added in future versions.</p>

<h2>JSON File Format</h2>
<p>The quiz data should be in <code>questions.json</code> with this format:</p>
<pre><code>[
    {
        "question_text": "Sample Question?",
        "alternatives": ["Option1", "Option2", "Option3"],
        "correct_answer": 1
    },
    ...
]</code></pre>
<ul>
  <li><code>question_text</code> is a string containing the question.</li>
  <li><code>alternatives</code> is a list of answer options.</li>
  <li><code>correct_answer</code> is the index (starting from 1) of the correct answer in the alternatives list.</li>
</ul>

<h2>Future Enhancements</h2>
<ul>
  <li>User Interaction: Implement functionality for users to select an answer and receive feedback.</li>
  <li>Scoring System: Keep track of the user's score throughout the quiz.</li>
  <li>Time Limit: Add a time limit for each question.</li>
</ul>

<h2>Contribution</h2>
<p>Feel free to fork the project and enhance its features. Your contributions are highly appreciated.</p>
