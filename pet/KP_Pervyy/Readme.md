## Запуск и проверка PostgreSQL (macOS + Homebrew)

### Запуск сервера PostgreSQL
```bash
brew services start postgresql@15
```
### Проверка, что сервис запущен
```bash
brew services list | grep postgresql
```
### Проверка доступности сервера и порта
```bash
pg_isready -h 127.0.0.1 -p 5432
```
### Подключение к PostgreSQL под пользователем macOS
При установке PostgreSQL через Homebrew по умолчанию создаётся роль, совпадающая с именем пользователя macOS.
```bash
psql -h 127.0.0.1 -p 5432 -U homekarpov postgres
```
### Просмотр существующих ролей
После подключения к PostgreSQL выполните:
```bash
\du
```
