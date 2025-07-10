from detoxify import Detoxify

def evaluate_text(text, threshold=0.8):
    """
    Loads in model and makes prediction on input text toxicity
    Flags text if toxicity threshhold is above allocated limit
    Returns a dictionary
    """

    model = Detoxify('original')
    scores = model.predict(text)

    # Convert all scores from float32 to regular Python floats
    scores = {k: float(v) for k, v in scores.items()}
    
    return {
        "input": text,
        "toxicity_score": scores["toxicity"],
        "flagged": scores["toxicity"] > threshold,
        "all_scores": scores
    }
