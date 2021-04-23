

<p> Programmering 1 - Python &ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Kokchun Giang </p>
<hr>
<br>

# Dataanalysprojekt 

Vi lever i en pågående Covid-19 pandemi i världen som skördat liv och helt förändrat vår vardag och levnadsvanor. Ni har från och med 2020 fått mängder av information från nyheterna kring smittotal, dödstal med mera. Med den insamlade datan har FHM, nyhetskanaler med flera gjort olika urval kring vad som ska presenteras. 

## Data

Nu ska du använda dig av datan och själv utforska, visualisera och presentera relevant information. Skapa ett konto och ladda ned datan från [Kaggle](https://www.kaggle.com/vascodegama/sweden-covid19-data).

## Uppvärmningsuppgifter

Följande uppgifter är hjälp för att ni ska komma igång med att utforska datan och dess möjligheter.  

<details open>

<summary>Uppvärmningsupgifter </summary>

1. Läs in filen "National_Daily_Deaths.csv" med hjälpa av modulen Pandas.
2. Använd matplotlib och rita en graf över antalet döda i Covid-19 i Sverige per dag. 
3. Ange lämpliga titlar på x-axeln, y-axeln och rubriken.

</details>

## Uppgift
Uppgiften ska göras individuellt, men du får fråga om hjälp och diskutera med andra. Följande delar ingår i uppgiften:

1. [Planering](#1.-planering)
2. [Dataanalys](#2.-dataanalys)
3. [Utvärdering](#3.-utvärdering)


### 1. Planering

Innan du får börjar koda måste du göra en <b>planering</b>. Planeringen ska godkännas av mig, och sedan får du sätta igång med själva koden. Ett tips är att manuellt titta igenom datan och fundera på vad som kan vara intressant att visualisera.

När du kodar måste du inte följa din planering till punkt och pricka, om du inser att du behöver göra något på ett annat sätt. Berätta istället i din utvärdering <b>vad</b> du gjort annorlunda och <b>varför</b>.

<details open>

<summary>Frågor att besvara </summary>
<br>

<ol type="a">
  <li><b> Struktur </b>- beskriv övergripande hur ditt program fungerar, antingen med <b>pseudokod</b> eller med <b>flödesschema</b>. 
  <br><br>

  Exempel på pseudokod för ett simuleringsprogram för att simulera &pi;/4: 
  ```md
    1. Simulera 10000 slumpmässiga punkter mellan punkter (x,y) mellan -1 och 1.

    2. Beräkna avståndet mellan varje punkt och origo.

    3. Om avståndet är lägre än 1, räkna punkten som inne i cirkeln, annars ute.

    4. Beräkna andelen som hamnar inne i cirkeln genom att dividera antalet inne med totalt antal simulerade punkter. 
  ```

  Motsvarande exempel med flödesschema: 

![alt text](https://github.com/NTI-Kronhus/TE19CD-PRRPRR01/blob/master/assets/Simulera_pi_FC.png?raw=true "Flow chart")

  Använd [diagrams.net](https://www.diagrams.net/) och logga in med ditt skolkonto för att skapa ett flödesschema. 
  </li>
  <li>Vad tänker du undersöka?</li>
  <li>Hur ska resultatet presenteras? Vilka typer av grafer och varför? </li>
  <li>Vilka variabler och funktioner behöver du och varför?</li>
  <li>Vilka kontrollstrukturer (if-sats, loopar, mm) behöver du och varför?</li>
  <li>Vilka datastrukturer behöver du och varför?</li>
</ol>

</details>

### 2. Dataanalys

När er planering är godkänd får ni börja skriva kod. 
<details open>
<summary>För <b>godkänt</b> krävs följande:</summary>

- Godkänd planering
- Läsa in minst två olika dataset
- Rita minst två olika typer av grafer (ex linjediagram, cirkeldiagram) med matplotlib
- Graferna ska ha relevanta titlar, etiketter på axlarna, legends mm  
- Kommenterad kod med relevanta kommentarer
- Ej plagierad kod (vissa mindre kodsnutt är okej givet att du källhänvisar och kan motivera att du förstått koden)
- Godkänd utvärdering
</details>

<details open>
<summary>För <b>högre</b> än godkänt krävs även att allt eller vissa av följande är uppfyllda:</summary>

- Kommenterad kod med korrekt användning av datavetenskaplig terminologi*
- Använda funktioner för att strukturera upp och återanvända kod*
- Variabelnamn ska vara beskrivande*
- Skapa minst fyra unika diagram som visualiserar datan* 
- Använda subplots för att visualisera flera diagram på ett figure-fönster (subplot)
- Använda plotly express eller plotly graph objects för att rita grafer
- Använda plotly dash för att skapa en dashboard
- Använda dash bootstrap components för att ge stil till din dashboard
- Lägg till interaktiva delar i din dashboard, ex att låta användaren få välja vad som ska visualiseras. (svår)


De punkter markerade med asterisker * är obligatoriska för högre betyg än godkänt.
</details>

### 3. Utvärdering

<details open>

<summary>Utvärderingen görs i form av en videologg där du spelar in din skärm och gör följande punkter:</summary>

<ol type="a">
  <li>Beskriv vad du har undersökt och dina resultat</li>
  <li>Beskriv detaljerat din kod och hur den fungerar. I beskrivningen är det viktigt att motivera varför du kodat som du gjort.</li>
  <li>Har du tagit någon kodsnutt från någon annan, ska du <b>källhänvisa</b> och visa att du förstått den.</li>
  <li>Blev din kod precis som du planerade eller gjorde du avvikelser? Isåfall vilka avvikelser gjorde du och varför?</li>
  <li>Hur var arbetsprocessen för projektet?</li>

</details>