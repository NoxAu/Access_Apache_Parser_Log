# Access_Apache_Parser_Log

<!--Установка-->
## Установка
1. Клонирование репозитория:
```sh
git clone https://github.com/NoxAu/Access_Apache_Parser_Log.git
```

2. Переход в каталог проекта:
```sh
cd Access_Apache_Parser_Log
```

3. Устанавливаем зависимости:
```sh
pip install -r requirements.txt
```

4. Настраиваем конфигурационный файл config.yml:
```yaml
app:
  # automatic aggregation of logs
  schedule_update_logs_enabled: True
  # aggregation interval in seconds
  schedule_update_logs_delay: 30
  # automatic launch of the Apache web server
  start_apache_server: True

logs:
  format: '%h %l %u %t \"%r\" %>s %b'
  # the path to the folder with logs
  path: server/Apache24/logs
  # the name of the file with access logs
  access_log: access.log
```
5. Запустить приложение
```sh
python main.py
```
# Инструкция по использованию
Формат:
```sh
*Type of request* [*Request Parameter*]
```
## Виды запроса
*get*: get the data  
*parse*: aggregate data from a file to a database  
*help*: show this text again  
## Параметры
### get:
No parameters : no filtering  
-ip : filter by IP address   
-date : filter by date  
-start_date : filter on the left border of the date interval in logs (used together with end_date)  
-end_date : filter on the right border of the date interval in logs (used together with start_date)  

Примеры использования:
```sh 
get -ip 127.0.0.1
get -ip 127.0.0.1 -date 2024-06-10
get -ip 127.0.0.1 -start_date 2024-06-10 -end_date 2024-06-12
```
# Формат данных 
The date in the request is specified in the format "yyyy-mm-dd"  
Examples:  
```sh
2024-06-10  
2024-12-31
```
The IP address is specified in the standard format "ddd.ddd.ddd.ddd"  
Examples:
```sh
127.0.0.1
255.255.255.255
```
# Выход из приложения
To exit, use ```
w```

