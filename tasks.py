from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py")


@task
def test(ctx):
    ctx.run("pytest src")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src; coverage xml")

@task
def coveragehtml(ctx):
    ctx.run("coverage run --branch -m pytest src; coverage html")


@task
def lint(ctx):
    ctx.run("pylint src")
