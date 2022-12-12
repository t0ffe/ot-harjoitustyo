# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjien on mahdollista hallinnoida salasanojaan. 

## Käyttäjät

Soveluksesssa on vain yksi lokaali käyttäjä mutta useampi mode (gerenointi / vahvuus / selailu)

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

- Voit genroida salasanan
  - passphrase
  - password
  - oma
- parametrejä
  - pituus
  - sanojen määrä
  - mitä kirjainsettejä ([a-z], [A-Z], [0-9], [erikoismerkit], jne)

### Vahvuus

- Annat salasanan ja ohjelma kertoo nko se vahva
  - Pituus
  - merkit
  - toistuvuus(?)

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Salasanan vahvuuden paranatamis vinkkejä
- Salasanojen selaaminen
- salasana tiedoston salaus
