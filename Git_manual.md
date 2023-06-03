# Руководство пользователя Git
## Локальные репозитории
### Команды
* git init - инициализирует локальный репозиторий
* git commit - создает коммит 
  1. -m - текст
  2. -a - +init
* git log - показывает историю изменений
 1. --graph - Отображение в виде дерева
* git checkout **** - переход к изменению по первым 4 знакам
* git status - нынешний статус
* git push - отправка и синхронизация локального и удаленного репозитория
* git pull - загрузка данных с удаленого репозитория
* git diff - разница между commit
* git add - сохранение в сиситеме git
* git branch - выводит список веток
* git merge - слияние веток
* git clone <Ссылка> - Скачивает репозиторий по ссылкеД



* создание нового репозитория на Github
1. echo "# Geek" >> README.md
2. git init
3. git add README.md
4. git commit -m "first commit"
5. git branch -M main
6. git remote add origin https://github.com/DaemoniumLupus/Geek.git
7. git push -u origin main