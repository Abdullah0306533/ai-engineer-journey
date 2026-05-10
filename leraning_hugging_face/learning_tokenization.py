from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

text = "Abdullah Butt is an unconstitutional phenomenon"
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text)
decoded = tokenizer.decode(token_ids)

print(f"Original: {text}")
print(f"Tokens: {tokens}")
print(f"Token IDs: {token_ids}")
print(f"Decoded back: {decoded}")
print(f"Token count: {len(tokens)}")