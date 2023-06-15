
# Temporary files directory.
TMP_DIR = 'tmp'

# Primary source URL for published date.
UPDATED_URL = 'https://www.dgeec.mec.pt/np4/38/?form'

# Substring indicating location of published date.
UPDATED_GREP = 'Atualizado em'

# Primary source URL for paged results.
PAGED_URL = 'https://www.dgeec.mec.pt/np4/38/?page=0'

# Table headers in paged results and corresponding DataFrame headers.
PAGED_TO_DF = {
    'Nome do estabelecimento': 'nomeEstabelecimento',
    'Tipo de Ensino': 'tipoEnsino',
    'Dependência': 'dependencia',
    'Distrito': 'distrito',
}

# Field names in individual results and corresponding DataFrame headers.
RESULT_TO_DF = {
    'Nome do Estabelecimento': 'nomeEstabelecimento',
    'Depende de': 'dependencia',
    'Código do Estabelecimento': 'codigoEstabelecimento',
    'Tipo de Ensino': 'tipoEnsino',
    'Website': 'website',
    'Email': 'email',
    'Morada': 'morada',
    'Código Postal': 'codigoPostal',
    'Distrito': 'distrito',
    'Concelho': 'concelho',
    'Telefone': 'telefone',
    'Outro Telefone': 'outroTelefone',
    'Fax': 'fax',
    'Outro Fax': 'outroFax',
}

# Secondary source URL for postal code search.
POSTAL_URL = 'https://json.geoapi.pt/cp/'

# ECHE API URL for scoped results.
ECHEAPI_URL = 'https://eche-list.erasmuswithoutpaper.eu/api/countryCodeIso/PT/'
