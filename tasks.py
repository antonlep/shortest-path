from invoke import task


@task
def start(ctx, algorithm, input_file, start_x, start_y, end_x, end_y):
    ctx.run(
        f"python3 src/index.py {algorithm} {input_file} {start_x} {start_y} {end_x} {end_y}")


@task
def benchmark(ctx, algorithm, scenario):
    ctx.run(
        f"python3 src/index.py benchmark {algorithm} {scenario}")


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
