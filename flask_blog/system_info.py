import platform
import cpuinfo
import socket
import os
from flask import Flask, render_template

app = Flask(__name__)

class SystemInfo:
    # Création d'une méthode __init__ sans argument
    def __init__(self):
        self.system = platform.system()
        self.processor = platform.processor()
        self.architecture = platform.architecture()
        self.hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.hostname)
        self.cpu_info = cpuinfo.get_cpu_info()
        self.ram_size = round(os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024.0 ** 3), 2)

    # Création d'une méthode "to_dict"
    def to_dict(self):
        return {
            'system': self.system,
            'processor': self.processor,
            'architecture': f"{self.architecture[0]} {self.architecture[1]}",
            'hostname': self.hostname,
            'ip_address': self.ip_address,
            'cpu_type': self.cpu_info['brand_raw'],
            'cpu_frequency': self.cpu_info.get('hz_actual_raw', 'Unknown'),
            'cpu_cores': self.cpu_info['count'],
            'ram_size': f"{self.ram_size} Go"
        }

class HtmlRenderer:
    # Création d'une méthode __init__ avec les arguments "template_path" et "template_file"
    def __init__(self, template_path='templates', template_file='system_info.html'):
        self.template_path = template_path
        self.template_file = template_file

    # Création d'une méthode "render" avec l'argument "context"
    def render(self, context):
        return render_template(self.template_file, **context)

@app.route('/')
# Création d'une fonction "index" sans argument et qui retourne la valeur de la méthode "render" de l'instance "html_renderer" avec l'argument "system_info"
def index():
    system_info = SystemInfo().to_dict()
    html_renderer = HtmlRenderer()
    html = html_renderer.render(system_info)
    return html

if __name__ == '__main__':
    app.run(debug=True)
