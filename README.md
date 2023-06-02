# simple-fastapi-project
simple fastapi project

# Правила работы с кодом

## Настройка окружения

### Создание virtualenv
Чтобы точно воспроизвести окружение и версии библиотек необходимо использовать virtualenv

Для Linux и MacOs
```
python3 -m venv venv
```

Для Windows
```
py -m venv venv
```

Будет создана директория venv, из которой можно активировать окружение

Для Linux и MacOs
```
source venv/bin/activate
```

Для Windows
```
venv\Scripts\activate.bat
```

### Установка зависимостей
Сперва рекомендуется обновить pip
```
pip install --upgrade pip
```

Для установки зависимстей необходимо активировать окружение и выполнить
```
pip install -r requirements.txt
```

### Установка основного пакета

Для переиспользования кода из пакета recosys нужно установить его в режиме редактирования
```
pip install -e .
```