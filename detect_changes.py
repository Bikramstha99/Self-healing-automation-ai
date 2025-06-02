from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_bert_embedding(text):
    """Get the BERT embedding for a given text"""
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    # Return the mean of all token embeddings as a single representation
    return outputs.last_hidden_state.mean(dim=1).squeeze()

def compare_locators(old_locator, new_locator):
    """Compare old and new locators using BERT embeddings"""
    old_embedding = get_bert_embedding(old_locator)
    new_embedding = get_bert_embedding(new_locator)
    
    # Calculate cosine similarity between embeddings
    similarity = cosine_similarity([old_embedding.numpy()], [new_embedding.numpy()])[0][0]
    
    return similarity

def detect_changes(old_locators, new_locators, threshold=0.8):
    """Detect changes by comparing locators using BERT"""
    matched_locators = {}
    for old_locator in old_locators:
        for new_locator in new_locators:
            similarity = compare_locators(old_locator['value'], new_locator['value'])
            # If the similarity score is higher than a threshold, consider them a match
            if similarity >= threshold:
                matched_locators[old_locator['value']] = new_locator['value']
                break
    return matched_locators
