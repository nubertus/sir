""" SIR-Modell mit Euler-Verfahren 
    André Nuber, April 2026 """

# Importe
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__": 
    # Startwerte
    t = 0           # Zeit in Tagen
    s = 997         # susceptibles
    i = 3           # infected
    r = 0           # removed
    n = s+i+r       # Anzahl Personen
    
    # Parameter
    a = 0.0004
    b = 0.04    
    dt = 1          # Zeitschritt in Tagen
    tmax = 100      # Ende der Simulation

    # csv-Datei öffnen
    dateiname = "ausgabe.csv"
    bildname = "sir.png"
    pd.DataFrame(columns=["t","S","I","R"]).to_csv(dateiname,index=False)
    
    # Zeitschritt
    while t<tmax: 
        # Ableitungen
        ds = -a*s*i
        di = a*s*i - b*i
        dr = b*i

        # Werte aktualisieren
        s += ds
        i += di
        r += dr
        t += dt

        # neue Werte in csv-Datei anhängen 
        pd.DataFrame([[t,s,i,r]], columns=["t","S","I","R"]).to_csv(dateiname,mode="a",header=False,index=False)
    
    # Daten graphisch darstellen
    data = pd.read_csv(dateiname)
    data.plot(
        x="t",                      # x-Werte
        y=["S","I","R"],            # y-Werte: drei Graphen
        lw="2",                     # "line width"
        xlim=[0,t],                 # Grenzen des Bereichs auf der x-Achse
        ylim=[0,n],                 # Grenzen des Bereichs auf der y-Achse
        grid=True,                  # Gitterlinien
        title=f"Entwicklung einer Pandemie für a={a}, b={b}",   # Titel
        xlabel="Zeit [d]",          # Beschriftung der x-Achse
        ylabel="Anzahl Personen",   # Beschriftung der y-Achse
        figsize=(12, 6),            # Grösse (in Zoll) der Abbildung 
    )
    plt.savefig(bildname)
    plt.show()  