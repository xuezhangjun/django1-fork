#!/usr/bin/env python
import os
import sys
# fork push test

# test_meger-upstream
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
