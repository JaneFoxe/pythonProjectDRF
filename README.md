Для запуска проекта:

1. Форкнуть репозиторий.
2. Клонировать на локальную машину.
3. Запустить сервер в контейнере Docker командой
"sudo docker-compose up -d —build" в фоновом режиме.
4. Подставить свои значения в файл .env
5. Создать и применить миграции последовательными командами 
python3 manage.py makemigrations и python3 manage.py migrate.
