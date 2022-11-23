# sumgaz
Gazeta summary generator based on Ilya Gusev's model 
[link to model](https://huggingface.co/IlyaGusev/rugpt3medium_sum_gazeta)

## Create virtual environment
```
$ conda create --name py37 python=3.7
```

### To activate this environment, use
```
$ conda activate py37
```

### To deactivate an active environment, use
```
$ conda deactivate
```
### Install torch
```
$ conda activate py37
does not works:$ sudo pip install torch
does not works:$ conda install torch
$ pip install torchvision 
```

### Install transformers
```
$ pip install transformers
```

### Run application
```
$ python  sumgaz.py 
```
### Application output log example
```
Downloading: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 678/678 [00:00<00:00, 278kB/s]
Downloading: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.61M/1.61M [00:01<00:00, 1.29MB/s]
Downloading: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.27M/1.27M [00:02<00:00, 610kB/s]
Downloading: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2.98M/2.98M [00:04<00:00, 628kB/s]
Downloading: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 24.0/24.0 [00:00<00:00, 9.86kB/s]
Downloading: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 105/105 [00:00<00:00, 39.7kB/s]
Downloading: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 986/986 [00:00<00:00, 364kB/s]
Downloading: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.52G/1.52G [15:53<00:00, 1.60MB/s]
/home/primauser/anaconda3/envs/py37/lib/python3.7/site-packages/transformers/generation_utils.py:1364: UserWarning: Neither `max_length` nor `max_new_tokens` has been set, `max_length` will default to 800 (`self.config.max_length`). Controlling `max_length` via the config is deprecated and `max_length` will be removed from the config in v5 of Transformers -- we recommend using `max_new_tokens` to control the maximum length of the generation.
  UserWarning,
Нападающий «Зенита» Александр Кокорин и полузащитник «Краснодара» Павел Мамаев, обвиняемые в избиении водителя ведущей Первого канала Ольги Ушаковой, отпущены под подписку о невыезде. Об этом сообщил адвокат Кокорина Игорь Бушманов.
```


