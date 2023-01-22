# webfasumgas
Web-application based on FastAPI . Makes summary of newspaper article on Russian. 

Based on Ilya Gusev's model [link to model](https://huggingface.co/IlyaGusev/rugpt3medium_sum_gazeta).
# fasumgaz
Web-applicatation for newspaper summarization,
based on Ilya Gusev's model 
[link to model](https://huggingface.co/IlyaGusev/rugpt3medium_sum_gazeta)
FastAPI is used as web-interface.

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

## Install dependancies
```
$ pip install -r requirements.txt

```

## Run web-application
```
$ uvicorn webfasumgaz:app
```
URL of service will be printed in command line.
Use curl or postman for acces to service. For
example:
```
curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"text": "О том, что лидеру республиканцев в Палате представителей может не хватить голосов для получения должности, его оппоненты предупреждали давно. В частности, об этом за пару недель до исторического голосования заявляли пять крайне правых республиканцев из полусекретного кружка «Кокус свободы». Лидеры созданной еще в 2015 году организации не скрывали своего намерения изменить ситуацию в нижней палате сразу после промежуточных выборов в Конгресс, предупреждая, что воспользуются для этого процедурой голосования за спикера. Поскольку в это объединение, по разным данным входят десятки конгрессменов, эксперты не исключали, что желающих выторговать для крайне правых более выгодные для них условия будет гораздо больше, чем пять. Это стало очевидно из подсчета голосов, которые господин Маккарти получил в ходе голосования за него как за лидера партии. В ноябре один из членов «Кокуса свободы», Чип Рой, выдвинул на этот пост альтернативного кандидата — конгрессмена от Аризоны и тоже члена «Кокуса» Энди Биггса."}'
```
Reference answer:
```
"Палата представителей США может не получить большинство в сенате из-за того, что лидер республиканцев в сенате республиканец Митт Ромни не сможет набрать необходимое количество голосов для получения кресла спикера."
```
