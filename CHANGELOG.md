# Лог изменений.
### Навигация:
##### {Версия} - {Билд}
* [0.7.3 - 167](https://github.com/SantaSpeen/BotClient.Python/blob/master/CHANGELOG.md#[05.08.2020] 0.7.3)

#### [05.08.2020] 0.7.3 
* Билд: 167

* **!FIXED**:
    * Бесконечное открытие настроек
    
* **!REFACTORING**:
    * `config.py` -> `json_access.py`:
        * Реструктурированны методы:
            * `open_config`
            * `save_config`
            
        * Добавлены методы:
            * `open_global_vars`
            * `save_global_vars`
            
* **!ADDED**:
    * Папка `jsons`, так как появилсь необходимость
    * Json файл - `global_vars`, для сохранения очень глобальных\Стойких переменных