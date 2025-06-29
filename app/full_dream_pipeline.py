# app/full_dream_pipeline.py

from analysis.dream_analyzer import analyze_dream
from generation.prompt_builder import generate_prompt
from generation.mps_image_generator import generate_dream_image

def main():
    print("\n🌙 Welcome to DreamMirror AI 🌌")
    user_input = input("📝 Describe your dream: ")

    print("\n🔍 Analyzing your dream...")
    analysis = analyze_dream(user_input)

    print("\n🪄 Generating visual prompt...")
    prompt = generate_prompt(analysis)
    print(f"✨ Prompt: {prompt}")

    print("\n🎨 Generating all the images from dream...")
    image_paths = generate_dream_image(prompt, num_images=3)

    print("\n🖼️ All dream images generated:")
    for path in image_paths:
        print(f" - {path}")
        
    print("🖼️ Open the image to see your dream come to life!\n")
    
    while True:
        print("\nWhat would you like to do next?")
        print("1️⃣  Regenerate dream visuals")
        print("2️⃣  Rate this dream")
        print("3️⃣  Exit")

        choice = input("Enter option number (1/2/3): ").strip()

        if choice == "1":
            print("\n🔁 Regenerating dream visuals...")
            image_paths = generate_dream_image(prompt, num_images=3)
            for path in image_paths:
                print(f" - {path}")
        elif choice == "2":
            rating = input("⭐ Rate this dream from 1 to 5: ").strip()
            print(f"📌 Dream rated {rating}/5. (Optional: save to dream journal next!)")
        elif choice == "3":
            print("👋 Exiting. See you in your next dream!")
            break
        else:
            print("❗ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
