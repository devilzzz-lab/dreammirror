import React, { useState } from "react";
import axios from "axios";
import "./DreamMirror.css";

export default function DreamMirror() {
  const [dream, setDream] = useState("");
  const [analysis, setAnalysis] = useState(null);
  const [prompt, setPrompt] = useState("");
  const [images, setImages] = useState([]);
  const [loading, setLoading] = useState(false);

  // Chat state
  const [chatMessages, setChatMessages] = useState([]);
  const [chatInput, setChatInput] = useState("");
  const [chatLoading, setChatLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!dream.trim()) return alert("Please describe your dream.");
    setLoading(true);
    setImages([]);
    setAnalysis(null);
    setPrompt("");

    try {
      const res = await axios.post("http://localhost:5000/analyze", { dream });
      setAnalysis(res.data.analysis);
      setPrompt(res.data.prompt);
      setImages(res.data.images);
    } catch (err) {
      console.error(err);
      alert("Error analyzing dream.");
    }
    setLoading(false);
  };

  const handleChatSend = async () => {
    if (!chatInput.trim()) return;
    const userMsg = { sender: "user", text: chatInput };
    setChatMessages((prev) => [...prev, userMsg]);
    setChatLoading(true);
    setChatInput("");

    try {
      const res = await axios.post("http://localhost:5000/chat", { message: chatInput });
      const botMsg = { sender: "bot", text: res.data.reply };
      setChatMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      console.error(err);
      const botMsg = { sender: "bot", text: "Sorry, I couldn't respond right now." };
      setChatMessages((prev) => [...prev, botMsg]);
    }
    setChatLoading(false);
  };

  return (
    <div className="dreammirror-container">
      {/* Dream Section */}
      <div className="dream-section">
        <h1>🌙 DreamMirror AI</h1>
        <textarea
          placeholder="Describe your dream..."
          value={dream}
          onChange={(e) => setDream(e.target.value)}
        />
        <button onClick={handleAnalyze} disabled={loading}>
          {loading ? "Processing..." : "Analyze & Generate"}
        </button>

        {analysis && (
          <div>
            <h2>✨ Prompt</h2>
            <p>{prompt}</p>
            <div className="image-grid">
              {images.map((img, i) => (
                <img key={i} src={`http://localhost:5000/${img}`} alt="dream" />
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Chat Section */}
      <div className="chat-section">
        <h2>💬 Emotional Support AI</h2>
        <div className="chat-box">
          {chatMessages.map((msg, i) => (
            <div key={i} className={`chat-message ${msg.sender}`}>
              {msg.text}
            </div>
          ))}
          {chatLoading && <div className="chat-message bot">Typing...</div>}
        </div>
        <div className="chat-input">
          <input
            type="text"
            placeholder="Type your feelings..."
            value={chatInput}
            onChange={(e) => setChatInput(e.target.value)}
            onKeyPress={(e) => e.key === "Enter" && handleChatSend()}
          />
          <button onClick={handleChatSend}>Send</button>
        </div>
      </div>
    </div>
  );
}
