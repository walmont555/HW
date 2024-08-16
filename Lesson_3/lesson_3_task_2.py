from smartphone import Smartphone


catalog = []
catalog.append(Smartphone("самсунг", "А52", "+79057775511"))
catalog.append(Smartphone("самсунг", "А5", "+79031112233"))
catalog.append(Smartphone("самсунг", "А3", "+79262229900"))
catalog.append(Smartphone("самсунг", "А8", "+79178883344"))
catalog.append(Smartphone("самсунг", "А10", "+79029990044"))
for phone in catalog:
    print(f"{phone.marka} - {phone.model}. {phone.phone}")