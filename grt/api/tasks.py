from grt.ext import rq


@rq.job(description='')
def monitor(town):
    pass
