import subprocess
from pathlib import Path


class SvnClient:

    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password

    def _execute(self, *args):
        command = [
            "svn",
            *args,
            "--username", self.username,
            "--password", self.password,
            "--non-interactive",
            "--trust-server-cert"
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise Exception(result.stderr)

        return result.stdout

    def checkout(self, remote_path, local_path):
        return self._execute(
            "checkout",
            f"{self.server}/{remote_path}",
            local_path
        )

    def update(self, working_copy):
        return self._execute(
            "update",
            working_copy
        )

    def export_file(self, remote_file, destination):
        return self._execute(
            "export",
            f"{self.server}/{remote_file}",
            destination,
            "--force"
        )

    def cat(self, remote_file):
        return self._execute(
            "cat",
            f"{self.server}/{remote_file}"
        )

    def info(self, remote_path=""):
        return self._execute(
            "info",
            f"{self.server}/{remote_path}"
        )

    def list(self, remote_path=""):
        return self._execute(
            "list",
            f"{self.server}/{remote_path}"
        )