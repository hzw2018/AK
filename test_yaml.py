from base.base_yaml import BaseYaml


def test_yaml():
    assr  = []
    for data in BaseYaml("data_longin.yaml").base_yaml().values():
        assr.append((data.get("username"),data.get("password")))
    return  assr



print(test_yaml())