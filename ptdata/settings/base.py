
# Temporary files directory.
TMP_DIR = 'tmp'

# Filename separator.
SEP = '__'

# Primary source filename prefix.
PRIMARY_PREFIX = 'dgeec'

# Primary source base URL.
PRIMARY_BASEURL = 'https://www.dgeec.mec.pt/np4/38/'

# Query parameter to obtain published date.
PRIMARY_UPDATED_PARAM = 'form'

# Substring indicating location of published date.
PRIMARY_UPDATED_GREP = 'Atualizado em'

# Query parameter to obtain paged results.
PRIMARY_PAGED_PARAM = 'page'

# Table headers in paged results and corresponding DataFrame headers.
PRIMARY_PAGED_TO_DF = {
    'Nome do estabelecimento': 'nomeEstabelecimento',
    'Tipo de Ensino': 'tipoEnsino',
    'Dependência': 'dependencia',
    'Distrito': 'distrito',
}

# Field names in individual results and corresponding DataFrame headers.
PRIMARY_RESULT_TO_DF = {
    'Nome do Estabelecimento': 'nomeEstabelecimento',
    'Depende de': 'depende',
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

# Secondary source filename prefix.
SECONDARY_PREFIX = 'geoapi'

# Secondary source base URL.
SECONDARY_BASEURL = 'https://json.geoapi.pt/cp/'

# ECHE API prefix.
ECHEAPI_PREFIX = 'echeapi'

# ECHE API URL for scoped results.
ECHEAPI_URL = 'https://eche-list.erasmuswithoutpaper.eu/api/countryCodeIso/PT/'
