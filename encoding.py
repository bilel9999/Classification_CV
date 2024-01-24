import torch
from transformers import BertTokenizer, BertModel

# # Check if GPU is available
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load BERT tokenizer and model to the specified device
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased')
model = BertModel.from_pretrained('bert-large-uncased')
# model = BertModel.from_pretrained('bert-large-uncased').to(device)
def encode_text(text):
    input_ids = torch.tensor(tokenizer.encode(text, add_special_tokens=True)).unsqueeze(0)
    # input_ids = torch.tensor(tokenizer.encode(text, add_special_tokens=True)).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(input_ids)
    embeddings = outputs.last_hidden_state.squeeze(0)
    aggregated_embedding = torch.mean(embeddings, dim=0)
    print(aggregated_embedding)
    return aggregated_embedding