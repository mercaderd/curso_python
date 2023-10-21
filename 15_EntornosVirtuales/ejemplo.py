from docxtpl import DocxTemplate

lista_confirmados = [
    {
        'nombre': 'Alberto',
        'apellido': 'García',
        'evento': '2ª Ed. Curso de python',
        'fecha': '11/12/2023'
    },
    {
        'nombre': 'Pedro',
        'apellido': 'Moreno',
        'evento': '2ª Ed. Curso de python',
        'fecha': '11/12/2023'
    },
    {
        'nombre': 'Jordi',
        'apellido': 'Molina',
        'evento': '2ª Ed. Curso de python',
        'fecha': '11/12/2023'
    },

]
doc = DocxTemplate("./template.docx")
for i,confirmado in enumerate(lista_confirmados):
    doc.render(confirmado)
    doc.save(f"confirmacion{i+1}.docx")