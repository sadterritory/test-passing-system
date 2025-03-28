# CGI и PHP тестирующая система

## Описание проекта
Проект реализует веб-приложение для проведения тестов с двумя вариантами реализации:
1. CGI-скрипт (Python) с поддержкой cookies и историей результатов
2. PHP-скрипт с сохранением результатов в файл

## Функционал

### Общий для обеих реализаций:
- Тест из 3+ вопросов
- 3+ варианта ответа на каждый вопрос
- Поддержка вопросов с несколькими правильными ответами
- Отображение даты прохождения теста

### CGI-версия:
- Поддержка методов GET и POST
- Хранение результатов в cookies
- Отображение текущих и предыдущих результатов
- Универсальный обработчик запросов

### PHP-версия:
- Сохранение результатов в текстовый файл
- Ссылка для просмотра полной истории результатов
- Простое текстовое представление результатов

## Технологии
- Python 3.x (для CGI-версии)
- PHP 7.4+ (для PHP-версии)
- Веб-сервер с поддержкой CGI (Apache, Nginx)
- HTML/CSS для интерфейса
