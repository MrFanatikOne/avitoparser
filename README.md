# Авито парсер

## Данный парсер выгружает: _имена, адреса, номера и ссылки на товары/услуги_ на площадке авито

### Для работы данного скрипта надо:
##### * Установить пакеты selenium командой - pip install selenium
##### * Скачать cromedriver под свою версию google Chrome 
##### * Создать файл login.txt, в котором будет записаны логин и пароль от своего аккаунта Авито

## При запуске скрипта в консоле спрашивается:
#### * Поисковый запрос на авито
#### * Количество обробатываемых запросов 
#### * Город в которому будет происходить поиск и выгрузка(* для поиска по всей России)

### Результат работы будет записан в файл вида '_|Введенный запрос|_ _|Город в котором происходит поиск|_ _|Количесво обробатываемых запросов|_'.csv
