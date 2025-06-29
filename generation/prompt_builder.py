# generation/prompt_builder.py

def generate_prompt(analysis):
    nouns = ", ".join(analysis["nouns"])
    adjectives = ", ".join(analysis["adjectives"])
    verbs = ", ".join(analysis["verbs"])

    prompt = f"A surreal dream scene with {adjectives} {nouns}, where someone is {verbs}. Atmospheric lighting, soft surreal colors, mystical tone."
    return prompt
