# 1. Install

```
curl -fsSL https://ollama.com/install.sh | sh
```

## 1.1 Server

If the ollama backend doesn't automatically start, run it manually:

```
ollama serve
```

This might fail if port is already taken

Check it: ```sudo lsof -i :11434``` then ```kill -9 PID``` (if it's not ollama itself)

# 2. Mistral

Pull the mistral model:

```
ollama pull mistral:instruct
```

This will fetch the latest Mistral 7B Instruct model in quantized format (by default, it uses q4_0 or similar, runs well on 3090 Ti).

# 3. Run a chat

```
ollama run mistral:instruct
```

This should pull up interactive shell

## 3.3 Run as a local API

```
ollama serve
```

Example request:

```sh
curl http://localhost:11434/api/generate -d '{
  "model": "mistral:instruct",
  "prompt": "",
  "stream": false
}'
```

Should return JSON:

```json
{
  "response": "",
  ...
}
```

# 4. Some degree of tweaking is possible

Create custom model with a `Modelfile`

```
FROM mistral:instruct

PARAMETER temperature 0.7
PARAMETER stop "\nUser:"
```

Then:

```
ollama create my-mistral -f Modelfile
ollama run my-mistral
```