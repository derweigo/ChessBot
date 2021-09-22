from lichesspy.api import user as liuser

def get_elo(user: str, timecontrol: str) -> int:
    """ Return the lichess Rating  """
    return liuser(user)['perfs'][timecontrol]['rating']
