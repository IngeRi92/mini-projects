# Python Web Scraper (Poolik)

See projekt on lihtne Pythoniga kirjutatud töökuulutuste veebiskreiper, mis kogub Pythoniga seotud tööpakkumisi CV.ee lehelt ning salvestab need CSV faili.

## Hetkeseis

- Skript kasutab `requests` ja `BeautifulSoup` mooduleid (kuigi hetkel BeautifulSoup'i ei kasutata).
- Andmed saadakse CV.ee API kaudu ning salvestatakse faili `jobs.csv`.
- CSV failis on veerud: Title, Company, Publish Date, Expiration Date, Link.
- Kood on poolik ja arenduses – jätkan homme!

## Kasutamine

1. Veendu, et sul on vajalikud moodulid paigaldatud:
   ```bash
   pip install requests beautifulsoup4
   ```
2. Käivita skript:
   ```bash
   python webscraper.py
   ```
3. Tulemus salvestatakse faili `jobs.csv` samas kaustas.

## Tulevikuplaanid

- GUI
- Teised lehekülhed: CVKeskus ja Töötukassa

---

**Märkus:** See projekt on pooleli ja jätkan arendamist
