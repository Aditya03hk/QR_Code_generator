from flask import Flask,render_template,request
from flask import send_file
#https://pypi.org/project/qrcode/
import qrcode
from io import BytesIO
# import base64
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

@app.route('/download_qr', methods=['POST'])
def download_qr():
    data = request.form.get('link')
    if data:
        # Generate QR code
        qr = qrcode.make(data)
        
        # Save QR code to BytesIO buffer
        qr_buffer = BytesIO()
        qr.save(qr_buffer)
        qr_buffer.seek(0)
        
        # Return QR code as downloadable file
        return send_file(
            qr_buffer,
            mimetype='image/png',
            as_attachment=True,
            download_name='qrcode.png'
        )

    return "Error: No QR code data provided"


if __name__ == '__main__':
    app.run(debug=True)
