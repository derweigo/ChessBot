from lichesspy.api import user as liuser


def get_elo(user: str, timecontrol: str) -> int:
    """ Return the lichess Rating  """
    return liuser(user)['perfs'][timecontrol]['rating']


def live_game(user: str) -> str:
    """ Return the live game played by the user """
    try:
        game = liuser(user)['playing']
    except Exception:
        game = "This user is not playing a game right now."
    return game
