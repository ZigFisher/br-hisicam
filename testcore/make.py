import subprocess
import logging


class Make:
    def __init__(self, root_dir, args=[]):
        self._root_dir = root_dir
        self._args = ["make", "-s", "--no-print-directory"] + args

    def check_call(self, args):
        args = self._args + args
        logging.debug(f"Execute {args} in {self._root_dir} ...")
        subprocess.check_call(args, cwd=self._root_dir)

    def check_output(self, args):
        args = self._args + args
        logging.debug(f"Execute {args} in {self._root_dir} ...")
        output = subprocess.check_output(args, cwd=self._root_dir)
        logging.debug(f"Output of {args} command: {output}")
        return output

    def get_output_lines(self, args):
        out = self.check_output(args)
        return [l.strip() for l in out.decode("utf-8").split("\n")]
