# reservas.py - RF4 y RF5: Reservas por turno y control de aforo
from config import AFORO_MAXIMO

reservas_por_turno = {}


def reservar(estudiante, turno):
    ocupados = reservas_por_turno.setdefault(turno, [])
    if len(ocupados) >= AFORO_MAXIMO:
        return False  # turno lleno
    ocupados.append(estudiante)
    return True


def cupos_disponibles(turno):
    return AFORO_MAXIMO - len(reservas_por_turno.get(turno, []))
