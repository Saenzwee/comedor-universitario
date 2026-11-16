# pagos.py - RF6 y RF7: Tarifa, registro de pago y ticket con código QR
from config import PRECIO_RACION

pagos_registrados = []


def calcular_tarifa(es_becario):
    """Los becarios no pagan; los no becarios pagan el precio de la ración."""
    return 0.0 if es_becario else PRECIO_RACION


def registrar_pago(estudiante, es_becario):
    monto = calcular_tarifa(es_becario)
    pagos_registrados.append({"estudiante": estudiante, "monto": monto})
    return monto


def emitir_ticket(estudiante, turno):
    codigo_qr = f"QR-{estudiante}-{turno}"
    return {"estudiante": estudiante, "turno": turno, "codigo_qr": codigo_qr, "usado": False}
