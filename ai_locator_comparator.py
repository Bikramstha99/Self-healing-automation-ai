# ai_locator_comparator.py
from sentence_transformers import SentenceTransformer
import numpy as np

# Load a pre-trained Sentence-BERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def compare_locators_using_ai(old_locator, new_locator):
    """
    Compare locators using AI (BERT/Sentence-BERT) embeddings.
    If similarity score > threshold, consider them as same.
    """
    embeddings_old = model.encode([old_locator])
    embeddings_new = model.encode([new_locator])

    # Calculate cosine similarity
    cosine_similarity = np.dot(embeddings_old, embeddings_new.T) / (np.linalg.norm(embeddings_old) * np.linalg.norm(embeddings_new))
    
    return cosine_similarity[0][0]

def detect_changes_using_ai(old_locators, new_locators, similarity_threshold=0.7):
    """
    Detect changes by comparing locators using AI-based similarity detection.
    """
    matched_locators = {}
    for old_key, old_locator in old_locators.items():
        for new_key, new_locator in new_locators.items():
            similarity = compare_locators_using_ai(old_locator, new_locator)
            if similarity >= similarity_threshold:
                matched_locators[old_key] = new_key
                break

    return matched_locators
