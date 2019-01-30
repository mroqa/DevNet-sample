__author__ = 'moahmed'

from flask import Flask, render_template, logging, redirect, url_for, flash, request,session
from data import Commands, Devices, Apps
import os
from netmiko import ConnectHandler
from datetime import datetime
import ipaddress

app = Flask(__name__)

cmds = Commands()
apps = Apps()
devices = Devices()

app.config['File_Dir'] = '/'

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/about")
def about():
    base = os.path.dirname(os.path.abspath(__file__))
    target_folder = os.path.join(base, 'static')
    target = os.path.join(target_folder, 'net.jpg')
    print(target)
    return render_template('about.html', image_url = target)

@app.route("/devices")
def vlan():

    return render_template('vlan.html', apps = apps)


@app.route("/provision", methods = ['GET', 'POST'])
def provision():
    if request.method == 'POST':
        vlanId = request.form['vlanId']
        vlanName = request.form['vlanName'].strip()
        userName = request.form['username'].strip()
        passCode = request.form['passcode']
        interface = request.form['int']

        for d in devices:
            d['password']=passCode
            d['username']=userName

        for d in devices:
            netco = ConnectHandler(**d)
            all_commands = ['vlan '+vlanId , 'name '+vlanName]
            output = netco.send_config_set(all_commands)
            netco.save_config()
            print(output)
        session['dList'] = devices
        print(interface)

        for d in devices:
            if '192.168.100.114' == d['ip']:
                print('FOUND')
            else:
                continue


        flash('VLAN ' + str(vlanId) + ' has been created successfully...','success ')
        return redirect(url_for('success'))

    return render_template('provision.html')


@app.route("/success")
def success():

    return render_template('success.html')


@app.route("/device/<string:id>")
def device(id):
    #print(id)
    for x in apps:
        if id == x['id']:
            nxos = {
                'device_type': 'cisco_nxos',
                'ip': x['ip'],
                'username':'admin',
                'password':'admin',
                #'global_delay_factor': 2,
            }
            '''
            nxos = {
                'device_type': 'cisco_nxos',
                'ip': x['ip'],
                'username':'cattool',
                 'password':'NW762@n2016',
            }'''
            print(nxos)

            try:
                print (datetime.now() )
                net_connect = ConnectHandler(**nxos)

                net_connect.clear_buffer()
                #net_connect.find_prompt()
                #time.sleep(1)
                output = net_connect.send_command('show running', expect_string=r'#')
                net_connect.disconnect()
                return render_template("apprun.html", output = output)
            except Exception as e:
                return render_template("500.html", error = str(e))

@app.route("/snmp", methods = ['GET', 'POST'])
def snmp():
    if request.method == 'POST':
        switchIP = request.form['swip'].strip()
        snmpUser = request.form['snmpUser'].strip()
        hashType = request.form['hash']
        password = request.form['password']
        privType = request.form['priv']
        encryptType = request.form['key']
        contact = request.form['contact']
        location = request.form['location'].strip()
        server = request.form['server'].strip()
        sourceInt = request.form['source']
        vrf = request.form['vrf'].strip()

        print(switchIP + '\n' + snmpUser+'\n'+ hashType + '\n' + password +'\n' + sourceInt+ '\n')

        try:
            switchIP = ipaddress.ip_address(switchIP)
            server = ipaddress.ip_address(server)
            netco = ConnectHandler(device_type='cisco_nxos', ip='10.10.10.5', username='admin', password='admin')
            config_commands = ['snmp-server globalEnforcePriv',
                               'snmp-server user SNMPv3User auth sha P@$$w0rd321 priv aes-128 P@$$w0rd321',
                               'snmp-server contact SOC_NW',
                               'snmp-server location ELM',
                               'snmp-server enable traps',
                               'snmp-server host 192.168.100.102 traps version 3 priv SNMPv3User',
                               'snmp-server host 192.168.100.102 source-interface mgmt 0',
                               'snmp-server host 192.168.100.102 use-vrf management',
                               ]
            output = netco.send_config_set(config_commands)
            print(output)
        except Exception as e:
            return render_template('snmp.html', error = e)

        flash('SNMP has been created successfully...','success')
        return redirect(url_for('success'))

    return render_template('snmp.html')



@app.errorhandler(404)
def page_not_found(e):
  return render_template('500.html'), 404

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    #app.run(debug=True)
    app.run(host = '0.0.0.0', debug=True)

