import os
import json
import pytest
import random
from typing import Dict, Any, Generator


from filelock import Filelock
from contextlib import contextmanager


def is_parallel_mode(request) -> bool:
    """Check is the mode is parallel or not."""

    return "-n" in request.config.invocation_params.args

def get_certain_account(necessary_status: bool = False)-> Dict[str, Any]:
    """
    Function to get certain busy or not busy account
    :param necessary_status:
    :return:
    """
    lock_file_path, json_file_path = "account_data.json.lock", "account_data.json"
    with Filelock (lock_file_path):
        with open(json_file_path) as infile:
            account_list = json.load(infile)["account"]

        if os.path.isfile(json_file_path):
            free_or_busy_account = [account for account in account_list
                                    if account ["isBusy"] is not necessary_status]
            certain_account = random.choice(free_or_busy_accounts)
        else:
            certain_account = random.choice(account_list)
        return certain_account


"""
Running tests in parallel with pytest can significantly reduce the time it takes to execute a large test suite.
To achieve parallel test execution, you can use the pytest-xdist plugin, which extends pytest with new command-line 
options to run multiple tests at the same time.
"""