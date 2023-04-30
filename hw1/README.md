## Запуск

```
docker-compose build
```

```
docker-compose up
```


Для редактирования тестовых данных нужно поредачить ```server/test_data.py```
## Запросы


Поддерживаемы форматы: ["native", "xml", "json", "protobuf", "avro", "yaml", "msgpack", "all"]

Вид запроса:
```
echo "get_result FORMAT" | nc -u localhost 2000
```

# Например:
Req1:
```
echo "get_result yaml" | nc -u localhost 2000
```

Resp1:
```
yaml - 127  - 54.92176907137036ms - 89.49686866253614ms
```

Req2:
```
echo "get_result protobuf" | nc -u localhost 2000
```
Resp2:
```
protobuf - 58  - 5.154924932867289ms - 0.09633786976337433ms
```

Req3:
```
echo "get_result protobuf" | nc -u localhost 2000
```
Resp3:
```
native - 147  - 0.1883581280708313ms - 0.2340259961783886ms
xml - 453  - 11.388526298105717ms - 17.983976751565933ms
json - 146  - 0.7125837728381157ms - 0.4384862259030342ms
protobuf - 58  - 5.154924932867289ms - 0.09633786976337433ms
avro - 44  - 1.1196020059287548ms - 1.0358081199228764ms
yaml - 127  - 54.92176907137036ms - 89.49686866253614ms
msgpack - 98  - 0.23178430274128914ms - 0.1715598627924919ms
```