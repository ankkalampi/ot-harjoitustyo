```mermaid
classDiagram

Pelinappula "1" --> "1" Pelaaja 
Pelaaja "1" --> "0..*" Kiinteisto
Katu "1" --> Kiinteisto
Laitos "1" --> Kiinteisto
Asema "1" --> Kiinteisto
Pelilauta "1" --> "40" Ruutu
Pelinappula "1" --> "1" Ruutu
Pelilauta "1" --> "2..8" Pelinappula
Pelilauta "1" --> "2" Noppa
Ruutu <|-- Aloitusruutu
Ruutu <|-- Katu
Ruutu <|-- Laitos
Ruutu <|-- Sattuma
Ruutu <|-- Yhteismaa
Ruutu <|-- Vankila
Ruutu <|-- Asema
Kortti <|-- YhteismaaKortti
Kortti <|-- SattumaKortti

 class Kiinteisto{
     +int hinta

     +osta()
     +myy()
     +kiinnita()
 }
   

 class Noppa{
  +heita()
 }

 class Pelaaja{

  +int rahat
  +Pelaaja seuraavaPelaaja
 
 }

 class Pelilauta{
  int aloitusruutu
  int vankilaruutu

  +aloitaPeli()
  +siirraVuoro()
 }

 class Ruutu{
  +Ruutu seuraavaruutu
  +int index
  +teeToiminto()
 }

 class Pelinappula{

  +liiku(maara)
  +suoritaVuoro()
  +lopetaVuoro()
 }

 class Aloitusruutu

 class Vankila

 class Asema

 class Laitos

 class Sattuma

 class Yhteismaa

 class Kortti{
  +teeToiminto(Pelaaja)
 }

 class YhteismaaKortti

 class SattumaKortti

 class Katu{
  +String nimi
  +int talojenMaara
  +int talonHinta

  
  +rakennaTalo()
  +myyTalo()
 }

 ```
