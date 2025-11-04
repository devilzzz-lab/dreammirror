<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

  <h1>🌙 DreamMirror AI</h1>
  <p>DreamMirror AI is an interactive NLP and AI image generation system that takes your dream description, analyzes it for emotion and meaning, and generates surreal dream visuals using <b>Stable Diffusion (v1.5)</b> with Apple Silicon <b>MPS acceleration</b>.</p>

  <h2>🤝 Contributing & Branch Rules</h2>
  <table border="1" cellpadding="5" cellspacing="0">
    <tr>
      <th>Branch Name</th>
      <th>Purpose</th>
      <th>Who Can Push</th>
    </tr>
    <tr>
      <td><b>main</b></td>
      <td>Production-ready and stable code (<b>protected</b>)</td>
      <td>🔐 Only Devil (Lead)</td>
    </tr>
    <tr>
      <td><b>srimathi</b></td>
      <td>Personal branch for Srimathi</td>
      <td>✅ Srimathi only</td>
    </tr>
    <tr>
      <td><b>saran</b></td>
      <td>Personal branch for Saran</td>
      <td>✅ Saran only</td>
    </tr>
    <tr>
      <td><b>swetha</b></td>
      <td>Personal branch for Swetha</td>
      <td>✅ Swetha only</td>
    </tr>
  </table>

  <h2>🧑‍💻 Contribution Workflow</h2>
  <ol>
    <li>
      <b>Clone the repository</b>
      <pre>git clone https://github.com/devilzzz-lab/dreammirror.git
cd dreammirror</pre>
    </li>
    <li>
      <b>Checkout your personal branch</b>
      <pre>git checkout srimathi   # Example: use your assigned branch name</pre>
    </li>
    <li>
      <b>Sync with latest main (recommended before edits)</b>
      <pre>git pull origin main</pre>
    </li>
    <li>
      <b>Make and push your changes</b>
      <pre>git add .
git commit -m "Updated dream analysis module"
git push origin srimathi</pre>
    </li>
    <li>
      <b>Create Pull Request</b><br>
      Open a PR from your branch → <b>main</b>.<br>
      Only Devil (admin) can review and merge.
    </li>
  </ol>

  <h2>🔒 Main Branch Protection</h2>
  <p>The <b>main</b> branch is locked to prevent direct edits.<br>
  All updates go through Pull Requests for code review and stability.</p>

  <h2>🛠 Backend Installation & Setup</h2>
  <ol>
    <li>
      <b>Create and activate virtual environment</b>
      <pre>
cd dreammirror
python3 -m venv venv
source venv/bin/activate       # (Mac / Linux)
venv\Scripts\activate          # (Windows)
      </pre>
    </li>
    <li>
      <b>Install dependencies</b>
      <pre>
pip install --upgrade pip
pip install -r requirements.txt
      </pre>
    </li>
    <li>
      <b>Download spaCy English model</b>
      <pre>python -m spacy download en_core_web_sm</pre>
    </li>
    <li>
      <b>Set Hugging Face local cache directory</b>
      <pre>export HF_HOME=~/sd_models</pre>
    </li>
  </ol>

  <h2>🚀 Run Backend Server</h2>
  <pre>
# Make sure you're inside the virtual environment
cd dreammirror
source venv/bin/activate

# Start backend (FastAPI + Uvicorn)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
  </pre>

  <h3>📌 Example Output</h3>
  <pre>
🌙 Welcome to DreamMirror AI 🌌
📝 Describe your dream: I was walking through glowing forests under a violet sky.

🔍 Analyzing dream emotions...
🪄 NLP Processing Complete.
✨ Generated Prompt:
A surreal dream landscape of glowing forests and violet skies, mystical ambiance, emotional tone: calm and wonder.

🎨 Generating visuals using Stable Diffusion (MPS accelerated)...
✅ Saved: app/dream_outputs/generated_dream_1.png
✅ Saved: app/dream_outputs/generated_dream_2.png
✅ Saved: app/dream_outputs/generated_dream_3.png
  </pre>

  <h2>🎨 Frontend Setup (React)</h2>
  <ol>
    <li>
      <b>Navigate to frontend folder</b>
      <pre>cd dreammirror-frontend</pre>
    </li>
    <li>
      <b>Install dependencies</b>
      <pre>npm install</pre>
    </li>
    <li>
      <b>Run the development server</b>
      <pre>npm start</pre>
    </li>
    <li>
      <b>Access the app in browser</b>
      <pre>http://localhost:3000</pre>
    </li>
  </ol>

  <h2>✅ Team Collaboration Best Practices</h2>
  <ul>
    <li>Never push directly to <b>main</b>.</li>
    <li>Work only in your assigned personal branch.</li>
    <li>Pull latest <b>main</b> before starting new work.</li>
    <li>Keep commits clear and descriptive.</li>
    <li>Test backend (FastAPI) and frontend (React) before pushing.</li>
  </ul>

  <h3>To sync your local copy with main</h3>
  <pre>
git checkout main
git pull origin main
  </pre>

  <p>💡 Together, we turn dreams into AI-powered reality! ✨</p>

</body>
</html>
