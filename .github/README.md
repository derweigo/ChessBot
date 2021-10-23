# ChessBot
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=ffffff) 

![VS Code](https://img.shields.io/badge/VSCode-%23007ACC?logo=Visual-studio-code) ![Pycharm](https://img.shields.io/badge/PyCharm-green?logo=PyCharm) 

![Git](https://img.shields.io/badge/-Git-%23F05032?logo=git&logoColor=%23ffffff) ![GitHub](https://img.shields.io/badge/GitHub-0d8a00?logo=github&logoColor=ffffff) 

<a href="https://github.com/Fevecx/ChessBot">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=Fevecx&repo=ChessBot&theme=algolia" />
</a>


## Technical fundamentals
To use the bot you need a Discord account.
We recommend creating another new account for this purpose. You don't need a Lichess account.  The presence of Python is required.
 
### Create a Discord bot
Discord bots can be created on the [Discord Developer](https://discord.com/developers/) page. Since this is a different topic, we recommend the video from freeCodeCamp. It is linked at the end of this text. Of course, the bot must also be invited to their server and be able to write there. But this is your responsibility.  [YouTube Video about Discord Bots](https://youtu.be/SPTfmiYiuok?t=3)


## Installing the bot

### Clone git
You can download the git simply by using the command git clone. Please use the master branch

```GIT
git clone https://github.com/Fevecx/chessbot.git
```

### Pip install 
Actually, pip should already be there. If this is not the case, I will give a short instruction here. Simply copy the following commands into a shell or CMD. The instructions are only for Windows users. Linux and Mac users know everything better and therefore don't need them. 

```PowerShell
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Installation of the pip suspensions
This is also done with a simple console input. 
```PowerShell
pip install -r client\requirements.txt 
```

Please note that the requirements file is located in the subfolder client.

## Set up the bot 
The bot does not use encv as a development environment. Similar to the [faultybot](https://github.com/jplight/faultybot), the Discord token and all private keys are read in via a config file. An env is not required due to the simplicity of the project :)
Therefore it is actually only necessary to create a config file and to store the token there. The file should have the following structure

```python
token = "DATA"
```


## Have Fun
