import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "./HistoryPage.css";

export default function HistoryPage() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const savedHistory = localStorage.getItem("dreamHistory");
    if (savedHistory) setHistory(JSON.parse(savedHistory));
  }, []);

  return (
    <div className="history-container">
      {/* 🏠 Home Button (Bottom-Left) */}
      <div className="home-btn">
        <Link to="/DreamMirror">🏠 Home</Link>
      </div>

      <h1>📜 Dream History</h1>
      {history.length === 0 ? (
        <p>No history available.</p>
      ) : (
        history.map((entry, i) => (
          <div key={i} className="history-entry">
            <p><strong>{entry.date}</strong></p>
            <p><b>Dream:</b> {entry.dream}</p>
            <p><b>Analysis:</b> {entry.analysis}</p>
            <p><b>Prompt:</b> {entry.prompt}</p>
            <div className="image-grid">
              {entry.images.map((img, j) => (
                <img
                  key={j}
                  src={`http://localhost:5000/${img}`}
                  alt="dream-history"
                />
              ))}
            </div>
            <hr />
          </div>
        ))
      )}
    </div>
  );
}
