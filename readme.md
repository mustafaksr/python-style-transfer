
# Run localy
```bash
git clone https://github.com/mustafaksr/python-style-transfer.git

cd ~/python-style-transfer
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

# Run Docker
```bash
export PORT=8080
docker pull mustafakeser/tensorflow_style_transfer:latest
docker run -p $PORT:$PORT -e PORT=$PORT mustafakeser/tensorflow_style_transfer:latest
```