from flask import(Blueprint,g,jsonify,request)
from threading import Timer
import subprocess

from . import portScan
from . import multiScan
from . import osTest
from . import arpSpoof

bp=Blueprint('webInterface',__name__)

@bp.route('/scan',methods=('POST','GET'))
def scanStart():
    ip=request.form['ip']
    startPort=request.form['sPort']
    endPort=request.form['ePort']
    scanType=request.form['type']
    if scanType=='single':
        return jsonify(portScan.scanAll(ip,startPort,endPort))
    if scanType=='multi':
        multiScan.main()
        return jsonify('程序已启动，但是当时做的时候忘记加参数设置功能，现在没时间改了...')

@bp.route('/mitm',methods=('POST','GET'))
def mitmproxyGo():
    child1=subprocess.Popen("mitmdump -s startport.py ")
    def endit():
        child1.kill()
    t=Timer(60,endit)
    t.start()
    return "废话少说，上http://www.scut.edu.cn"

@bp.route('/arp',methods=('POST','GET'))
def arpThief():
    tip=request.form['tip']
    gip=request.form['gip']
    arpSpoof.spoof('Intel(R) Dual Band Wireless-AC 3160',tip,gip)
    return "我好像永远不会返回消息" #是的没错，这个会一直处于pending...
