# dis_hla_lib/dis_communication.py
from dis_hla_lib.communication import Communication


class DISCommunication(Communication):
    """DIS-Kommunikation mit pyDIS, erbt von Communication."""
    
    def __init__(self, host='localhost', port=3000):
        """
        Initialisiere die DIS-Verbindung.
        :param host: Host-Adresse des DIS-Servers (z.B. 'localhost').
        :param port: Port-Nummer des DIS-Servers (Standard ist 3000).
        """
        self.host = host
        self.port = port
        
        # Verbindung mit pyDIS herstellen (hier für UDP)
        self.dis_socket = pydis.DisSocket(host=self.host, port=self.port)
        self.dis_socket.open()

    def send(self, data):
        """
        Sende DIS-Daten.
        :param data: Die zu sendenden Daten.
        """
        # Hier nehmen wir an, dass `data` ein einfaches DIS-PDU (Protocol Data Unit) ist.
        print(f"Sende über DIS: {data}")
        
        # Beispiel: Senden einer einfachen Nachricht (PDU).
        # Die genaue Implementierung hängt davon ab, welche Art von PDU du senden möchtest.
        self.dis_socket.send(data)

    def receive(self):
        """
        Empfange DIS-Daten.
        :return: Die empfangenen Daten.
        """
        print("Empfange DIS-Daten...")
        data = self.dis_socket.receive()
        return data

    def close(self):
        """Schließe die Verbindung."""
        self.dis_socket.close()

    def set_port(self, port):
        """Setze den Port dynamisch."""
        self.port = port
        self.dis_socket.close()  # Schließe die alte Verbindung
        self.dis_socket = pydis.DisSocket(host=self.host, port=self.port)  # Neue Verbindung mit dem neuen Port
        self.dis_socket.open()
