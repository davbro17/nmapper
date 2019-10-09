# NMAPPER

Creates a Draw.io diagram xml file from NMAP xml output.

## Requirements

| Program | Link |
| --- | --- |
| Python 2.7 or 3.7 | https://www.python.org/downloads/ |
| Pip or Pip3 | https://pip.pypa.io/en/stable/installing/ |
| nmap | https://nmap.org/download.html |
| libnmap | https://pypi.org/project/python-libnmap/ |

## Getting Started

Step 1, run a nmap scan [(tutorial)](https://highon.coffee/blog/nmap-cheat-sheet/) Make sure to use `-oX` in order to save the output as an xml file. Example:

```bash
nmap -sS -A -T4 192.168.0.1/24 -xO example.xml
```

Step 2, run nmapper.py with an xml file as an argument. Example:

```bash
python nmapper.py example.xml
```
OR
```bash
python3 nmapper.py example.xml
```

Step 3, profit! If successful, the python script, will create a Draw.io xml file. Import this file into Draw.io [(guide)]( https://about.draw.io/draw-io-training-exercise-10-export-and-import/). Behold, a beautiful network diagram!

Step 4, more profits! "But I only use Microsoft Visio," -that coworker. In Draw.io, you can export a file as a visio file [(guide)](https://about.draw.io/draw-io-training-exercise-10-export-and-import/). You can also export a diagram to Gliffy or as embedded html.
