import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# https://huggingface.co/IlyaGusev/rugpt3medium_sum_gazeta
model_name = "IlyaGusev/rugpt3medium_sum_gazeta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

article_text = "По сообщению пресс-службы Института астрономии Общества Макса Планка, телескопу James Webb удалось изучить атмосферу экзопланеты так подробно, как никогда прежде. По мнению учёных, это новый уровень наблюдения за экзопланетами, который в будущем даст возможность определять на них наличие внеземной жизни. Телескоп провёл анализ атмосферы газового гиганта WASP-39b. Он напоминает Сатурн в Солнечной системе, вращается вокруг звезды в созвездии Девы и расположен недалеко от неё - примерно на одной восьмой расстояния от Меркурия до Солнца. Эта звезда относится к классу G, как и наше Солнце, но она немного меньше него. Вся система находится на расстоянии около 700 световых лет от Земли. Ещё в августе текущего года сообщалось, что в атмосфере WASP-39b был обнаружен углекислый газ, а теперь появились гораздо более подробные данные о составе атмосферы экзопланеты."

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
    no_repeat_ngram_size=4,
    max_new_tokens = 100 # Plastov
)

summary = tokenizer.decode(output_ids[0], skip_special_tokens=False)
summary = summary.split(tokenizer.sep_token)[1]
summary = summary.split(tokenizer.eos_token)[0]
print(summary)
