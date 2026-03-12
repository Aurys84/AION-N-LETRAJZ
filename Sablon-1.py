import webbrowser
import os

# Aion Labor - Interaktív Önéletrajz Generátor
def generalj_es_nyisd_meg():
    print("--- Aion Mátrix Önéletrajz-űrlap ---")
    
    # Adatbekérés (űrlap módra)
    nev = input("Teljes név: ")
    cim = input("Lakcím: ")
    tel = input("Telefonszám: ")
    email = input("E-mail cím: ")
    bemutatkozas = input("Rövid bemutatkozás: ")
    tapasztalat = input("Munkatapasztalat (pl. Cég, dátum, pozíció): ")
    tanulmanyok = input("Tanulmányok (iskola, szak): ")
    keszsegek = input("Készségek (vesszővel elválasztva): ")

    # A dizájn (Nóra és Iringó stílusa alapján)
    html_tartalom = f"""
    <!DOCTYPE html>
    <html lang="hu">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; margin: 0; color: #333; }}
            .oldalsav {{ background-color: #007bb5; color: white; width: 30%; padding: 30px; min-height: 100vh; }}
            .fo-tartalom {{ width: 70%; padding: 50px; background-color: #f9f9f9; }}
            h1 {{ font-size: 40px; margin-bottom: 5px; color: #222; text-transform: uppercase; }}
            h2 {{ border-bottom: 2px solid #fff; padding-bottom: 5px; font-size: 18px; }}
            .szekcio-cim {{ color: #007bb5; border-bottom: 2px solid #007bb5; padding-bottom: 5px; margin-top: 30px; }}
            p {{ line-height: 1.6; }}
        </style>
    </head>
    <body>
        <div class="oldalsav">
            <h2>KÉSZSÉGEK</h2>
            <p>{keszsegek}</p>
            <h2>ELÉRHETŐSÉG</h2>
            <p>📍 {cim}<br>📞 {tel}<br>✉️ {email}</p>
        </div>
        <div class="fo-tartalom">
            <h1>{nev}</h1>
            <h3 class="szekcio-cim">BEMUTATKOZÁS</h3>
            <p>{bemutatkozas}</p>
            <h3 class="szekcio-cim">MUNKATAPASZTALAT</h3>
            <p>{tapasztalat}</p>
            <h3 class="szekcio-cim">TANULMÁNYOK</h3>
            <p>{tanulmanyok}</p>
        </div>
    </body>
    </html>
    """

    fajlnev = "Aion_Oneletrajz.html"
    with open(fajlnev, "w", encoding="utf-8") as f:
        f.write(html_tartalom)
    
    # Ez a rész nyitja meg neked automatikusan!
    eleresi_ut = os.path.abspath(fajlnev)
    print(f"\n✅ Kész! A fájl mentve: {eleresi_ut}")
    print(f"🔗 Nyisd meg itt: file://{eleresi_ut}")
    
    webbrowser.open("file://" + eleresi_ut)

if __name__ == "__main__":
    generalj_es_nyisd_meg()