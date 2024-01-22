# Minecraft Plugins Testing Tool
# EN

**Author:** drazz

**License:** [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

---

## Description
The *Minecraft Plugins Testing Tool*, developed by *drazz*, is a Python program designed to simplify the process of testing Minecraft plugins on various server cores and versions. The tool provides a user-friendly graphical interface for configuring and launching Minecraft servers with different plugins and settings.

---

## Guide

1. **Select Java:**
   Click the "Select Java" button to choose the Java executable (`java.exe`) for running the Minecraft server.

2. **Java Arguments:**
   Specify Java arguments in the "Java Arguments" text box. Add the argument `-XX:MaxPermSize=256M` if the "Java Not Recognized" error occurs.

3. **Select Core:**
   Choose the server core from the drop-down menu. The available cores are dynamically loaded from the configuration file.

4. **Select Version:**
   Choose the Minecraft version for the selected core. The available versions are loaded based on the chosen core.
   
6. **Launch:**
   Press the "Launch" button to start the Minecraft server with the specified configurations. The tool will automatically download and set up the server files if they are not present.

---

## Features
- User-friendly GUI for configuring server launch parameters.
- Dynamic loading of server cores and versions from a configuration file (`versions.json`).
- Automatic download of server files for the selected core and version.
- Detailed error messages.

---

## Notes
- Make sure to provide the correct Java executable path.
- Customize Java arguments based on your server requirements.

---

## Disclaimer
This tool is provided under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). Users are encouraged to review and adhere to the license terms. The tool is not affiliated with Mojang or Minecraft.


# RU

**Автор:** drazz

**Лицензия:** [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

---

## Описание
Инструмент тестирования плагинов Minecraft, разработанный *drazz*, представляет собой программу на языке Python, предназначенную для упрощения процесса тестирования плагинов Minecraft на различных ядрах и версиях. Инструмент предоставляет удобный графический интерфейс для настройки и запуска серверов Minecraft с различными плагинами и параметрами.

---

## Руководство

1. **Выбор Java:**
   Нажмите кнопку "Выбрать Java", чтобы выбрать исполняемый файл Java (`java.exe`) для запуска сервера Minecraft.

2. **Аргументы Java:**
   Укажите аргументы Java в текстовом поле "Аргументы Java". Добавьте аргумент `-XX:MaxPermSize=256M`, если возникает ошибка "Java Not Recognized".

3. **Выбор ядра:**
   Выберите серверное ядро из выпадающего списка. Доступные ядра динамически загружаются из файла конфигурации.

4. **Выбор версии:**
   Выберите версию Minecraft для выбранного ядра. Доступные версии загружаются на основе выбранного ядра.

5. **Открыть файлы сервера:**
   Нажмите кнопку "Открыть файлы сервера", чтобы перейти в директорию файлов сервера в проводнике.

6. **Запуск:**
   Нажмите кнопку "Запуск", чтобы запустить сервер Minecraft с указанными параметрами. Инструмент автоматически загрузит и настроит файлы сервера, если они отсутствуют.

---

## Особенности
- Удобный графический интерфейс для настройки параметров запуска сервера.
- Динамическая загрузка ядер и версий из файла конфигурации (`versions.json`).
- Автоматическая загрузка файлов сервера для выбранного ядра и версии.
- Подробные сообщения об ошибках.

---

## Заметки
- Убедитесь в правильности указания пути к исполняемому файлу Java.
- Настройте аргументы Java в соответствии с требованиями вашего сервера.

---

## Отказ от ответственности
Этот инструмент предоставляется в соответствии с [лицензией Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Рекомендуется ознакомиться с условиями лицензии и следовать им. Инструмент не имеет отношения к Mojang или Minecraft.

