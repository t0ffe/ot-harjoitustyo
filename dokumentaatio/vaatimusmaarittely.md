# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjien on mahdollista luoda ja hallinnoida salasanojaan sekä varmistaa niiden turvallisuus. 

## Käyttäjät

Sovelluksesssa on vain yksi lokaali käyttäjä mutta useampi mode (generointi / vahvuus / selailu)

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

### Generointi

- Voit generoida salasanan
  - passphrase
  - password
  - oma
- parametrejä
  - pituus
  - sanojen määrä
  - mitä kirjainsettejä ([a-z], [A-Z], [0-9], [erikoismerkit], jne)

### Vahvuus

- Annat salasanan ja ohjelma kertoo onko se vahva
  - Pituus
  - merkit
  - toistuvuus(?)

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Salasanan vahvuuden parantamisvinkkejä
- Salasanojen selaaminen
- Salasanojen ryhmittely
- Salasanatiedoston salaus
