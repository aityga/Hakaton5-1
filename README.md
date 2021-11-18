Интернет-магазин на Django + React.js [Базовый функционал]

Инструкция по запуску:

Внимание!! На машине обязательно должен быть установлен **Node.js**! 

[Скачать NodeJS](https://nodejs.org/en/download/)

1. Создать директорию, куда будете клонировать проект и перейти в нее
2. Клонировать проект с помощью `git clone`, указав **ssh** или **https** адрес
3. Создать виртуальное окружение (с помощью **venv**, например - `python3 -m venv имя_окружения`)
4. Активировать виртуальное окружение
-  `.\имя_окружения\Scripts\activate.bat`- **Windows**
- `source имя_окружения/bin/activate/` - **unix**

5. Перейти в **eshop-ui**
6. Прописать `npm install`
7. Прописать `npm install axios`
8. Прописать `npm run build`
9. Вернуться в **djreactshop**
10. Прописать `python manage.py makemigrations` и `python manage.py migrate`
11. Прописать `python manage.py collectstatic`
12. Создать пользователя - `python manage.py createsuperuser`
13. Запустить сервер - `python manage.py runserver`
14. Зайти в админку и создать там *Customer*'а для созданного выше пользователя и Корзину
15. Создать **Категорию** и товар, чтобы потестировать работу корзины.
