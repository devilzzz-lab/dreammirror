<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <h1>🌙 DreamMirror AI</h1>
  <p>DreamMirror AI is an interactive project that takes your dream description, analyzes it using NLP, and generates surreal dream visuals using Stable Diffusion with Apple Silicon MPS acceleration.</p>

  <h2>🤝 Contributing & Branch Rules</h2>
  <table border="1">
    <tr>
      <th>Branch Name</th>
      <th>Purpose</th>
      <th>Who Can Push</th>
    </tr>
    <tr>
      <td><b>main</b></td>
      <td>Production-ready code (<b>protected</b>)</td>
      <td>🔐 Only Devil (lead)</td>
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
      <pre>git checkout srimathi  # Example: use your assigned branch name</pre>
    </li>
    <li>
      <b>Pull latest main (optional, for sync)</b>
      <pre>git pull origin main</pre>
    </li>
    <li>
      <b>Make your changes</b>
      <pre>git add .
git commit -m "Your commit message"
git push origin srimathi</pre>
    </li>
    <li>
      <b>Request merge</b><br>
      Open a Pull Request from your branch to main. Only Devil (admin) can approve and merge.
    </li>
  </ol>

  <h2>🔒 Main Branch Protection</h2>
  <p>Direct pushes to main are blocked for everyone except Devil.<br>
  All updates to main must go through Pull Requests.<br>
  This keeps main stable and production-ready.</p>

  <h2>🛠 Installation Guide</h2>
  <ol>
    <li>
      <b>Create & Activate Virtual Environment</b>
      <pre>python3 -m venv venv
source venv/bin/activate       # Mac / Linux
venv\Scripts\activate          # Windows</pre>
    </li>
    <li>
      <b>Install Requirements</b>
      <pre>pip install -r requirements.txt</pre>
    </li>
    <li>
      <b>Download Required Data</b>
      <pre>python -m spacy download en_core_web_sm
python -m textblob.download_corpora
python -m nltk.downloader vader_lexicon</pre>
    </li>
  </ol>

  <h2>🚀 Running DreamMirror AI</h2>
  <p>Run the interactive dream analysis + image generation pipeline:</p>
  <pre>python app/full_dream_pipeline.py</pre>
  <p>The program will:</p>
  <ul>
    <li>Ask you to describe your dream.</li>
    <li>Analyze the text for keywords, emotions, and themes.</li>
    <li>Generate a Stable Diffusion prompt.</li>
    <li>Create AI dream visuals in <b>data/</b> folder.</li>
  </ul>

  <h3>📌 Example Output</h3>
  <pre>🌙 Welcome to DreamMirror AI 🌌
📝 Describe your dream: I was flying over glowing cities at night.

🔍 Analyzing your dream...
🪄 Generating visual prompt...
✨ Prompt: A surreal dream scene with cities, where someone is flying. Atmospheric lighting, soft surreal colors, mystical tone.

🎨 Generating images...
✅ Saved: data/generated_dream_1.png
✅ Saved: data/generated_dream_2.png
✅ Saved: data/generated_dream_3.png
</pre>

  <h2>✅ Best Practices for Team</h2>
  <ul>
    <li>Always work in your assigned branch.</li>
    <li>Never push directly to main.</li>
    <li>Keep commits small and meaningful.</li>
    <li>Sync with main before starting new work.</li>
    <li>Use pull requests for all merges.</li>
  </ul>

  <p>💡 Let's turn dreams into reality — together! ✨</p>
</body>
</html>
