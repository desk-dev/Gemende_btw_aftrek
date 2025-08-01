def gemengde_btw():
    """Bereken de niet-aftrekbare btw bij gemengde btw-aftrek (vrijgestelde en belaste omzet)"""
    try:
        kosten = float(input("Wat waren je kosten exclusief btw? € "))
        totale_omzet = float(input("Wat was je totale omzet exclusief btw? € "))
        vrijgestelde_omzet = float(input("Hoeveel daarvan was vrijgesteld? € "))
        
        if totale_omzet == 0:
            print("De totale omzet mag niet nul zijn.")
            return

        btw = kosten * 0.21
        correctie = btw * (vrijgestelde_omzet / totale_omzet)
        aftrekbare_btw = btw - correctie

        print("\n--- Samenvatting ---")
        print(f"Totale kosten: €{kosten:.2f}")
        print(f"Totale omzet: €{totale_omzet:.2f}")
        print(f"Vrijgestelde omzet: €{vrijgestelde_omzet:.2f}")
        print(f"Totaal berekende btw over kosten: €{btw:.2f}")
        print(f"Niet-aftrekbare btw (correctie): €{correctie:.2f}")
        print(f"Aftrekbare btw: €{aftrekbare_btw:.2f}")
    except ValueError:
        print("Voer alleen getallen in, gebruik een punt voor decimalen (bijv. 1000.50).")

gemengde_btw()
