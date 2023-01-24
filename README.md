# webfasumgaz
Web-application based on FastAPI. Makes summary of newspaper article on Russian. 

Based on Ilya Gusev's model, [link to model](https://huggingface.co/IlyaGusev/rugpt3medium_sum_gazeta).

## Install Anaconda
See info hear [Digtal Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-20-04)

## Create virtual environment
```
$ conda create --name py37 python=3.7
```

## Activate this environment
```
$ conda activate py37
```

## Install dependancies
```
$ cd  ~/webfasumgaz
$ pip install -r requirements.txt
$ pip install "fastapi[all]"
$ pip install "uvicorn[standard]"
$ conda install pytorch
$ conda install transformers

```

## Run web-application with acces trough local host
```
$ uvicorn webfasumgaz:app
```

## Run web-application with acces trough external IP-address
### Enable port
```
$ sudo ufw allow 8000
```
### Start with option --host 0.0.0.0
```
$ uvicorn --host 0.0.0.0 webfasumgaz:app
```

URL of service will be printed in command line.
Use curl or postman for acces to service.
For example:
```
curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"text": "О том, что лидеру республиканцев в Палате представителей может не хватить голосов для получения должности, его оппоненты предупреждали давно. В частности, об этом за пару недель до исторического голосования заявляли пять крайне правых республиканцев из полусекретного кружка «Кокус свободы». Лидеры созданной еще в 2015 году организации не скрывали своего намерения изменить ситуацию в нижней палате сразу после промежуточных выборов в Конгресс, предупреждая, что воспользуются для этого процедурой голосования за спикера. Поскольку в это объединение, по разным данным входят десятки конгрессменов, эксперты не исключали, что желающих выторговать для крайне правых более выгодные для них условия будет гораздо больше, чем пять. Это стало очевидно из подсчета голосов, которые господин Маккарти получил в ходе голосования за него как за лидера партии. В ноябре один из членов «Кокуса свободы», Чип Рой, выдвинул на этот пост альтернативного кандидата — конгрессмена от Аризоны и тоже члена «Кокуса» Энди Биггса."}'
```
Reference answer:
```
"Палата представителей США может не получить большинство в сенате из-за того, что лидер республиканцев в сенате республиканец Митт Ромни не сможет набрать необходимое количество голосов для получения кресла спикера."
```
