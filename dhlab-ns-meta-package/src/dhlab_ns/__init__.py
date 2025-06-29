"""The dhlab python library provides functions and objects
to retrieve and analyze image and text data from the digital collection of the National Library of Norway.

You can build text corpora, retrieve their metadata, search for images, and do quantitative analyses.

The dhlab python package calls the [DHLAB API](https://api.nb.no/dhlab/) under the hood to retrieve data.
"""
# api
from dhlab_ns.api.dhlab_api import totals

# legacy code
from dhlab_ns.legacy import (
    graph_networkx_louvain,
    module_update,
    nb_external_files,
    nbpictures,
    nbtext,
    token_map,
)

# # metadata
# from dhlab.metadata.natbib import metadata_from_urn, metadata_query

# # ngram
# from dhlab.ngram.ngram import Ngram, NgramBook, NgramNews

# text
from dhlab_ns.text import nbtokenizer
from dhlab_ns.text.chunking import Chunks
from dhlab_ns.text.conc_coll import Collocations, Concordance, Counts
from dhlab_ns.text.corpus import Corpus
from dhlab_ns.text.dispersion import Dispersion
from dhlab_ns.text.geo_data import GeoData, GeoNames
from dhlab_ns.text.parse import NER, POS, Models
from dhlab_ns.text.wildcard import WildcardWordSearch
from dhlab_ns.utils.display import css
from dhlab_ns.utils.files import download_from_github, get_file_from_github

# # wordbank
# from dhlab.wordbank.wordbank import WordForm, WordLemma, WordParadigm
