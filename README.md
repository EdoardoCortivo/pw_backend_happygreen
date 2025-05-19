HappyGreen Backend API
<div align="center">
  <img src="https://via.placeholder.com/150" alt="HappyGreen Logo" width="150" height="150">
  <h3>Sostenibilità a portata di click</h3>
</div>
📋 Indice

Descrizione del Progetto
Funzionalità
Requisiti di Sistema
Installazione

Windows
MacOS
Linux


Struttura del Progetto
REST API Endpoints
Tecnologie Utilizzate
Team di Sviluppo
Licenza

📝 Descrizione del Progetto
HappyGreen è un'applicazione mobile Android progettata per sensibilizzare gli utenti sul tema della sostenibilità ambientale attraverso il riconoscimento di oggetti, quiz educativi e condivisione di informazioni ecologiche. Questo repository contiene il backend dell'applicazione, sviluppato con Django REST Framework.
Il progetto è stato realizzato come parte del corso TPSIT (Tecnologie e Progettazione di Sistemi Informatici e di Telecomunicazioni) per offrire agli studenti uno strumento divertente e interattivo per imparare a prendersi cura dell'ambiente.
🔍 Funzionalità
Il backend supporta le seguenti funzionalità:

👤 Gestione Utenti: Registrazione e autenticazione tramite JWT
👥 Gruppi di Amici: Creazione e gestione di gruppi con diversi ruoli utente
📱 Condivisione Contenuti: Post, commenti e geolocalizzazione
📷 Riconoscimento Oggetti: Archiviazione di oggetti scansionati con ML Kit
❓ Quiz e Sfide: Quiz educativi sulla sostenibilità con sistema di punteggio
🏆 Badge e Premi: Sistema di ricompense per le attività ecologiche
🔍 Scanner Barcode: Database di prodotti eco-friendly e alternative sostenibili
♻️ Classificazione Rifiuti: Guida interattiva alla raccolta differenziata

💻 Requisiti di Sistema

Python 3.8+
MySQL 8.0+ o MariaDB 10.5+
Django 5.0+
Django REST Framework 3.14+
Ambiente virtuale Python (venv o virtualenv)

🚀 Installazione
Windows

Clona il repository:
bashgit clone https://github.com/tuousername/backend-happygreen.git
cd backend-happygreen

Crea un ambiente virtuale:
bashpython -m venv .venv
.venv\Scripts\activate

Installa le dipendenze:
bashpip install -r requirements.txt

Configura il database MySQL:
bashmysql -u root -p
CREATE DATABASE pwhappygreen_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
exit

Esegui le migrazioni:
bashpython manage.py migrate

Avvia il server:
bashpython manage.py runserver


MacOS

Clona il repository:
bashgit clone https://github.com/tuousername/backend-happygreen.git
cd backend-happygreen

Crea un ambiente virtuale:
bashpython3 -m venv .venv
source .venv/bin/activate

Installa le dipendenze:
bashpip install -r requirements.txt

Configura il database MySQL:
bashmysql -u root -p
CREATE DATABASE pwhappygreen_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
exit

Esegui le migrazioni:
bashpython manage.py migrate

Avvia il server:
bashpython manage.py runserver


Linux

Clona il repository:
bashgit clone https://github.com/tuousername/backend-happygreen.git
cd backend-happygreen

Crea un ambiente virtuale:
bashpython3 -m venv .venv
source .venv/bin/activate

Installa le dipendenze:
bashpip install -r requirements.txt

Configura il database MySQL:
bashsudo mysql -u root -p
CREATE DATABASE pwhappygreen_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
exit

Esegui le migrazioni:
bashpython manage.py migrate

Avvia il server:
bashpython manage.py runserver


📁 Struttura del Progetto
backend-happygreen/
├── backend_happygreen/      # Directory principale del progetto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Configurazioni del progetto
│   ├── urls.py              # URL mapper principale
│   └── wsgi.py
├── happygreen/              # App principale
│   ├── __init__.py
│   ├── admin.py             # Configurazione admin panel
│   ├── apps.py
│   ├── models.py            # Modelli del database
│   ├── serializers.py       # Serializzatori REST
│   ├── tests.py             # Test unitari e API
│   ├── urls.py              # URL della app
│   └── views.py             # Logic views e API endpoints
├── templates/               # Template HTML
│   └── index.html           # Homepage API
├── media/                   # File caricati dagli utenti
├── .venv/                   # Ambiente virtuale Python
├── manage.py                # Script di gestione Django
└── requirements.txt         # Dipendenze Python
🌐 REST API Endpoints
L'API offre i seguenti endpoint:

Autenticazione

POST /token/: Ottieni token JWT
POST /token/refresh/: Rinnova token JWT


Utenti

GET /users/: Lista utenti
POST /users/: Crea nuovo utente
GET /users/{id}/: Dettagli utente
PUT /users/{id}/: Aggiorna utente
DELETE /users/{id}/: Elimina utente


Gruppi

GET /groups/: Lista gruppi
POST /groups/: Crea nuovo gruppo
GET /groups/{id}/: Dettagli gruppo
PUT /groups/{id}/: Aggiorna gruppo
DELETE /groups/{id}/: Elimina gruppo


Post e Commenti

GET /posts/: Lista post
POST /posts/: Crea nuovo post
GET /posts/{id}/: Dettagli post
GET /comments/: Lista commenti
POST /comments/: Crea nuovo commento


Oggetti Scansionati

GET /scanned-objects/: Lista oggetti scansionati
POST /scanned-objects/: Aggiungi oggetto scansionato


Quiz e Badge

GET /quizzes/: Lista quiz
GET /badges/: Lista badge


Prodotti Eco-Friendly

GET /eco-products/: Lista prodotti eco
GET /eco-products/{barcode}/: Cerca prodotto per barcode


Classificazione Rifiuti

GET /waste-classifications/: Guida alla raccolta differenziata



🛠 Tecnologie Utilizzate

Backend: Django, Django REST Framework, JWT Authentication
Database: MySQL/MariaDB
Deployment: ngrok per test da dispositivi mobili
Testing: Django TestCase, APITestCase

👨‍💻 Team di Sviluppo
Progetto realizzato da:

Nome Cognome
Nome Cognome
Nome Cognome

📄 Licenza
Questo progetto è distribuito con licenza MIT. Vedere il file LICENSE per maggiori dettagli.
