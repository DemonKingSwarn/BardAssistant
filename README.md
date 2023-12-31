# BardAssistant <img src="https://www.gstatic.com/lamda/images/favicon_v1_150160cddff7f294ce30.svg" width="35px" />

It is a Google Bard based Voice Assistant. [Uses the reverse engineered Bard API](https://github.com/acheong08/Bard).

# Installation

```sh
pip install --upgrade BardAssistant
```

**NOTE** YOU NEED `PYTHON` INSTALLED AND IN YOUR `PATH`

# Authentication

Go to https://bard.google.com

- hit `F12` for console
    - Copy the values
        - Session: Go to Application -> Cookies -> `__Secure-1PSID` and `__Secure-1PSIDTS`. Copy the value of those cookie.
    - Paste those cookie values in the `config.json` file based on the example here [config.json.example](https://github.com/DemonKingSwarn/BardAssistant/raw/master/config.json.example)
        - On Linux and Mac:
            - `~/.config/BardAssistant/config.json`
        - On Windows:
            - `C:\Users\<username>\.config\BardAssistant\config.json`

# Usage

- Open a terminal
- Type `BardAssistant` and hit enter
