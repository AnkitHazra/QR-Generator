from flask import Flask, render_template, request
import qrcode
from io import BytesIO
import base64
from urllib.parse import urlparse

app = Flask(__name__)

def is_valid_url(u):
    try:
        p = urlparse(u)
        return bool(p.scheme and p.netloc)
    except:
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_data = None
    if request.method == 'POST':
        link = request.form.get('link', '').strip()
        if not link:
            return render_template('index.html', error='Please enter a URL')
        if not (link.startswith('http://') or link.startswith('https://')):
            link = 'https://' + link
        if not is_valid_url(link) or len(link) > 2000:
            return render_template('index.html', error='Please enter a valid URL (max 2000 chars)')

        try:
            img_io = BytesIO()
            img = qrcode.make(link)
            img.save(img_io, 'PNG')
            img_io.seek(0)
            b64 = base64.b64encode(img_io.read()).decode('utf-8')
            qr_data = f"data:image/png;base64,{b64}"
        except Exception:
            return render_template('index.html', error='Failed to generate QR')

    return render_template('index.html', qr_data=qr_data)

if __name__ == "__main__":
    app.run()