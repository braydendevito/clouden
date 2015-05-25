from flask import Flask, request, redirect, url_for, render_template
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import InputRequired


with open('iwlist/sep1.txt', 'r') as infile:

       data = infile.read()

lhs, rhs = data.split(":", 1)

ssid1 = ''.join(lhs.split())[:-2]
####
with open('iwlist/sep2.txt', 'r') as infile:

       data = infile.read()

lhs, rhs = data.split(":", 1)

ssid2 = ''.join(lhs.split())[:-2]
####
with open('iwlist/sep3.txt', 'r') as infile:

       data = infile.read()

lhs, rhs = data.split(":", 1)

ssid3 = ''.join(lhs.split())[:-2]
####
with open('iwlist/sep4.txt', 'r') as infile:

       data = infile.read()

lhs, rhs = data.split(":", 1)

ssid4 = ''.join(lhs.split())[:-2]
####
with open('iwlist/sep5.txt', 'r') as infile:

       data = infile.read()

lhs, rhs = data.split(":", 1)

ssid5 = ''.join(lhs.split())[:-2]



app = Flask(__name__)

class WifiForm(Form):
    password = StringField(validators=[InputRequired()])


@app.route('/', methods=['GET', 'POST'])
def wifi_password1():
    form = WifiForm(csrf_enabled=False)

    if form.validate_on_submit():
        password = form.password.data

        with open('wpa_supplicant.conf', 'w') as f:
            f.write("ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\n\nnetwork={\n\tssid=\"" + ssid1 + "\"" + "\n\tpsk=\"" + password + "\"" + "\n\tproto=RSN\n\tkey_mgmt=WPA-PSK\n\tpairwise=CCMP\n\tauth_alg=OPEN\n}")

        return redirect(url_for('wifi_password1'))

    return render_template('main.html',form=form)
#
@app.route('/', methods=['GET', 'POST'])
def wifi_password2():
    form = WifiForm(csrf_enabled=False)

    if form.validate_on_submit():
        password = form.password.data

        with open('wpa_supplicant.conf', 'w') as f:
            f.write("ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\n\nnetwork={\n\tssid=\"" + ssid2 + "\"" + "\n\tpsk=\"" + password + "\"" + "\n\tproto=RSN\n\tkey_mgmt=WPA-PSK\n\tpairwise=CCMP\n\tauth_alg=OPEN\n}")

        return redirect(url_for('wifi_password2'))

    return render_template('main.html',form=form)
#
@app.route('/', methods=['GET', 'POST'])
def wifi_password3():
    form = WifiForm(csrf_enabled=False)

    if form.validate_on_submit():
        password = form.password.data

        with open('wpa_supplicant.conf', 'w') as f:
            f.write("ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\n\nnetwork={\n\tssid=\"" + ssid3 + "\"" + "\n\tpsk=\"" + password + "\"" + "\n\tproto=RSN\n\tkey_mgmt=WPA-PSK\n\tpairwise=CCMP\n\tauth_alg=OPEN\n}")

        return redirect(url_for('wifi_password3'))

    return render_template('main.html',form=form)
#
@app.route('/', methods=['GET', 'POST'])
def wifi_password4():
    form = WifiForm(csrf_enabled=False)

    if form.validate_on_submit():
        password = form.password.data

        with open('wpa_supplicant.conf', 'w') as f:
            f.write("ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\n\nnetwork={\n\tssid=\"" + ssid4 + "\"" + "\n\tpsk=\"" + password + "\"" + "\n\tproto=RSN\n\tkey_mgmt=WPA-PSK\n\tpairwise=CCMP\n\tauth_alg=OPEN\n}")

        return redirect(url_for('wifi_password4'))

    return render_template('main.html',form=form)
#
@app.route('/', methods=['GET', 'POST'])
def wifi_password5():
    form = WifiForm(csrf_enabled=False)

    if form.validate_on_submit():
        password = form.password.data

        with open('wpa_supplicant.conf', 'w') as f:
            f.write("ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\n\nnetwork={\n\tssid=\"" + ssid5 + "\"" + "\n\tpsk=\"" + password + "\"" + "\n\tproto=RSN\n\tkey_mgmt=WPA-PSK\n\tpairwise=CCMP\n\tauth_alg=OPEN\n}")

        return redirect(url_for('wifi_password5'))

    return render_template('main.html',form=form)




if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

