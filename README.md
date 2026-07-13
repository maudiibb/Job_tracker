# Job Tracker

Ett litet fullstack-projekt för att hålla koll på jobbansökningar — vilka företag jag har kontaktat, vilka roller jag sökt, status på varje ansökan, och en snabb "spara jobbannons"-funktion via en bookmarklet.

Byggt som portfolioprojekt sommaren 2026, för att träna på att koppla ihop ett riktigt backend (FastAPI + SQLAlchemy) med ett rent vanilla JS-frontend, utan ramverk.

## Skärmdumpar

**Tabellvy med företag och nästlade ansökningar:**

![Tabellvy](screenshots/table-view.png)

**Formulär ifyllt via bookmarkleten:**

![Ifyllt formulär](screenshots/form-filled.png)

## Funktioner

- **Full CRUD** för både företag och ansökningar (skapa, läsa, uppdatera, ta bort)
- **Nästlad data** – varje företag visar sina kopplade ansökningar direkt i tabellen
- **Duplicate detection** – hindrar dubbletter på exakt samma jobb-URL (hård spärr), varnar vid samma företag + samma roll (mjuk varning)
- **Sök och filter** – fritextsök på företag/roll/källa samt filtrering på status, allt client-side utan extra serveranrop
- **Bookmarklet-capture** – ett bokmärke som, när man klickar på det från en jobbannons, öppnar trackern i en ny flik med länk och dagens datum redan ifyllda i formuläret

## Tech stack

- **Backend:** FastAPI, SQLAlchemy, SQLite
- **Frontend:** Vanilla JavaScript, HTML — ingen ramverk
- **Verktyg:** Swagger/OpenAPI för API-testning under utveckling

## Arkitektur

```
app/
├── main.py         # API-endpoints (10 st) för companies och applications
├── models.py       # SQLAlchemy-modeller
├── schemas.py       # Pydantic-scheman för request/response, inkl. nästlad CompanyWithApplications
├── crud.py         # Databaslogik, inkl. duplicate/similar-kontroller
├── database.py     # DB-uppkoppling och session
└── static/
    └── index.html  # Hela frontend: tabell, formulär, sök/filter, bookmarklet-hantering
```

**Hur duplicate detection funkar:** Vid ny ansökan kollar `crud.py` först om exakt samma `job_url` redan finns (då avbryts skapandet med ett 409-fel). Finns ingen exakt träff kollas istället om samma företag redan har en ansökan med samma roll-titel — i så fall skapas ansökan ändå, men med en varning tillbaka till frontend.

**Hur bookmarkleten funkar:** Ett litet `javascript:`-snippet sparat som bokmärke läser av `window.location.href` (jobbannonsens URL) och dagens datum, och öppnar trackern i en ny flik med de värdena som query-parametrar. `index.html` läser av parametrarna vid sidladdning och fyller i fälten `job_url` och `applied_date` automatiskt.

## Vad jag lärde mig

Det här var första gången jag byggde ett frontend från grunden i vanilla JS efter att mest ha jobbat i Python/SQL tidigare. Sånt som DOM-manipulation, event listeners och att hålla koll på state (som `editingApplicationId`) utan ett ramverk gav en bättre känsla för vad ramverk som React egentligen löser åt en. Duplicate detection-logiken var också ett bra sätt att öva på att tänka igenom edge cases innan man kodar, inte bara "happy path".

## Köra lokalt

1. Klona repot och gå in i mappen
2. Skapa och aktivera en virtuell miljö
3. Installera beroenden: `pip install -r requirements.txt`
4. Starta servern: `uvicorn app.main:app --reload`
5. Öppna `http://localhost:8000/static/index.html`
