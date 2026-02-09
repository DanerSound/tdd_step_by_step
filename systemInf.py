import platform


def system_information():

    return {
        'system': platform.system(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'architecture': platform.architecture(),
        'python_version': platform.python_version(),
    }

system_information()