
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

# DGEEC source filename prefix.
DGEEC_PREFIX = 'dgeec'

# DGEEC source base URL.
DGEEC_BASEURL = 'https://www.dgeec.mec.pt/np4/38/'

# Query parameter to obtain published date.
DGEEC_UPDATED_PARAM = 'form'

# Substring indicating location of published date.
DGEEC_UPDATED_GREP = 'Atualizado em'

# Expected published date.
DGEEC_UPDATED_EXPECTED = '2022-12-06'

# URL suffix to obtain paged results from POST.
DGEEC_PAGED_SUFFIX = '?page='

# Substring indicating paged output.
DGEEC_PAGED_GREP = '15 por página'

# Table headers in paged results and corresponding DataFrame headers.
DGEEC_PAGED_TO_DF = {
    'Nome do estabelecimento': 'nomeEstabelecimento',
    'Tipo de Ensino': 'tipoEnsino',
    'Dependência': 'depende',
    'Distrito': 'distrito',
}

# Field names in individual results and corresponding DataFrame headers.
DGEEC_RESULT_TO_DF = {
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

# DGEEC source unique ID.
DGEEC_ID = 'codigoEstabelecimento'

# ECHE API prefix.
ECHEAPI_PREFIX = 'eche'

# ECHE API URL for scoped results.
ECHEAPI_URL = 'https://eche-list.erasmuswithoutpaper.eu/api/countryCodeIso/PT/'

# ECHE API source unique ID.
ECHEAPI_ID = 'erasmusCodeNormalized'

# Processed columns for postal code matching.
CLEAN_CP7 = 'cp7'
CLEAN_CP4 = 'cp4'

# Processed column for FQDN matching.
CLEAN_FQDN = 'fqdn'

# Parameters for URL parsing.
SUBDOMAINS_TO_REMOVE = [
    'novoportal',
    'www',
]
