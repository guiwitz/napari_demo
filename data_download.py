import os

if not os.path.isfile('Sample/cxcr4aMO2_290112.lsm'):
    os.makedirs('Sample/',exist_ok=True)
    myfile = requests.get('https://zenodo.org/record/1211599/files/cxcr4aMO2_290112.lsm?download=1', allow_redirects=True)
    open('Sample/cxcr4aMO2_290112.lsm', 'wb').write(myfile.content)
