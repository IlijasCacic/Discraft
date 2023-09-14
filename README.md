# Discraft

Kratki opis projekta
Web servisa koji olakšava upravljanje rasporedom događanja ili sastanaka za korisnike na platformi.

Osnovne funkcionalnosti uključuju:
- Unos imena, datuma, vremena, opisa i organizatora događaja.
- Uređivanje imena, datuma, vremena, opisa i organizatora upisanog događaja.
- Brisanje događaja.

### Pokretanje aplikacije lokalno ###
---
Preuzimanje zip datoteke sa github-a

raspakiranje sadržaja

Otvaranje terminala

Izrada docker image-a upisivanjem naredbe: "docker build -t event-service ."

Pokretanje kontejnera sa naredbom: "docker run -d -p 5000:5000 event-service"

Otvaranje preglednika na adresi: http://localhost:5000/
