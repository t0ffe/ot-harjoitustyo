# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjien on mahdollista pitää kirjaa myymistään tuotteista (haalarimerkeistään). 

## Käyttäjät

Alkuvaiheessa sovelluksella on ainoastaan yksi käyttäjärooli, _myyjä_. Myöhemmin sovellukseen saatetaan lisätä _opiskelija_, joka on merkkien ostaja.

## Käyttöliittymäluonnos

```
 .----------------.             .----------------.             .----------------. 
| .--------------. |           | .--------------. |           | .--------------. |
| |              | |           | |              | |           | |              | |
| |              | |           | |              | |   ---->   | |              | |
| |   Käyttäjän  | |           | |    Näkymä    | |           | |    Merkin    | |
| |    valinta   | |   ---->   | |   kaikista   | |           | |   muokkaus   | |
| |              | |           | |   merkeistä  | |   <----   | |              | |
| |              | |           | |              | |           | |              | |
| |              | |           | |              | |           | |              | |
| '--------------' |           | '--------------' |           | '--------------' |
 '----------------'             '----------------'             '----------------' 
```

## Perusversion tarjoama toiminnallisuus

### Ennen käyttäjän valintaa

- Käyttäjä voi valita olevansa myyjä (tai opiskelija)

### Käyttäjän valinnan jälkeen

- Käyttäjä näkee inventaarion merkeistä, joita tällä hetkellä on _varastossa_
  - Voit lisätä merkkejä bulkki määrä (+10 / +50 / +100 / jne.)
  - Voit "myydä" merkkejä (-1 / -5 / -10 / jne.)
- Jokaisella merkillä on hintansa, määrä ja kuva
- Sisältää kuvan ja merkin nimen
- Merkin muokkaus
  - Hinta
  - Kuva
  - Nimi


## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Merkkien järjestely erinäisiin järjestyksiin 
  - Milloin saapunut
  - Määrä
  - Hinta
  - Nimi
- Merkkien myyntihistoria

- Opiskelijan näkymä jossa:
  - Mitä merkkejä omistat
  - Mihin ne on kiinnitetty haalareissasi
    - mahd. generoitu linkki / kuva / teksti josta nämä käy ilmi, jonka voi jakaa
