def languaje_menu(language_code):
    language_dict = {
        0: ["Jugar", "Dificultad", "Idioma: Castellano", "Créditos", "Salir"],
        1: ["Jugar", "Dificultat", "Idioma: Català", "Crédits", "Sortir"],
        2: ["Play", "Difficulty", "Language: English", "Credits", "Exit"],
        3: ["Xogar", "Dificultade", "Idioma: Galego", "Créditos", "Saír"],
        4: ["Jolastu", "Zailtasuna", "Hizkuntza: Euskera", "Kredituak", "Irten"],
        5: ["Jouer", "Difficulté", "Langue: Français", "Crédits", "Sortir"],
        6: ["Spielen", "Schwierigkeit", "Sprache: Deutsch", "Kredite", "Ausgang"],
        7: ["Giocare", "Difficoltà", "Lingua: Italiano", "Crediti", "Uscita"],
        8: ["Jogar", "Dificuldade", "Língua: Português", "Créditos", "Saída"],
        9:  ["Jugar", "Dificultat", "Idioma: Aragonés", "Créditos", "Salir"],
        10: ["Jugá", "Dificurtá", "Lengua: Ehtremeño", "Créditoh", "Salí"],
        11: ["Xugar", "Dificultá", "Llingua: Bable", "Créditos", "Salir"],
        12: ["Jugar", "Dificultat", "Idioma: Aranès", "Crédits", "Sortir"]
    }
    
    return language_dict.get(language_code, [])
    
def languaje_difficulty(language_code):
    language_dict = {
        0: ["DIFICULTAD","","Pasos extra","Puntos consumidos el coger","Puertas y ventanas cerradas","???","Puntos consumidos al conseguir madera","Puntos consumidos al clavar madera","Daño","","Volver"],
        1: ["DIFICULTAT","","Passos extra","Punts consumits al agafar","Portes i finestres tancades","???","Punts consumits al aconseguir fusta","Punts consumits al clavar fusta","Dany","","Tornar"],
        2: ["DIFFICULTY","","Extra steps","Points consumed when picking up","Closed doors and windows","???","Points consumed when getting wood","Points consumed when nailing wood","Damage","","Back"],
        3: ["DIFICULTADE","","Pasos extra","Puntos consumidos al coger","Portas e fiestras pechadas","???","Puntos consumidos ao conseguir madeira","Puntos consumidos ao cravar madeira","Dano","","Volver"],
        4: ["ZAILTASUNA","","Pauso gehiago","Puntuak kontsumituak","Ateak eta leihoak itxita","???","Puntuak kontsumituak egurra lortzean","Puntuak kontsumituak egurra marratzean","Minak","","Itzuli"],
        5: ["DIFFICULTÉ","","Pas supplémentaires","Points consommés en ramassant","Portes et fenêtres fermées","???","Points consommés en obtenant du bois","Points consommés en clouant du bois","Dommage","","Retour"],
        6: ["SCHWIERIGKEIT","","Extra Schritte","Punkte verbraucht beim Aufnehmen","Geschlossene Türen und Fenster","???","Punkte verbraucht beim Holz bekommen","Punkte verbraucht beim Holz nageln","Schaden","","Zurück"],
        7: ["DIFFICOLTÀ","","Passi extra","Punti consumati nel raccogliere","Porte e finestre chiuse","???","Punti consumati nel ottenere legno","Punti consumati nel inchiodare legno","Danno","","Indietro"],
        8: ["DIFICULDADE","","Passos extra","Pontos consumidos ao apanhar","Portas e janelas fechadas","???","Pontos consumidos ao conseguir madeira","Pontos consumidos ao pregar madeira","Dano","","Voltar"],
        9: ["DIFICULTAT","","Pasos extra","Puntos consumidos el coger","Puertas y ventanas cerradas","???","Puntos consumidos al conseguir madera","Puntos consumidos al clavar madera","Daño","","Volver"],
        10: ["DIFICULTÁ","","Pasus extra","Puntuos consumíus al coger","Puertas y ventanas cerrás","???","Puntuos consumíus al consiguir madera","Puntuos consumíus al clavar madera","Daño","","Volver"],
        11: ["DIFICULTÁ","","Pasos extra","Puntos consumidos el coger","Puertas y ventanas cerradas","???","Puntos consumidos al conseguir madera","Puntos consumidos al clavar madera","Daño","","Volver"],
        12: ["DIFICULTAT","","Pasos extra","Puntos consumidos el coger","Puertas y ventanas cerradas","???","Puntos consumidos al conseguir madera","Puntos consumidos al clavar madera","Daño","","Volver"]
    }
    
    return language_dict.get(language_code, [])
