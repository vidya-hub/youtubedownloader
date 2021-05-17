import http.client

conn = http.client.HTTPSConnection("youtube-to-mp4.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "c14ed64d89mshd41ecc420a5e25fp16b1b8jsnb1789191b5d3",
    'x-rapidapi-host': "youtube-to-mp4.p.rapidapi.com"
    }

conn.request("GET", "/url=&title?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DIfNB5RTxnhI&title=Call%20of%20Duty%20%3A%20Modern%20Warfare%202%20Remastered%20-%20All%20Weapon%20Reload%20Animations%20in%204%20Minutes", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))