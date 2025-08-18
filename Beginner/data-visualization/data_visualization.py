import statistics


# Küsib kasutajalt arvulisi andmeid ja tagastab need nimekirjana
def get_data():
    while True:
        try:
            data = [
                float(x) for x in input("Sisesta andmed (nt 10, 20, 15): ").split(",")
            ]
            if len(data) > 1:
                return data
            print("Vaja vähemalt 2 arvu.")
        except ValueError:
            print("Vigane sisend.")


# Küsib kasutajalt siltide nimed või loob vaikimisi sildid
def get_labels(n):
    labels = input(f"Siltide nimed ({n} tk, vabatahtlik): ").split(",")
    labels = [l.strip() for l in labels if l.strip()]
    return labels + [f"Item {i+1}" for i in range(len(labels), n)]


# Arvutab ja tagastab andmete põhistatistika
def stats(data):
    try:
        mode = statistics.mode(data)
    except statistics.StatisticsError:
        mode = "-"
    return {
        "Kogus": len(data),
        "Summa": sum(data),
        "Keskmine": round(statistics.mean(data), 3),
        "Mediaan": statistics.median(data),
        "Mood": mode,
        "Miinimum": min(data),
        "Maksimum": max(data),
        "Vahemik": max(data) - min(data),
        "Standardhälve": round(statistics.stdev(data), 3) if len(data) > 1 else 0,
    }


# Joonistab andmetest lihtsa tulpdiagrammi tekstina
def bar_chart(data, labels):
    scale = 50 / max(data) if max(data) else 1
    for l, v in zip(labels, data):
        print(f"{l:>8}: {'█'*int(v*scale)} ({v})")


# Joonistab andmetest lihtsa histogrammi tekstina
def histogram(data, bins=5):
    mn, mx = min(data), max(data)
    if mn == mx:
        print("Kõik väärtused võrdsed.")
        return
    w = (mx - mn) / bins
    for i in range(bins):
        a, b = mn + i * w, mn + (i + 1) * w
        c = sum(a <= x < b or (i == bins - 1 and x == b) for x in data)
        print(f"{a:.1f}-{b:.1f}: {'▓'*c} ({c})")


""" Histogramm on diagramm, mis näitab, kui palju andmepunkte jääb erinevatesse väärtuste vahemikesse 
(ehk "ämbritesse" või "binnidesse").See aitab visuaalselt näha andmete jaotust ja sagedust, 
näiteks kas andmed on ühtlaselt jaotunud, kas on tippe või tühimikke. """


# Analüüsib andmete trendi (tõusev, langev, püsiv, muutlik)
def trend(data):
    inc = sum(data[i] > data[i - 1] for i in range(1, len(data)))
    dec = sum(data[i] < data[i - 1] for i in range(1, len(data)))
    if inc + dec == 0:
        t = "Püsiv"
    elif inc > dec * 1.5:
        t = "Tõusev"
    elif dec > inc * 1.5:
        t = "Langev"
    else:
        t = "Muutlik"
    print(f"Trend: {t} (↑{inc}, ↓{dec})")


# Peamine funktsioon, mis käivitab andmeanalüüsi programmi
def main():
    print("Lihtne andmeanalüüs")
    while True:
        data = get_data()
        labels = get_labels(len(data))
        s = stats(data)
        print("\nStatistika:", s)
        bar_chart(data, labels)
        histogram(data)
        trend(data)
        if input("Veel? (ei lõpetab): ").lower().startswith("e"):
            break


if __name__ == "__main__":
    main()
