# Урок 31
Для начала работы скопируйте репозиторий на локальную машину с помощью команды в терминале:

`git clone https://github.com/skypro-008/lesson31-and-tests.git`

Откройте с клонированный репозиторий в PyCharm.

### Создайте виртуальное окружение:

#### Простой вариант:
Pycharm может предложить вам сделать это после того, как вы откроете папку с проектом.
В этом случае после открытия папки с проектом в PyCharm.
Появляется всплывающее окно, Creating virtual environment c тремя полями.
В первом поле выбираем размещение папки с виртуальным окружением, как правило, это папка venv
в корне проекта
Во втором поле выбираем устанавливаемый интерпретатор по умолчанию (можно оставить без изменений)
В 3 поле выбираем список зависимостей (должен быть выбран файл requirements.txt, 
находящийся в корне папки проекта)

#### Если этого не произошло, тогда следует выполнить следующие действия вручную:
#### Установка виртуального окружения:
1. Во вкладке File выберите пункт Settings
2. В открывшемся окне, с левой стороны найдите вкладку с именем
вашего репозитория (Project: lesson31-and-tests)
3. В выбранной вкладке откройте настройку Python Interpreter
4. В открывшейся настройке кликните на значок ⚙ (шестеренки) 
расположенный сверху справа и выберите опцию Add
5. В открывшемся окне слева выберите Virtualenv Environment, 
а справа выберите New Environment и нажмите ОК

#### Установка зависимостей:
Для этого можно воспользоваться графическим интерфейсом PyCharm,
который вам предложит сделать это как только вы откроете файл с заданием.

Или же вы можете сделать это вручную, выполнив следующую команду в терминале:
`pip install -r requirements.txt`

*У владельцев операционной системы MacOS могут возникнуть сложности с установкой зависимостей.
Если возникла ошибка - сначала выполните в терминале команду brew install postgresql.
После её выполнения ошибок с установкой зависимостей быть не должно.
#### Настройка виртуального окружения завершена!

### Подготовка проекта django
После того как Вы установили все зависимости, необходимо подготовить django к работе:
для этого нам потребуется:

1. Иметь возможность запуска на локальной машине docker-контейнера 
(необходимо для запуска контейнера с базы данных):
- переходим в каталог `postgres_l31` и выполняем команду `docker-compose up -d`.

2. Выполнить необходимые команды для подготовки базы данных к работе:
Текущий проект уже содержит настроенную базу данных, но пока еще она 
пустая, не содержит таблиц, а всё её наполнение
находится в фикстурах (в django - файлы в формате json содержащие данные для наполнения БД).
Для начала для создания таблиц в нашей базе данных выполните команды
`python3 manage.py makemigrations` и `python3 manage.py migrate`,
после чего перенесите фикстуры из json файлов в базу данных с помощью команды
`python3 manage.py loadall`

Данная часть тренажера состоит из одного django-проекта в котором,
каждое приложение соответствует одному заданию.


### Порядок выполнения заданий

## Часть 1


### Задание unique_links
Перейдите в приложение unique_links.
И измените модель UniquePost таким образом, чтобы значение поля slug было уникальным
Для успешного выполнения данного задания достаточно просто внести изменения в соответствующую модель 

### Задание smallest
Перейдите в приложение smallest, в котором представлена модель постов.
Сделайте так, чтобы в тексте каждого поста было как минимум 5 символов.
При выполнении данного задания попробуйте проверить себя и создать пост с помощью POST-запроса
на адрес `/smallest/`. 
При этом, перед тем, как осуществить такой запрос, не забудьте получить токен
существующего пользователя - такое ограничение предусмотрено исходным кодом задачи.

Чтобы сделать запрос от аутентифицированного пользователя,
получите токен c помощью POST-запроса на адрес `/token/`
Учетные данные для проверок:
username: `sky_user`
password: `skypro`
Чтобы сделать аутентифицированный запрос, передайте token пользователя
в заголовке 'Authorization' HTTP запроса:
```
Authorization: Token <token value>
```
В данном случае аутентифицированный запрос необходим для того, 
чтобы сохранить в БД, каким именно пользователем создан пост.

### Задание back_to_future
Перейдите в приложение back_to_future
Напишите валидатор для поля code модели Vacation,
который проверяет, что соответствующая запись поля code есть в модели Code 
(связывать модели между собой не нужно).
Для самопроверки попробуйте отправить соответствующий POST-запрос на адрес `/back_to_future/` 
с необходимыми данными.
Если вы не забыли сделать миграции и загрузить фикстуры, имеющиеся в проекте,
то в базе данных в модели Code уже должна быть сохранена такая запись:

```json
  {
    "model": "back_to_future.code",
    "pk": 1,
    "fields": {
      "code": "main"
    }
  }
```

### Задание comments_not_required
Перейдите в приложение comments_not_required.
Измените сериализатор записи о мероприятии таким образом,
чтобы он выполнял следующие требования:
1. При изменении (PATCH-запрос) поле comment в модели Calendar нельзя изменить.
2. При создании нового объекта (POST-запрос) данное поле могло бы быть пустым.

Адрес для запросов: `/events/`
   
### Задание try_to_dismiss
Перейдите в приложение try_to_dismiss.
Для данной модели сотрудника и сериалайзера проверьте, 
что дата увольнения, полученная от пользователя, наступает не раньше сегодняшнего дня.
Адрес для запросов: `/resources/`

## Часть 2

### Задание default_shop "Магазин по умолчанию"
Перейдите в файл factories приложения default_shop.
Вам дана модель магазина и фабрика к этой модели. 
Допишите фабрику так, чтобы у нее всегда проставлялись 
координаты и store_id (значения указаны в константах).


### Задание use_factory "Использую фабрику"
Перейдите в файл factory_test.py приложения use_factory.
В файле factories.py того же приложения вам дана фабрика для модели Skill. 
Подключите ее как фикстуру в тест и проверьте, 
что поле name заполнено значением "Skill 1".

### Задание choco "Шоколада много не бывает"
Перейдите в файл list_test.py приложения choco.
У нас есть View, которая выводит только 5 записей из модели. 
Для модели уже написана фабрика. 
Напишите тест, в котором создается 6 записей модели (через фабрику) 
и проверяется, что при GET-запросе на адрес `/choco/` возвращается только 5 из них. 
Важно только количество. 
Данные из ручки отдаются в формате: 
```json
{
	"items": [
	  {
		"name": "choco 1"
	  },
      {
		"name": "choco 2"
	  }
	]
}
```

### Задание get_list "Как слышно" 
Перейдите в файл get_list_test.py приложения get_list.
Напишите тест, который проверяет, что GET-запрос на адрес `get_list` отвечает статусом 200.

### Задание create_choco "Только самое важное"
Перейдите в файл create_choco_test.py приложения create_choco.
Ручка POST `choco_create` создает шоколадку, но возвращает 
только поле name сохраненной шоколадки. 
Мы написали все входящие и исходящие данные. 
Допишите тест так, чтобы он проверял статус ответа (201) 
и его правильность.

### Задание healthcheck "Есть кто живой"
Перейдите в файл healthcheck_test.py приложения healthcheck.
Для проверки работоспособности в приложении было написано 3 ручки 
`/lifecheck/`, `/readynesscheck/`, `/healthcheck/`, которые отдают status_code=200. 
Используя свои знания о parametrize, напишите 1 тест-функцию, которая проверит все три ручки.

### Задание name_template "Шаблон имени"
Перейдите в файл template_test.py приложения name_template.
Наша ручка для сохранения шоколада `/chocolate/create/` принимает только названия, 
начинающиеся с `Choco`. Используя parametrize, напишите функцию, 
которая проверяет, что на имя Choco отдается код 200, а на имя Test — 422.
