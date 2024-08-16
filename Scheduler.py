from SensitiveDataChecker import SensitiveDataChecker
from BranchProtector import BranchProtector

from apscheduler.schedulers.blocking import BlockingScheduler

""" This script schedules and executes the checks and fixes 
"""


def job():
    token = 'token----------%'  # Replace with actual token
    checker = SensitiveDataChecker(token)
    protector = BranchProtector(token)

    # enforcer.set_repositories_public()

    checker.check_public_repositories()
    protector.enforce_branch_protections()


if __name__ == "__main__":

    scheduler = BlockingScheduler()
    job()  # Run immediately upon start

    # Schedule the job to run daily at 1:00 AM
    scheduler.add_job(job, 'cron', hour=1)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
