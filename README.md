<center><img src="https://github.com/new92/IGFI/assets/94779840/21aa884d-6dfe-46b3-881c-e9f74b69dedc" alt="Logo" width="512" height="512" /></center>

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9864f7f507804c81975576919a4a684a?logo=codacy&style=for-the-badge)](https://app.codacy.com/gh/new92/IGFI/dashboard?logo=codacy&style=for-the-badge) [![Number of files](https://img.shields.io/github/directory-file-count/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/directory-file-count/new92/IGFI) [![Code size](https://img.shields.io/github/languages/code-size/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/languages/code-size/new92/IGFI) [![Followers](https://img.shields.io/github/followers/new92?style=for-the-badge)](https://img.shields.io/github/followers/new92) [![Forks](https://img.shields.io/github/forks/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/forks/new92/IGFI) [![Stars](https://img.shields.io/github/stars/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/stars/new92/IGFI) [![Open issues](https://img.shields.io/github/issues-raw/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/issues-raw/new92/IGFI) [![Closed Issues](https://img.shields.io/github/issues-closed-raw/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/issues-closed-raw/new92/IGFI) [![Open pull requests](https://img.shields.io/github/issues-pr-raw/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/issues-pr-raw/new92/IGFI) [![Closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/issues-pr-closed-raw/new92/IGFI) [![Discussions](https://img.shields.io/github/discussions/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/discussions/new92/IGFI) [![Contributors](https://img.shields.io/github/contributors/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/contributors/new92/IGFI) [![Language](https://img.shields.io/github/languages/top/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/languages/top/new92/IGFI?style=for-the-badge)

# IGIfy Remastered

With IGIfy Remastered, you can effortlessly attempt to increase your followers by following and unfollowing accounts to encourage follow-backs. **It works seamlessly for both private and public accounts**. Gains depend on user behavior and Instagram's algorithm—results vary. Initial uses may yield 0-50 followers, with subsequent uses adding 0-30. To maintain account safety, use the script every 2-3 days and enable niche targeting for better results. The script provides info on actions taken and detected gains.

> If you find this repository helpful, please consider giving it a star and/or forking it. Your support encourages me to keep sharing similar repositories. If you encounter any issues, have suggestions, or simply didn't like the script, feel free to contact me anytime at <a href='mailto:new92github@gmail.com'>this email address</a>, or start a <a href="https://github.com/TechWithTy/IGIfy-Remastered/discussions">discussion</a>, or open an <a href="https://github.com/TechWithTy/IGIfy-Remastered/issues">issue</a>. Any form of feedback is welcome and appreciated (please refrain from using vulgar language).

[![github-stats-card](https://kasroudra-stats-card.onrender.com/repo?user=TechWithTy&repo=IGIfy-Remastered&layout=compact&theme=vue)](https://github.com/KasRoudra/github-stats-card)

## Urls 🔗

 - [License](https://github.com/TechWithTy/IGIfy-Remastered/blob/main/LICENSE.md)
 - [Contributing](https://github.com/TechWithTy/IGIfy-Remastered/blob/main/CONTRIBUTING.md)
 - [Code of conduct](https://github.com/TechWithTy/IGIfy-Remastered/blob/main/CODE_OF_CONDUCT.md)
 - [You may also find interesting](https://github.com/TechWithTy?tab=repositories)

## Author ✍️

- [@TechWithTy](https://github.com/TechWithTy)

## Installation 📥

- **Make sure you're logged in to your Instagram account from Firefox before executing IGFI.**

### Linux 🐧

```bash
sudo su
git clone https://github.com/TechWithTy/IGIfy-Remastered
cd IGIfy-Remastered
sudo pip install -r ./files/requirements.txt
python3 ./cookies.py # generates a session file (not cookies.sqlite)
python3 ./igfi.py -u <username> -p <password> --session <path_to_session_file>
```

### Windows 🪟

```bash
git clone https://github.com/TechWithTy/IGIfy-Remastered
cd IGIfy-Remastered
pip install -r ./files/requirements.txt
python cookies.py  # generates a session file (not cookies.sqlite)
python igfi.py -u <username> -p <password> --session <path_to_session_file>
```

### MacOS 🍎

```bash
git clone https://github.com/TechWithTy/IGIfy-Remastered
cd IGIfy-Remastered
python -m pip install -r ./files/requirements.txt
python3 ./cookies.py # generates a session file (not cookies.sqlite)
python3 ./igfi.py -u <username> -p <password> --session <path_to_session_file>
```

### Docker 🐋

```bash
git clone https://github.com/TechWithTy/IGIfy-Remastered
cd IGIfy-Remastered
python3 ./cookies.py # this command will generate the value for the <path_to_session_file>
docker build -t igfi .
docker run -e DOCKER_CONTAINER=true -e USERNAME=<username> -e PASSWORD=<password> -e SESSION=<path_to_session_file> -p 4000:4000 -it igfi
```

## Troubleshooting 🛠️

### Dependency Conflicts

If you encounter dependency conflicts when installing requirements, it's likely because you have other Python packages installed that require different versions of the same dependencies (e.g., pydantic, rich).

**Solutions:**

1. **Use the provided setup scripts** (Recommended):
   ```bash
   # For Linux/Mac
   bash setup.sh

   # For Windows
   setup.bat
   ```

2. **Manual virtual environment setup**:
   ```bash
   # Create and activate virtual environment
   python -m venv venv

   # On Windows:
   venv\Scripts\activate

   # On Linux/Mac:
   source venv/bin/activate

   # Install dependencies
   pip install -r files/requirements.txt
   ```

3. **Update pip**:
   ```bash
   pip install --upgrade pip
   ```

### Common Issues

- **ModuleNotFoundError**: Make sure you're in the virtual environment or have installed all requirements
- **Version conflicts**: Always use a virtual environment to avoid conflicts with other projects
- **Instagram login errors**: Run `python cookies.py` first to generate session data

### Windows 🪟

```bash
git clone https://github.com/new92/IGFI
cd IGFI
python -m venv igfi
.\igfi\scripts\activate
pip install -r ./files/requirements.txt
python cookies.py  # generates a session file (not cookies.sqlite)
python igfi.py -u <username> -p <password> --session <path_to_session_file>
```

### Linux 🐧 / MacOS 🍎

```bash
git clone https://github.com/new92/IGFI
cd IGFI
python -m venv igfi
source venv/bin/activate
pip install -r ./files/requirements.txt
python3 ./cookies.py # generates a session file (not cookies.sqlite)
python3 ./igfi.py -u <username> -p <password> --session <path_to_session_file>

## Usage 📚

- Full usage guide with examples, batching, follow-only, cleanup, and hashtag targeting is in `USAGE.md`.

### Important: Passing --session on Windows

- Keep the entire command on one line and quote the path.
- `--session` must point to the session file created by `cookies.py` (or an instagrapi settings JSON) — not to `cookies.sqlite`.

Examples:

- CMD:
  - `python igfi.py -u "<username_or_email>" -p "<password>" --session "C:\\Users\\<you>\\Documents\\Github\\IGFI\\ig_session.json"`
- PowerShell:
  - `python .\igfi.py -u '<username_or_email>' -p '<password>' --session 'C:\\Users\\<you>\\Documents\\Github\\IGFI\\ig_session.json'`
- Git Bash:
  - `python igfi.py -u "<username_or_email>" -p "<password>" --session "/c/Users/<you>/Documents/Github/IGFI/ig_session.json"`
```

##### Virtual environment deactivation 📭

##### Windows 🪟

`.\venv\Scripts\deactivate`

##### Linux 🐧 / MacOS 🍎

`deactivate`

## Update 🔄️

```bash
cd <path_to_script>/IGFI
git pull
```

## Features 🚀

- [ ] **Add followers from specific categories (ex. fitness, education, food, entertainment etc.)**
- [ ] Script which doesn't depend on third-party modules.
- [ ] GUI
- [ ] Docker support
- [x] ~~Virtual environment setup~~
- [x] ~~Execute the script directly from terminal (using argparse)~~
- [ ] V4 (this version will include the features as shown above and some extra)
- [x] ~~Display the usernames of the followers added~~ **<a href="https://github.com/new92/IGFI/scripts/tree/main/igfi.py">URL</a>**
- [x] ~~V3 script~~ **<a href='https://github.com/new92/IGFI/tree/main/scripts/igfi.py'>URL</a>**

## Tested on 🔎

| OS | Linux | Windows | MacOS
| :---: | :---: | :---: | :---: |
| -> | Kali |
| -> | Ubuntu | 10 |
| -> | | 11 |

## Screenshots 📸

**Photos of the project can be found at <a href="https://github.com/new92/IGFI/tree/main/photos">this url</a>**

## Contributing 🤝

Contributions are always welcome !

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.
For more info please check the `CODE_OF_CONDUCT.md` file

## Feedback 💭

If you have any feedback, please reach out to us at <a href="mailto:your.email@example.com">this email address</a>.

**Feel free to contact us anytime ! You'll get a reply within a day. Please avoid abusive or offensive language.
If you are reporting a bug or making a suggestion please make sure your make it as detailed as possible.**

## FAQ 🤔

#### Question 1

- Error while logging in ?

Answer ➡️ This error can be resolved by simply executing the `cookies.py` script and running the script again.

#### Question 2

- Where can I report a bug ?

Answer ➡️ You can report a bug by creating an issue or by emailing us at <a href="mailto:your.email@example.com">this</a> email address. Please feel free to include screenshots, the error which is being displayed, the OS you are using, your default browser etc. Any other additional info will be appreciated and will help to resolve the bug faster

### Question 3

- Is illegal to increase followers using script(s) ?

Answer ➡️ No, not at all! It's similar to asking if following and unfollowing an account is illegal, even though Instagram doesn't recommend using this technique to increase your followers.


### Question 4

- Can my account get blocked by using this script ?

Answer ➡️ Only if you're using a very old version of Instagram. But the script has been tested in several accounts and none of them got blocked.

## License 📜

[![License](https://img.shields.io/github/license/new92/IGFI?style=for-the-badge)](https://github.com/new92/IGFI/blob/main/LICENSE.md)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=new92/IGFI&type=Date)](https://star-history.com/#new92/IGFI&Date)
