<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>DreamMirror AI</title>
</head>
<body>

  <h1>🌙 DreamMirror AI</h1>
  <p>DreamMirror AI is an interactive project that takes your dream description, analyzes it using NLP, and generates surreal dream visuals using Stable Diffusion with Apple Silicon MPS acceleration.</p>

  <h2>🤝 Contributing & Branch Rules</h2>
  <table border="1" cellpadding="5" cellspacing="0">
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
  <p>Direct pushes to <b>main</b> are blocked for everyone except Devil.<br>
  All updates to main must go through Pull Requests.<br>
  This keeps main stable and production-ready.</p>

  <h2>🛠 Installation & Run</h2>
  <ol>
    <li>
      <b>Create & Activate Virtual Environment</b>
      <pre>python3 -m venv venv
source venv/bin/activate       # Mac / Linux
venv\Scripts\activate          # Windows</pre>
    </li>
    <li>
      <b>Install dependencies and download spaCy model</b>
      <pre>pip install numpy pillow spacy textblob nltk torch torchvision torchaudio diffusers transformers accelerate safetensors tqdm opencv-python && python3 -m spacy download en_core_web_sm</pre>
    </li>
  </ol>

  <h2>🚀 Run DreamMirror AI</h2>
  <pre>python3 -m app.full_dream_pipeline</pre>

  <h3>📌 Example Output</h3>
  <pre>
🌙 Welcome to DreamMirror AI 🌌
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
    <li>Main branch is closed (protected); never push directly to <b>main</b>.</li>
    <li>Always check if <b>main</b> has updates before starting work.</li>
    <li>Work only in your assigned personal branch.</li>
    <li>To check and sync with main, run:</li>
  </ul>
  <pre>
git checkout main
git pull origin main
  </pre>

  <p>💡 Let's turn dreams into reality — together! ✨</p>

</body>
</html>
