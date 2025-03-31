from tokenizers import ByteLevelBPETokenizer

paths = ['python_code_text_data.txt']

tokenizer = ByteLevelBPETokenizer()

tokenizer.train(files=paths, vocab_size=52_000, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>"
])

# save files to disk
tokenizer.save_model("tokenizer")