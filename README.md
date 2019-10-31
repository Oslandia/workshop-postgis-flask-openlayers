# Installation du workshop en mode dév

Installer ansible dans un environnement virtuel

```sh
virtualenv -p python3 venv
. venv/bin/activate
python3 -m pip install ansible
```

Ensuite récupérer la machine virtuelle et la configurer
```
vagrant up
vagrant provision
```




