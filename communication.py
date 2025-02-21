# dis_hla_lib/communication.py

class Communication:
    """Basisklasse für alle Kommunikationsarten."""
    
    def send(self, data):
        """Sende Daten (wird in Unterklassen überschrieben)."""
        raise NotImplementedError("Die send-Methode muss in der Unterklasse implementiert werden.")
    
    def receive(self):
        """Empfange Daten (wird in Unterklassen überschrieben)."""
        raise NotImplementedError("Die receive-Methode muss in der Unterklasse implementiert werden.")
