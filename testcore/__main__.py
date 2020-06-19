from .env import BrHisiCam, list_boards
from . import BR_HISICAM_ROOT, BASE_WORK_DIR
import os
import argparse
import logging


def make_all(br_hisicam):
    br_hisicam.make_all()


# -------------------------------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose",      help="Enabel debug logging", action="store_true")
    parser.add_argument("-l", "--list",         help="List boards", action="store_true")
    parser.add_argument("-b", "--board",        help="Target board ID", metavar="BOARD", type=str)
    parser.add_argument("-o", "--output_dir",   help=f"Output directory, default {BASE_WORK_DIR}/<BOARD>", type=str)
    parser.add_argument("-c", "--clean",        help="Clean before building", action="store_true")

    subparsers = parser.add_subparsers(title="Action")
    for action in (
        make_all,
    ):
        action_parser = subparsers.add_parser(action.__name__,
            help=action.__doc__.strip() if action.__doc__ else None
        )
        action_parser.set_defaults(action=action)

    args = parser.parse_args()

    logging.basicConfig(level=(logging.DEBUG if args.verbose else logging.INFO))

    if args.list:
        print("\n".join(list_boards()))
        exit(0)

    if args.output_dir is None:
        args.output_dir = os.path.join(BASE_WORK_DIR, args.board)

    br_hisicam = BrHisiCam(
        board=args.board,
        output_dir=args.output_dir,
        clean=args.clean
    )

    args.action(br_hisicam)


if __name__ == "__main__":
    main()
