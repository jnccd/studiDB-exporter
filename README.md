# studiDB-exporter
Converts StudiDB table to .csv

## Usage
1. Execute `git clone https://github.com/jnccd/studiDB-exporter && cd studiDB-exporter`
2. Go to your studiDB page
3. Navigate to 'Erworbene Leistungen'
4. Copy everything as text from the 'Leistungsnachweise' table
5. Paste the text into 'copied.txt' (Override the sample text)
6. Execute `pip install py-linq && python convert.py`
7. Open the 'data.csv' with LibreOffice or Excel
8. Make some nice graphs
