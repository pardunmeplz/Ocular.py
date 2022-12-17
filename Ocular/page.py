import http.server
import socketserver
import os

class Page:
    name = 'ocular'
    style = {}

    def __init__(self, name):
        self.name = name
    
    def getStyle(self):
        styleText = ""
        for tag, val in self.style.items():
            styleText += f'{tag} : {val} ;'
        return styleText

    def host(self,port=8000):
        handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("",port), handler) as httpd:
            httpd.serve_forever()

    def build(self,path="index.html"):
            with open(path,'w') as webpage:
                webpage.write(f'''
<!DOCTYPE html>
<html>

<head>
    <script src="https://cdn.jsdelivr.net/pyodide/v0.20.0/full/pyodide.js"></script>
    <title>{self.name}</title>
<head>

<body id = "Body" style = "{self.getStyle()}">
    <script>
        loadPyodide().then(async pyodide =>  {{
        
        await pyodide.runPythonAsync(`
        from pyodide.http import pyfetch
        response = await pyfetch("src/main.py")
        with open("main.py", "wb") as f:
            f.write(await response.bytes())
        `)
        
        pyodide.runPython(`
        import main
        main.init()`)
        }})    
    </script>
</body>

</html>''')

    def run(self,path: str = "index.html",port: int = 8000) -> None:
        self.build(path = path)
        os.system(f"start \"\" http://localhost:{port}")
        self.host(port = port)