# dis_hla_lib/communication_manager.py
from dis_communication import DISCommunication
from hla_communication import HLACommunication

class CommunicationManager:
    """Manager für die Kommunikation, der DIS oder HLA verwendet."""

    def __init__(self, comm_type="DIS", host="localhost", port=3000):
        """Initialisierung der Kommunikation basierend auf dem gewählten Typ."""
        self.comm_type = comm_type
        if comm_type == "DIS":
            self.communication = DISCommunication(host=host, port=port)
        elif comm_type == "HLA":
            self.communication = HLACommunication(host=host, port=port)
        else:
            raise ValueError(f"Unbekannter Kommunikationstyp: {comm_type}")
    
    def send_scenario_data(self, data):
        """Sende Szenario-Daten (DIS oder HLA)."""
        self.communication.send(data)
    
    def receive_scenario_data(self):
        """Empfange Szenario-Daten (DIS oder HLA)."""
        return self.communication.receive()

    def set_port(self, port):
        """Setze den Port für die Kommunikation."""
        self.communication.set_port(port)
    
    def close(self):
        """Schließe die Verbindung."""
        self.communication.close()
