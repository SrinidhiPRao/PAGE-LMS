def build_prompt(topic: str, personality: str, emotion: str) -> str:
    """
    Builds a contextually adaptive learning prompt for the LLM
    based on personality and emotional state.
    """

    base_intro = f"Generate educational content on the topic: '{topic}'."
    style_intro = (
        "Adapt your explanation style based on the learner's personality and emotion."
    )

    personality_prompts = {
        "openness": "Encourage exploration and creative thinking. Include interdisciplinary examples and open-ended questions.",
        "conscientiousness": "Provide structured, step-by-step guidance with clear goals and verification checkpoints.",
        "extraversion": "Use conversational tone and social engagement cues. Suggest interactive or collaborative tasks.",
        "agreeableness": "Be supportive and cooperative. Use friendly, collaborative examples.",
        "neuroticism": "Use calm, reassuring tone. Simplify concepts and include encouraging feedback.",
    }

    emotion_modifiers = {
        "frustrated": "Use gentle, encouraging language. Simplify explanations and build confidence.",
        "curious": "Offer deeper insights and challenges to sustain curiosity.",
        "confused": "Clarify step-by-step. Avoid jargon and confirm understanding frequently.",
        "satisfied": "Provide brief summary and suggest next-level topics to build on success.",
        "anxious": "Be empathetic and supportive. Reinforce that mistakes are part of learning.",
    }

    personality_text = personality_prompts.get(personality.lower(), "")
    emotion_text = emotion_modifiers.get(emotion.lower(), "")

    return (
        f"{base_intro}\n{style_intro}\n\n"
        f"Learner Personality: {personality}\n"
        f"Current Emotion: {emotion}\n\n"
        f"Adaptation Guidelines:\n- {personality_text}\n- {emotion_text}\n\n"
        f"Now, generate a psychologically adaptive, personalized learning explanation."
    )
