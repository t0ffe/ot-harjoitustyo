import uuid


class Merkki:

    def __init__(self, nimi, maara, hinta, kuva, merkki_id=None):

        self.nimi = nimi
        self.maara = maara
        self.hinta = hinta
        self.kuva = kuva
        self.id = merkki_id or str(uuid.uuid4())
