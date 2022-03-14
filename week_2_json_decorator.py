import json
from functools import wraps

def to_json(func):
    @wraps(func)
    def jsoned(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return jsoned

@to_json
def sample_func():
    return {i: str(i) for i in range(10)}

if __name__ == '__main__':
    sample_func()