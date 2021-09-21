# ChessBot
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=ffffff) ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?&logo=javascript&logoColor=000000) ![PHP](https://img.shields.io/badge/-PHP-BB4444?logo=PHP&logoColor=000000)

![VS Code](https://img.shields.io/badge/VSCode-%23007ACC?logo=Visual-studio-code) ![Pycharm](https://img.shields.io/badge/PyCharm-green?logo=PyCharm) 

![Git](https://img.shields.io/badge/-Git-%23F05032?logo=git&logoColor=%23ffffff)

<a href="https://github.com/Arvecx/ChessBot">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=arvecx&repo=ChessBot&theme=algolia" />
</a>


## Technical fundamentals
To use the bot you need a Discord bot and a Lichess account.
We recommend creating another new account for this purpose. The account is only important if you want to kick people. Otherwise you don't need a Lichess account.  The presence of Python is required.

### Create a Discord bot
Lichess bots can be created on the [Discord Developer](https://discord.com/developers/) page. Since this is a different topic, we recommend the video from freeCodeCamp. It is linked at the end of this text. Of course, the bot must also be invited to their server and be able to write there. But this is your responsibility.  [YouTube Video about Discord Bots](https://youtu.be/SPTfmiYiuok?t=3)


## Installing the bot

### Clone git
You can download the git simply by using the command git clone. Please use the master branch

```GIT
git clone https://github.com/arvecx/chessbot.git
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



## Have Fun