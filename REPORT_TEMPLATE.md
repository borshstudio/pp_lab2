# Лабораторная работа №2
## «Организация промышленного workflow с Git»

**ФИО:** <указать>  
**Группа:** <указать>  
**Вариант:** <указать>  
**Проект:** Python-проект «Git Flow demo calculator»

## 1. Цель работы
Закрепить навыки использования промышленных практик работы с Git: Git Flow, pull request, код-ревью, разрешение конфликтов и автоматизация с помощью Git hooks.

## 2. Организация репозитория
Использовались команды:

```bash
git init
git add .
git commit -m "Initial project structure"
git branch -M main
git remote add origin <URL_ВАШЕГО_РЕПОЗИТОРИЯ>
git push -u origin main
git checkout -b develop
git push -u origin develop
```

Файл `.gitignore` исключает временные файлы Python, виртуальные окружения, папки сборки, настройки IDE и системные файлы ОС.

## 3. История коммитов
Вставить вывод:

```bash
git log --oneline --graph --all --decorate
```

Пример:

```text
<скриншот или текст вывода git log>
```

## 4. Реализация Git Flow и pull request
Была создана ветка `feature/error-handling` от `develop`:

```bash
git checkout develop
git pull
git checkout -b feature/error-handling
```

В ветке были выполнены осмысленные коммиты:

```bash
git add calculator.py
git commit -m "Add division by zero validation"
git add test_calculator.py
git commit -m "Add tests for calculator functions"
git add app.py
git commit -m "Update demo output in application entrypoint"
git push -u origin feature/error-handling
```

Создан Pull Request `feature/error-handling -> develop`.

### Комментарии код-ревью
1. Добавить обработку деления на ноль в функции `divide`, чтобы программа не завершалась с неочевидной ошибкой.
2. Добавить тесты для новой логики, включая сценарий деления на ноль.

После ревью замечания были исправлены дополнительными коммитами в той же ветке, затем PR был одобрен и слит в `develop`.

## 5. Имитация конфликта и его разрешение
Для имитации командной работы были созданы две ветки от `develop`:

```bash
git checkout develop
git checkout -b feature/change-title-a
# изменить строку print("Git Flow demo calculator") в app.py
git add app.py
git commit -m "Change application title by developer A"
git push -u origin feature/change-title-a

git checkout develop
git checkout -b feature/change-title-b
# изменить ту же строку app.py иначе
git add app.py
git commit -m "Change application title by developer B"
git push -u origin feature/change-title-b
```

Первая ветка была слита в `develop`. При слиянии второй возник конфликт в файле `app.py`. Для разрешения использовался mergetool:

```bash
git checkout feature/change-title-b
git fetch origin
git merge origin/develop
git mergetool
git status
git add app.py
git commit -m "Resolve conflict in application title"
git push
```

### Документация решения конфликта
Конфликт возник в строке с названием приложения. Были варианты:

```text
<<<<<<< HEAD
print("Git Flow training calculator")
=======
print("Industrial Git Flow calculator")
>>>>>>> origin/develop
```

Выбрана объединённая формулировка:

```python
print("Industrial Git Flow training calculator")
```

Стратегия: ручное объединение смысла обеих правок, так как обе версии уточняли название приложения.

## 6. Настройка Git hooks
### pre-commit
Файл `.git/hooks/pre-commit` запускает `flake8` для изменённых Python-файлов. Если проверка не проходит, коммит отменяется.

```bash
cp hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

Листинг:

```bash
<вставить содержимое hooks/pre-commit>
```

### post-commit
Файл `.git/hooks/post-commit` добавляет запись в `commit.log`: дата, хеш, автор, сообщение коммита.

```bash
cp hooks/post-commit .git/hooks/post-commit
chmod +x .git/hooks/post-commit
```

Листинг:

```bash
<вставить содержимое hooks/post-commit>
```

## 7. Демонстрация логирования
После коммита в файле `commit.log` появилась запись вида:

```text
2026-05-19 18:30:15 | a1b2c3d | Ivan Ivanov <ivan@example.com> | Add tests for calculator functions
```

Вставить скриншот файла `commit.log` или вывод:

```bash
cat commit.log
```

## 8. Вывод
В ходе лабораторной работы был создан локальный и удалённый Git-репозиторий, настроена модель ветвления Git Flow с ветками `main`, `develop` и `feature/*`. Была реализована функциональность в отдельной feature-ветке, создан pull request, проведено код-ревью с исправлением замечаний. Также была имитирована командная работа с конфликтом изменений, конфликт был разрешён через mergetool и задокументирован. Дополнительно настроены Git hooks: `pre-commit` для автоматической проверки стиля кода и `post-commit` для логирования истории коммитов в файл `commit.log`.
