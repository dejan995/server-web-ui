from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_login import current_user, login_required
import os
import psutil
import socket

main = Blueprint('main', __name__)


@main.route('/')
def route_default():
    return redirect(url_for('users.login'))


@main.route('/dashboard')
@login_required
def dashboard():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    cpu_usage = psutil.cpu_percent(2)
    total_ram = str(round(psutil.virtual_memory()[0] / 1000000000, 2))
    available_ram = str(round(psutil.virtual_memory()[1] / 1000000000, 2))
    ram_usage = psutil.virtual_memory()[2]
    hostname = socket.gethostname()
    procs = {p.pid: p.info for p in psutil.process_iter(['name', 'username'])}

    if cpu_usage >= 80:
        cpu_color = 'red'
    elif 80 >= cpu_usage >= 35:
        cpu_color = 'yellow'
    else:
        cpu_color = 'green'

    if ram_usage >= 80:
        ram_color = 'red'
    elif 80 >= ram_usage >= 35:
        ram_color = 'yellow'
    else:
        ram_color = 'green'

    return render_template('main/dashboard.html', title='Dashboard', image_file=image_file,
                           cpu_usage=cpu_usage,
                           cpu_color=cpu_color,
                           total_ram=total_ram,
                           available_ram=available_ram,
                           ram_usage=ram_usage,
                           ram_color=ram_color,
                           hostname=hostname,
                           procs=procs)


@main.route('/kill_process/<int:pid>', methods=['POST'])
@login_required
def kill_process(pid):
    proc.kill
    return redirect(url_for('main.dashboard'))
