from flask import Flask,render_template,request
#https://pypi.org/project/qrcode/
import qrcode
from io import BytesIO
from base64 import b64encode

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generateQR():
    memory=BytesIO()
    data=request.form.get('link')
    if data:
        img=qrcode.make(data)
        img.save(memory)
        memory.seek(0)
        base64_img="data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii')
        return render_template('index.html', data=base64_img)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
