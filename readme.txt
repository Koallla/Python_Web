Доступные команды:
1 - Добавить новую запись в БД
2 - Поиск записи в БД
3 - Изменение записи в БД
4 - Удаление записи из БД
5 - Выход из программы
6 - Показать все записи в БД




Запуск контейнера с redis.conf:

docker run -d --name redis-test -p 6379:6379  -v /D//Python//Python_Web//redis.conf:/redis.conf redis redis-server /redis.conf

redis-cli:
docker exec -it <container id> redis-cli