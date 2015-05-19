from flask import Flask, render_template, request, redirect, url_for
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   f=open('/etc/wpa_supplicant/wpa_supplicant.conf','r')
   fp=f.read()
   templateData = {
      'title' : 'HELLO!',
      'time': timeString,
      'WPA': fp
      }
   f.close()
   return render_template('main.html', **templateData)

@app.route('/data', methods=['POST'])
def handle_data():
   newWPA=request.form['indexMain']
   print newWPA
   f=open('/boot/wpa_supplicant.conf','w')
   f.write(newWPA)
   f.close
   return redirect(url_for('hello'))

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
