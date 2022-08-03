# bhimupipy

BHIMUPIPY is a pip packages which can  verify  UPI IDs.

## Installation
Install this pip package .
```bash
pip install  bhimupipy
```

and use it like

```python
from bhimupipy import verify_upi
```

# Usage
### CLI

```
~$ bhimupipy --help

usage: -m [-h] [-v] [--upi UPI]

bhimupipy: Get the details of UPI ID.

options:
  -h, --help     show this help message and exit
  -v, --version  print the version of the package (default: False)
  --upi UPI      see upi datails (default: None)
```
### Verifying  UPI ID
```
~$ bhimupipy --upi sumithemmadi@ybl
```

```yaml
~$ bhimupipy --upi sumithemmadi@ybl
{
   "result": true,
   "vpa": "sumithemmadi@upi",
   "vpaValid": true,
   "payeeAccountName": "EMMADI SUMITH KUMAR",
   "message": "Verified UPI ID"
}
```
- This will verify UPI ID



## Verifing UPI ID 
```python
from bhimupipy import verify_upi
verify_upi("sumithemmadi@ybl")
```

## output
```py
{
   "result": true,
   "vpa": "sumithemmadi@upi",
   "vpaValid": true,
   "payeeAccountName": "EMMADI SUMITH KUMAR",
   "message": "Verified UPI ID"
}
```

