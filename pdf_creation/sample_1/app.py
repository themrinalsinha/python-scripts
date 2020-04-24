from os import getcwd
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(getcwd()))
template = env.get_template('myreport.html')

template_var = {
    'title': 'themrinalsinha.com',
    'national_pivot_table': 'just for testing...',
}

html_out = template.render(template_var)


from weasyprint import HTML

HTML(string=html_out).write_pdf('report.pdf')
