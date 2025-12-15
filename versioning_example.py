import hug


@hug.get('/echo', versions=1)
def echo(text):
    return text

@hug.get('/get', versions=range(2, 5))
def echo(text):
    return f"Echo: {text}"