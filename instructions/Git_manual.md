# Руководство пользователя Git
## Локальные репозитории
### Команды
* git init - инициализирует локальный репозиторий
* git commit - создает коммит 
  1. -m - текст
  2. -a - +add
* git log - показывает историю изменений
 1. --graph - Отображение в виде дерева
* git checkout **** - переход к изменению по первым 4 знакам
* git status - нынешний статус
* git push - отправка и синхронизация локального и удаленного репозитория
* git pull - загрузка данных с удаленого репозитория
* git diff - разница между commit
* git add - сохранение в системе git
* git branch - выводит список веток
* git merge - слияние веток
* git clone <Ссылка> - Скачивает репозиторий по ссылкеД
* git remote add origin <links> - Добавление ссылки к удаленому репозиторию
---
* Подключение к публичному репозиторию для предложения изменений 
  1. Создаем копию репозитория в своем аккаунте с помощью форка (fork).
  2. Загружаем на компьютер с удаленого репозитория (git pull <links>).
  3. Создаем новую ветку (git branch).
  4. Переходим на ветку (git checkout).
  5. Вносим необходимые изменения.
  6. Сохраняем (git add и git commit).
  7. Отправляем на удаленный репозиторий (git push).
  8. На Github делаем pull request


* создание нового репозитория на Github
1. echo "# Geek" >> README.md
2. git init
3. git add README.md
4. git commit -m "first commit"
5. git branch -M main
6. git remote add origin https://github.com/DaemoniumLupus/Geek.git
7. git push -u origin main