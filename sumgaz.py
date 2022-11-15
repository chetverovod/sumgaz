import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "IlyaGusev/rugpt3medium_sum_gazeta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

article_text = "..."

text_tokens = tokenizer(
    article_text,
    max_length=600,
    add_special_tokens=False, 
    padding=False,
    truncation=True
)["input_ids"]
input_ids = text_tokens + [tokenizer.sep_token_id]
input_ids = torch.LongTensor([input_ids])

output_ids = model.generate(
    input_ids=input_ids,
    no_repeat_ngram_size=4
)

summary = tokenizer.decode(output_ids[0], skip_special_tokens=False)
summary = summary.split(tokenizer.sep_token)[1]
summary = summary.split(tokenizer.eos_token)[0]
print(summary)
