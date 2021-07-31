from jinja2 import Template

passengers = {
    "header": ["Name", "Contact", "Email", "Gender"],
    "rows": [
        ["Aijaz", "03472877702", "muhammadaijaz76@gmail.com", "Male" ],
        ["Aijaz", "03472877702", "muhammadaijaz76@gmail.com", "Male" ],
        ["Aijaz", "03472877702", "muhammadaijaz76@gmail.com", "Male" ],
        ["Aijaz", "03472877702", "muhammadaijaz76@gmail.com", "Male" ]
        ]
}
def process_template():
    with open("./templates/template.html", 'r') as test_template:
        temp = Template(test_template.read())

    result = temp.render(name="Aijaz Abbasi", passengers=passengers)
    print("result", result)

    with open('./output/output.html', 'w') as output_file:
        output_file.write(result)
if __name__ == '__main__':
    process_template()

