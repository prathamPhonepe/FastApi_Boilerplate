from flask import Flask, request, abort
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def execute_request():
    url = request.args.get("url")
    if url == None:
        return "missing parameter: url. Did you read the source code attached on CTFd?"
    else:
        blacklist = ["DICT", "FILE", "FTP", "FTPS", "GOPHER", "IMAP", "HTTP", "HTTPS", "IMAPS", "LDAP", "LDAPS", "POP3", "POP3S", "RTMP", "RTSP", "SCP", "SFTP", "SMB", "SMBS", "SMTP", "SMTPS", "TELNET", "TFTP", "%"]
        for protocol in blacklist:
            if protocol.lower() in url.lower():
                abort(400)

        out = subprocess.run(['curl', url], capture_output=True, text=True)
        return out.stdout

# main driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"))