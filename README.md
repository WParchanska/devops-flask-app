# DevOps Flask App

## Opis projektu
Jest to prosty projekt Flask przygotowany do celów **DevOps i CI/CD**.  
Zawiera endpoint `/health` oraz przykładowe testy uruchamiane w **GitHub Actions**.  
Projekt pokazuje jak:

- Budować i testować aplikację Python/Flask
- Uruchamiać CI/CD workflow w GitHub Actions
- Budować obraz Dockerowy dla aplikacji

---

## Endpoints

- `/` – zwraca komunikat powitalny, timestamp i hostname  
- `/health` – zwraca status `"OK"`  

---

## Uruchamianie lokalnie

```bash
# instalacja zależności
python -m pip install --upgrade pip
pip install flask requests pytest

# uruchomienie aplikacji
python app.py

Aplikacja działa domyślnie na http://127.0.0.1:5001

#Testy

Test /health można uruchomić lokalnie przez pytest:
pytest

#Docker

Budowa obrazu Dockerowego:
docker build -t devops-flask-app .
docker run -p 5000:5000 devops-flask-app

#CI/CD

Workflow GitHub Actions wykonuje:
1.Instalację Pythona i dependencies
2.Uruchomienie Flask w tle
3.Testy /health i pytest
4.Budowę obrazu Dockerowego
5.Workflow odpala się automatycznie przy push i pull request do gałęzi main.
