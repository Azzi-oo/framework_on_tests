#!/bin/bash

# Активируем виртуальное окружение
source venv/bin/activate

# Запускаем тесты с Allure
echo "Running tests with Allure reporting..."
pytest test_petstore.py --alluredir=allure-results

# Генерируем отчет
echo "Generating Allure report..."
allure generate allure-results -o allure-report --clean

# Открываем отчет в браузере
echo "Opening Allure report in browser..."
allure open allure-report
