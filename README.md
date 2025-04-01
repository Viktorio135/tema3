## Основные компоненты

- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **Docker**

## Архитектура

Проект состоит из следующих основных компонентов:

- **Модели**: `Dog` и `Breed`, представляющие собак и их породы соответственно.
- **Сериализаторы**: `DogSerializers` и `BreedSerializers` для преобразования данных моделей в JSON.
- **ViewSets**: `DogViewSet` и `BreedViewSet` для обработки HTTP-запросов и предоставления данных через API.
- **Docker**: Используется для контейнеризации приложения и базы данных для упрощения развертывания и разработки.

Основная часть Views организована внутри ModelViewSets. Для оптимизации запросов к бд используются подзапросы.

## Установка и запуск

### Предварительные требования

- Docker и Docker Compose.

### Шаги по установке

1. **Клонируйте репозиторий**:
2. **Создайте файл .env** (пример в .env.example)
3. **Сборка и запуск контейнеров**
   ```
   docker-compose up --build
   ```
## Примеры использования API
Запрос:
  ```
  GET /api/dogs/
  ```
Ответ:
  ```
  [
      {
          "id": 1,
          "name": "Buddy",
          "breed": 1,
          "age": 3,
          "avg_age": 4.5
      },
      ...
  ]
  ```
Запрос:
  ```
  curl -X POST http://localhost:8000/api/dogs/ -H "Content-Type: application/json" -d '{
  "name": "шицу",
  "size": "Tiny",
  "friendliness": 5,
  "trainability": 2,
  "shedding_amount": 1,
  "exercise_needs": 3
  }'
  ```
Запрос:
  ```
  DELETE /api/dogs/id/
  ```