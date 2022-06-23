from speechbrain.pretrained import EncoderDecoderASR
import torch
import flask
from flask import Flask, request, jsonify, render_template
import os
app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False
@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')
@app.route('/model',methods=['POST'])
def runs():
    if request.method=='POST':
        file=request.files['wav']
        if not file:
            return render_template('index.html',label="no file")
        audio_0=os.path.join("/var/www/html/",file.filename)
        file.save(audio_0)
        asr_model = EncoderDecoderASR.from_hparams(source="ddwkim/asr-conformer-transformerlm-ksponspeech", savedir="pretrained_models/asr-conformer-transformerlm-ksponspeech",  run_opts={"device":"cpu"})
        results=asr_model.transcribe_file(audio_0)
        names=results.split("에게")[0].strip()
        substring=results.split("에게")[1]
        digit=substring.split("원")[0].strip()
        if digit == '만':
            amount=10000
        elif digit == '천':
            amount=1000
        elif digit == '백':
            amount=100
        service=substring.split("원")[1].strip()
        #return render_template('index.html',label1=name,label2=amount,label3=service)
        return jsonify(name=names,amount=amount,service=service)
if __name__ == '__main__':
# start api
    app.run(port=5000, debug=True)