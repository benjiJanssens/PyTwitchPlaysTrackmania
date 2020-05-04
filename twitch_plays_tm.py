import getopt
import sys

from pytwitchplays import TwitchPlays, Action, DIK_UP, DIK_DOWN, DIK_LEFT, DIK_RIGHT, DIK_NUMPAD0, DIK_RETURN, DIK_BACK

ACTIONS = {
    "up": Action(DIK_UP, 1.0),
    "down": Action(DIK_DOWN, 1.0),
    "left": Action(DIK_LEFT, 0.5),
    "right": Action(DIK_RIGHT, 0.5),
    "honk": Action(DIK_NUMPAD0, 1.0),
    "respawn": Action(DIK_RETURN, 1.0, "respawn", "Respawning...", 0.5),
    "restart": Action(DIK_BACK, 1.0, "restart", "Restarting...", 0.75)
}


def main(argv):
    usage = "python twitch_plays_tm.py -p <password> -u <username> [-c <channel>]"
    password = None
    username = None
    channel = None

    try:
        opts, args = getopt.getopt(
            argv, "hp:u:c:", ["password=", "username=", "channel="]
        )
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        if opt in ("-p", "--password"):
            password = arg
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-c", "--channel"):
            channel = arg
    if not channel:
        channel = username
    if password and username and channel:
        TWITCH_PLAYS = TwitchPlays(
            password, username, channel, ACTIONS
        )
        TWITCH_PLAYS.run()
    else:
        print(usage)
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
