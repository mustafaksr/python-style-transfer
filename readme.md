

```bash
cd /media/desktop/01D7E2330EB2B040/google-cloud-ml/python-style-transfer
```
```bash
virtualenv ~/style
```

```bash
source ~/style/bin/activate
```

```bash
pip install -r reqs.txt
```

```bash
export PORT=8080
python3 main.py
```

```bash
export PORT=8080
docker run -p $PORT:$PORT -e PORT=$PORT tensorflow_style_transfer:latest
```