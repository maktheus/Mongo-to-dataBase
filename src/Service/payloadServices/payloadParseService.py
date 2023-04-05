import subprocess
import json


def payloadWiseParser(payload):
    res = []
    for item in payload[0]:
        print(item)
        payload = item.get("payload")
        time = item.get("time")
        payload = json.loads(payload)
        payloadRaw = payload[6]["vs"]
        payloadDecodifier = subprocess.run(
            ["src/bin/decoder/main-linux", payloadRaw], stdout=subprocess.PIPE
        )
        payloadDecodifier = payloadDecodifier.stdout.decode("utf-8")
        payloadDecodifier = json.loads(payloadDecodifier)
        res.append({"payload": payloadDecodifier, "time": time})
    return res


def payloadHexParser(payload):
    res = []
    for item in payload[1]:
        payload = item.get("payload")
        time = item.get("time")
        try:
            payload = json.loads(payload)
        except json.decoder.JSONDecodeError:
            pass
        res.append({"payload": payload, "time": time})

    return res


def payloadKSParser(payload):
    res = []
    for item in payload[2]:
        payload = item.get("payload")
        time = item.get("time")
        payload = json.loads(payload)

        res.append({"payload": payload, "time": time})

    return res


def main():
    payloadHexParser()


if __name__ == "__main__":
    main()
