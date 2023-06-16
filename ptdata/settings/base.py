
# Temporary files directory.
TMP_DIR = 'tmp'

# Filename separator.
SEP = '__'

# Database directory.
DB_DIR = ''

# Database filename.
DB_FILENAME = 'data.db'

# Primary database table.
DB_TABLE = 'main'

# Primary source filename prefix.
PRIMARY_PREFIX = 'dgeec'

# Primary source base URL.
PRIMARY_BASEURL = 'https://www.dgeec.mec.pt/np4/38/'

# Query parameter to obtain published date.
PRIMARY_UPDATED_PARAM = 'form'

# Substring indicating location of published date.
PRIMARY_UPDATED_GREP = 'Atualizado em'

# Expected published date.
PRIMARY_UPDATED_EXPECTED = '2022-12-06'

# URL suffix to obtain paged results from POST.
PRIMARY_PAGED_SUFFIX = '?page='

# Substring indicating paged output.
PRIMARY_PAGED_GREP = '15 por página'

# Table headers in paged results and corresponding DataFrame headers.
PRIMARY_PAGED_TO_DF = {
    'Nome do estabelecimento': 'nomeEstabelecimento',
    'Tipo de Ensino': 'tipoEnsino',
    'Dependência': 'depende',
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
