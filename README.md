# Лабораторна робота №3

Тема: обробка виключень, модульність та документація в проєктах Python.

## Структура

```
.
├── lb3t1.py                      # Завдання 1: try/except/else/finally, with
├── lb3t2.py                      # Завдання 2: власні виключення, raise ... from ...
├── laba3.3/                      # Завдання 3: пакет з підпакетами
│   ├── requirements.txt
│   └── app_package/
│       ├── __init__.py
│       ├── __main__.py           # точка входу для python -m app_package
│       ├── exceptions/           # підпакет: доменні виключення
│       │   ├── __init__.py
│       │   └── domain_exceptions.py
│       └── services/             # підпакет: бізнес-логіка
│           ├── __init__.py
│           ├── parser.py
│           └── validator.py
├── laba3.4/                      # Завдання 4: той самий пакет з docstrings та анотаціями типів
│   ├── requirements.txt
│   └── app_package/
│       └── ...                   # структура як у laba3.3
├── README.md
└── .gitignore
```

## Вимоги

- Python 3.10+ (3.11+ лише для необов'язкового `except*`)
- Сторонні бібліотеки не використовуються

## Запуск

Завдання 1 і 2 запускаються з кореня репозиторію:

```bash
python lb3t1.py
python lb3t2.py
```

Завдання 3 і 4 запускаються з відповідної папки:

```bash
cd laba3.3
python -m app_package
```

```bash
cd laba3.4
python -m app_package
```

Інтроспекція (`help()`, `__doc__`, `__annotations__`) для завдання 4:

```bash
cd laba3.4
python -c "from app_package.services import parser; help(parser)"
```
