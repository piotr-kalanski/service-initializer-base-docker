def run_task(name: str, description: str, parameters: dict):
    for k,v in parameters.items():
        print(f"{k} -> {v}")
    print(f"{name} {description} {str(parameters)}")
