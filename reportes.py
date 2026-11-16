# reportes.py - RF11: Reportes diarios de raciones, ingresos, asistencia y merma

def reporte_diario(raciones_servidas, ingresos, asistentes, merma):
    print("REPORTE DIARIO DEL COMEDOR")
    print(f"- Raciones servidas: {raciones_servidas}")
    print(f"- Ingresos (S/): {ingresos:.2f}")
    print(f"- Asistencia: {asistentes}")
    print(f"- Merma (raciones): {merma}")


if __name__ == "__main__":
    reporte_diario(80, 320.00, 78, 2)
