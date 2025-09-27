import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from analysis.dream_analyzer import analyze_dream
from generation.prompt_builder import generate_prompt
from generation.mps_image_generator import generate_dream_image
from chatbot.support_bot import get_support_reply

# --- Setup ---
app = FastAPI()

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure dream_outputs directory exists inside app folder
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "dream_outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Mount static files
app.mount("/dream_outputs", StaticFiles(directory=OUTPUT_DIR), name="dream_outputs")

# --- Request Models ---
class DreamRequest(BaseModel):
    dream: str

class ChatRequest(BaseModel):
    message: str

# --- Endpoints ---
@app.post("/analyze")
async def analyze_dream_endpoint(req: DreamRequest):
    analysis = analyze_dream(req.dream)
    prompt = generate_prompt(analysis)
    image_paths = generate_dream_image(prompt, num_images=3, save_dir=OUTPUT_DIR)

    # Generate URLs for frontend
    public_paths = [f"/dream_outputs/{os.path.basename(p)}" for p in image_paths]

    return {
        "analysis": analysis,
        "prompt": prompt,
        "images": public_paths
    }

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    reply = get_support_reply(req.message)
    return {"reply": reply}
