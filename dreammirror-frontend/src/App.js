import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import DreamMirror from "./Components/DreamMirror";
import HistoryPage from "./Components/HistoryPage";
import Login from "./Components/Login";
import Signup from "./Components/Signup";
import "./App.css";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/dreammirror" element={<DreamMirror />} />
        <Route path="/history" element={<HistoryPage />} />
      </Routes>
    </Router>
  );
}

export default App;
