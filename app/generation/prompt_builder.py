def generate_prompt(analysis: dict) -> str:
    nouns = ", ".join(analysis.get("nouns", [])) or "mystical landscapes"
    adjectives = ", ".join(analysis.get("adjectives", [])) or "dreamlike"
    verbs = ", ".join(analysis.get("verbs", [])) or "floating"

    prompt = (
        f"A surreal dream scene with {adjectives} {nouns}, "
        f"where someone is {verbs}. Atmospheric lighting, "
        f"soft surreal colors, mystical tone."
    )
    return prompt
