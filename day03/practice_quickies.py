# 1. CONFIG DICTIONARY VIA **kwargs

def build_config(env = 'dev',debug = False, verbose = False, **kwargs):

    d = {'debug':debug, 'verbose':verbose, 'env':env} | kwargs
    return d

print(build_config(env='prod', timeout=30))
print(build_config())
print(build_config(debug=True, region='us-east'))
