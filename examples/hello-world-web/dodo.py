DOIT_CONFIG = {'verbosity':2}

def task_dev():
    """Run the main task for the project"""
    return {
        'actions': ["python3 -m hello-world-web"],
    }
