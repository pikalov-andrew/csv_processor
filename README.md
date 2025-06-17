# CSV Processor

CSV-процессор — это инструмент для обработки CSV-файлов с поддержкой фильтрации, 
агрегации и сортировки данных. Представлена CLI-интерфейсом с обработкой аргументов коммандной строки.

Программа:
* Следует SOLID и паттернам проектирования.
* Использует модульную архитектуру и расширяемость.
* Покрыта тестами ≥80%.
* Обеспечивает робастную обработку ошибок и читаемость кода.

## Установка

### 1. Клонируйте репозиторий
```bash  
    git clone https://github.com/pikalov-andrew/csv_processor.git   
    cd csv_processor
```
### 2. Создайте виртуальное окружение
```bash  
python -m venv .venv  
source .venv/bin/activate  # Linux/macOS  
# или  
.venv\Scripts\activate     # Windows
```
### 3. Установите зависимости
```bash 
pip install -r requirements.txt  
```
## Работа приложения
Пример работы команд:
```commandline
python main.py --file products.csv
python main.py -f products.csv -w price>500
python main.py -f products.csv -w price>500 -a rating=avg
python main.py -f products.csv -w price<1000 -o rating=desc
```
Пример обработки ошибок:
```commandline
python main.py -f products.csv -a rating=avg -o rating=desc
python main.py -f products.csv -w price*500
python main.py -f products.csv -w price>9999 -a price=max
python main.py -f products.csv -a rating=mean
```
Покрытие кода тестами:
```bash
pytest --cov=. --cov-report term-missing
```