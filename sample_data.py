from models import TechnicalManual


def load_sample_manuals():
    return [
        TechnicalManual("AMM", "29", 3, "A320-NEO", "Compliant"),
        TechnicalManual("IPC", "29", 2, "A320-NEO", "Compliant"),
        TechnicalManual("TSM", "32", 5, "A320-CEO", "Compliant"),
        TechnicalManual("AMM", "32", 1, "A320-CEO", "Compliant"),
    ]
