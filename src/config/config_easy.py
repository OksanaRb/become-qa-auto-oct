import os


class ConfigEasy:
    """Config class is responsible to storing frameworks and envs configuration"""
    
    request_timeout = 29
    user_name = os.environ.get('USERNAME')
    env = os.environ.get('BQA_ENV')


config = ConfigEasy()

print(config.request_timeout)
print(config.user_name)
print(config.env)