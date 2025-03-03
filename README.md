# Malicious VBA Macro

## Overview
This repository contains a demonstration of a malicious VBA macro used for cybersecurity research and analysis. The macro is designed to execute upon opening a document, retrieve an encoded C2 server address hidden within an image, establish a connection with the server, and exfiltrate sensitive files.

## Features
- **Steganographic Encoding**: The C2 server IP address is embedded in an image using least significant bit (LSB) encoding. ([encode.py](https://raw.githubusercontent.com/emmekappaa/MacroVBA_Project/refs/heads/master/codifica_decofica/codifica_ip.py?token=GHSAT0AAAAAAC62ZG7CO7XHNJLP5GC5BDBOZ6F6CSA))
- **VBA Macro Execution**: The macro automatically executes upon document opening.
- **Code Obfuscation**: Various obfuscation techniques, including function and variable renaming, string encoding, and comment removal, are applied.
- **Network Communication**: The macro retrieves the C2 server address, downloads and executes an information stealer, and transmits data back to the attacker.

## Attack Infrastructure
- **Attacker Machine**: Ubuntu 24.04.01 LTS running a Flask-based C2 server.
- **Victim Machine**: Windows 11 virtual machine connected via a NAT network in VirtualBox.
- **Communication Protocols**: Uses HTTP GET and POST requests for payload delivery and data exfiltration.

## Obfuscation Techniques
1. **Manual Obfuscation**: 
   - Function and variable renaming.
   - String encoding.
   - Comment removal.
2. **Automated Obfuscation**:
   - Usage of [MacroPack](https://github.com/sevagas/macro_pack) to generate obfuscated VBA code.
   
## Detection Evasion
The effectiveness of the obfuscation was evaluated using VirusTotal:
- **Custom Obfuscation**: Triggered heuristic-based detections (e.g., Heur2, associated with Emotet loaders).
- **MacroPack Obfuscation**: Identified with more specific signatures, indicating that automated obfuscation tools are less effective at evading detection.

## Delivery Method: Spear Phishing Attack
The macro was delivered via a **spear-phishing campaign**, masquerading as an **iCloud+ invoice receipt**. The email contained a "Click here" link, which directly triggered the download of the malicious document from **Storj**.


![Phishing Email](https://github.com/user-attachments/assets/72e2cd44-8559-4444-8b01-ac88d719fa10)


### Why Storj?
- **End-to-End Encryption**: Unlike Dropbox or Google Drive, Storj provides full encryption, ensuring that uploaded files remain unreadable to third parties.
- **No File Scanning**: Cloud services like Dropbox actively scan uploaded files and may suspend accounts distributing malicious macros. Storj, however, does not perform such scans, making it an ideal choice for payload hosting.


![storj](https://github.com/user-attachments/assets/26620649-a7ba-424b-8777-af9d3b2f7518)


## Disclaimer
This project is intended for educational and research purposes only. Unauthorized use of this code for malicious activities is strictly prohibited.
