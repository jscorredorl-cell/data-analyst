from pathlib import Path

RESOURCES_DIR = Path(__file__).resolve().parent.parent / "resources"

FILES = {
    "baloto.csv": (
        "Resultados de los sorteos del Baloto, la lotería de Colombia, entre abril de 2017 "
        "y marzo de 2023 (603 sorteos). Cada fila es un sorteo con su fecha, los cinco "
        "números de las balotas (C1 a C5) y la superbalota (SB)."
    ),
    "covid_19_clean_complete.csv": (
        "Reporte diario de COVID-19 por país y provincia, desde el 22 de enero hasta el "
        "27 de julio de 2020. Cada fila trae los casos confirmados, muertes, recuperados y "
        "casos activos acumulados hasta esa fecha, junto con la región de la OMS."
    ),
}

FILES_CONTEXT = "\n".join(
    f"- {RESOURCES_DIR / name}\n  {description}" for name, description in FILES.items()
)

SYSTEM_PROMPT = f"""\
Eres un analista de datos. Tu trabajo es responder las preguntas del usuario analizando \
los archivos de datos disponibles.

Archivos disponibles:
{FILES_CONTEXT}
"""
