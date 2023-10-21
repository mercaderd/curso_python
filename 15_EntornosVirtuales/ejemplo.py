from docxtpl import DocxTemplate

lista_confirmados = [
    {
        'nombre': 'Alberto',
        'apellido': 'García',
        'evento': '2ª Ed. Curso de python',
        'fecha': '11/12/2023',
        'herramientas': ['Ordenador portatil', 'Arduino', 'Cable USB']
    },
    {
        'nombre': 'Pedro',
        'apellido': 'Moreno',
        'evento': '2ª Ed. Curso de python',
        'fecha': '11/12/2023',
        'herramientas': ['Ordenador portatil', 'Raspberry Pi', 'Cable HDMI', 'Cable USB']
    },
    {
        'nombre': 'Jordi',
        'apellido': 'Molina',
        'evento': '2ª Ed. Curso de python',
        'fecha': '11/12/2023',
        'herramientas': ['Ordenador portatil', 'Arduino', 'Cable USB', 'Soldador']
    }

]
doc = DocxTemplate("./template.docx")
for i,confirmado in enumerate(lista_confirmados):
    doc.render(confirmado)
    doc.save(f"confirmacion{i+1}.docx")