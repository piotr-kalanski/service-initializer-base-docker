def run_task(name: str, description: str, parameters: dict, service_metadata: dict):
    for k,v in parameters.items():
        print(f"{k} -> {v}")
    for k,v in service_metadata.items():
        print(f"{k} -> {v}")        
    print(f"{name} {description} {str(parameters)} {str(service_metadata)}")
