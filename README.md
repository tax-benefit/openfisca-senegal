# OpenFisca Sénégal

Senegalese tax and benefit system for OpenFisca

> Warning: this is highly experimental!

This work was done during the first [hackathon in Dakar for Innovation and Collaboration for the Senegalese Tax System](http://www.imf.org/en/News/Events/Hackathon-Technological-Innovation-for-the-Senegalese-Tax-Administration)

See the [Jupyter Notebook](/notebooks/Senegalese%20tax%20and%20benefit%20system%20from%20scratch.ipynb).

## Links

- http://www.gouv.sn/IMG/pdf/cgi2013.pdf
- http://www.impotsetdomaines.gouv.sn/sites/default/files/formulaires/ir_declarationsanspagedegarde.pdf
- http://www.impotsetdomaines.gouv.sn/fr/simulateur-dimpots

## API

### Installation

```sh
pip install -e '.[api]' # needs to be executed in the folder containing the setup.py file
```

### Run

```sh
paster serve api/api_config.ini
```

To test with a sample file:

```sh
curl http://localhost:2000/api/1/calculate -X POST --data @./api/test.json --header 'Content-type: application/json'
```
