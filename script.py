from docxtpl import DocxTemplate
import pandas as pd

df = pd.read_excel("datos.xlsx")

for index, row in df.iterrows():
    alumno = row["alumno"]
    docente = row["docente"]
    curso = row["curso"]

    doc = DocxTemplate("plantilla.docx")
    context = { 'alumno' : alumno, 'docente' : docente, 'curso' : curso}

    doc.render(context)
    doc.save(f"C:/Users/Jonathan/Desktop/3reTrimestre/{alumno}.docx")
