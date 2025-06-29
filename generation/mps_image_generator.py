import torch
from diffusers import StableDiffusionPipeline
import os

def generate_dream_image(prompt, num_images=3, save_dir="data", resolution=(512, 512)):
    print(f"🧠 Generating {num_images} image(s) from prompt:\n{prompt}\n")

    os.makedirs(save_dir, exist_ok=True)

    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32,
        use_safetensors=True,
    )
    pipe = pipe.to("mps")
    pipe.enable_attention_slicing()

    pipe.unet.config.sample_size = resolution[0] // 8

    with torch.autocast("cpu"):
        result = pipe(
            prompt,
            num_inference_steps=30,
            guidance_scale=7.5,
            height=resolution[1],
            width=resolution[0],
            num_images_per_prompt=num_images,
        )
        images = result.images

    # Save images with incrementing filenames
    paths = []
    base = 1
    while os.path.exists(os.path.join(save_dir, f"generated_dream_{base}.png")):
        base += 1

    for i, img in enumerate(images):
        filename = os.path.join(save_dir, f"generated_dream_{base + i}.png")
        img.save(filename)
        paths.append(filename)
        print(f"✅ Saved: {filename}")

    return paths
