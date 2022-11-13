def steralise(params: dict, defaults: dict, excludes: list[str] = []) -> str:
    excludes.append("self")
    new = {}
    for key, value in params.items():
        if key in excludes:
            continue
        new[key] = defaults[key] if value is None else value
    return new

def to_str(params: dict) -> str:
    f = ""
    for key, value in params.items():
        f += f"{key}={','.join(value).lower() if isinstance(value, list) else str(value).lower()}&"
    return f[:-1]
