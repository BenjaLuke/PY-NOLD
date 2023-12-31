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
        0: ["DIFICULTAD","","Movimiento","Objetos por turno","Puertas y ventanas cerradas","Sucesos","Conseguir madera","Reforzar con madera","Ataque","","Volver"],
        1: ["DIFICULTAT","","Moviment","Objectes per torn","Portes i finestres tancades","Successos","Aconseguir fusta","Reforçar amb fusta","Atac","","Tornar"],
        2: ["DIFFICULTY","","Movement","Objects per turn","Closed doors and windows","Events","Get wood","Reinforce with wood","Attack","","Back"],
        3: ["DIFICULTADE","","Movimento","Obxectos por turno","Portas e fiestras pechadas","Sucesos","Conseguir madeira","Reforzar con madeira","Ataque","","Volver"],
        4: ["ZAILTASUNA","","Mugimendua","Objektuak txandako","Itxita dauden ateak eta leihoak","Gertaerak","Zureganako egurra","Egurragaz bermatu","Atakea","","Atzera"],
        5: ["DIFFICULTY","","Movement","Objects per turn","Closed doors and windows","Events","Get wood","Reinforce with wood","Attack","","Back"],
        6: ["SCHWIERIGKEIT","","Bewegung","Objekte pro Runde","Geschlossene Türen und Fenster","Ereignisse","Holz bekommen","Mit Holz verstärken","Angriff","","Zurück"],
        7: ["DIFFICOLTÀ","","Movimento","Oggetti per turno","Porte e finestre chiuse","Eventi","Ottenere legno","Rinforzare con legno","Attacco","","Indietro"],
        8: ["DIFICULDADE","","Movimento","Objetos por turno","Portas e janelas fechadas","Eventos","Obter madeira","Reforçar com madeira","Ataque","","Voltar"],
        9: ["DIFICULTAD","","Movimiento","Objetos por turno","Puertas y ventanas cerradas","Sucesos","Conseguir madera","Reforzar con madera","Ataque","","Volver"],
        10: ["DIFICURTÁ","","Movimiento","Ohetos por turno","Puertah y ventanah cerrah","Sucesoh","Conseguí madera","Reforzá con madera","Ataque","","Volvé"],
        11: ["DIFICULTÁ","","Movimientu","Obxetos por tornu","Puertes y finestres zarrades","Sucesos","Conseguir madera","Reforzar con madera","Ataque","","Volver"],
        12: ["DIFICULTAT","","Moviment","Objectes per torn","Portes i finestres tancades","Successos","Aconseguir fusta","Reforçar amb fusta","Atac","","Tornar"]
    }
    
    return language_dict.get(language_code, [])

def languaje_cast(language_code):
    language_dict = {
        0: ["CRÉDITOS","","Idea y desarrollo: Benjamín Miguel","Gráficos: Jana Vera","Música: Jorge Varela","Testeo: ---","Traducción: Manuel Barroso","Agradecimientos: Luis Valbuena","","Volver"],
        1: ["CRÉDITS","","Idea i desenvolupament: Benjamín Miguel","Gràfics: Jana Vera","Música: Jorge Varela","Test: ---","Traducció: Manuel Barroso","Agraïments: Luis Valbuena","","Tornar"],
        2: ["CREDITS","","Idea and development: Benjamín Miguel","Graphics: Jana Vera","Music: Jorge Varela","Test: ---","Translation: Manuel Barroso","Thanks: Luis Valbuena","","Back"],
        3: ["CRÉDITOS","","Idea e desenvolvemento: Benjamín Miguel","Gráficos: Jana Vera","Música: Jorge Varela","Testeo: ---","Tradución: Manuel Barroso","Agradecementos: Luis Valbuena","","Volver"],
        4: ["KREDITUAK","","Idea eta garapena: Benjamín Miguel","Grafikoak: Jana Vera","Musika: Jorge Varela","Testeo: ---","Itzulpena: Manuel Barroso","Eskerrik asko: Luis Valbuena","","Atzera"],
        5: ["CRÉDITS","","Idea et développement: Benjamín Miguel","Graphiques: Jana Vera","Musique: Jorge Varela","Test: ---","Traduction: Manuel Barroso","Merci: Luis Valbuena","","Retour"],
        6: ["KREDITE","","Idee und Entwicklung: Benjamín Miguel","Grafiken: Jana Vera","Musik: Jorge Varela","Test: ---","Übersetzung: Manuel Barroso","Danke: Luis Valbuena","","Zurück"],
        7: ["CREDITI","","Idea e sviluppo: Benjamín Miguel","Grafica: Jana Vera","Musica: Jorge Varela","Test: ---","Traduzione: Manuel Barroso","Grazie: Luis Valbuena","","Indietro"],
        8: ["CRÉDITOS","","Idea e desenvolvimento: Benjamín Miguel","Gráficos: Jana Vera","Música: Jorge Varela","Testeo: ---","Tradução: Manuel Barroso","Agradecimentos: Luis Valbuena","","Voltar"],
        9: ["CRÉDITOS","","Idea y desarrollo: Benjamín Miguel","Gráficos: Jana Vera","Música: Jorge Varela","Testeo: ---","Traducción: Manuel Barroso","Agradecimientos: Luis Valbuena","","Volver"],
        10: ["CRÉDITOH","","Idea y desarrollo: Benjamín Miguel","Gráficoh: Jana Vera","Múhicah: Jorge Varela","Tehteo: ---","Tradución: Manuel Barroso","Tradución: ---","Agradecimientoh: Luis Valbuena","","Volvé"],
        11: ["CRÉDITOS","","Idea y desenvolvimientu: Benjamín Miguel","Gráficos: Jana Vera","Música: Jorge Varela","Testeo: ---","Traducción: Manuel Barroso","Agradecimientos: Luis Valbuena","","Volver"],
        12: ["CRÉDITS","","Idea i desenvolupament: Benjamín Miguel","Gràfics: Jana Vera","Música: Jorge Varela","Test: ---","Traducció: Manuel Barroso","Agraïments: Luis Valbuena","","Tornar"]
    }
    
    return language_dict.get(language_code, [])