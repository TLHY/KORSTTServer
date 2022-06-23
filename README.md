# KORSTTServerAPI
![image](https://user-images.githubusercontent.com/54972550/175376454-07211c01-2b4e-473b-aac3-86f757a6bb1b.png)

**Input:**
Korean wav file

**output:**
JSON example: {"amount":10000,"name":"아들","service":"송금"}
API loads the STT model and writes string from input wav.
Then, it's divided to name, amount, service

**NOTICE:**
Follow steps from https://huggingface.co/ddwkim/asr-conformer-transformerlm-ksponspeech 
which is a speechbrain model trained with Ksponspeech dataset provided by AI HUB.
