import pandas as pd
from pandas import DataFrame

from dhlab_ns.api.nb_ngram_api import get_ngram


def nb_ngram(
    terms: str,
    corpus: str = "bok",
    smooth: int = 1,
    years: tuple = (1810, 2010),
    mode: str = "relative",
    lang: str = "nob",
):
    """Extract N-gram frequencies from given `terms` and `years`.
    `lang` param is not supported for corpus=`avis` and will be set to None if `avis` is passed.

    The `lang` param is not supported for `corpus="avis"` and will be set to None if `avis` is passed.

    Returns:
        A sorted Pandas DataFrame indexed by year, with columns for each term.

    :meta private:
    """
    # Set default lang for 'bok'-corpus
    if corpus == "avis":
        lang = None

    df = ngram_conv(
        get_ngram(terms, corpus=corpus, lang=lang),
        smooth=smooth,
        years=years,
        mode=mode,
    )
    df.index = df.index.astype(int)
    return df.sort_index()


## tar tilbake til original den her virker ikke LGJ
def ngram_conv_old(
    ngrams, smooth: int = 1, years: tuple = (1810, 2013), mode: str = "relative"
) -> DataFrame:
    """Construct a dataframe with ngram mean frequencies per year over a given time period.

    :meta private:
    """
    ngc = {}
    # check if relative frequency or absolute frequency is in question
    if mode.startswith("rel") or mode == "y":
        arg = "y"
    else:
        arg = "f"
    for x in ngrams:
        if x and isinstance(x, list):
            ngc[x["key"]] = {
                z["x"]: z[arg]
                for z in x["values"]
                if years[1] >= int(z["x"]) >= years[0]
            }
    return pd.DataFrame(ngc).rolling(window=smooth, win_type="triang").mean()


def ngram_conv(
    ngrams,
    smooth: int = 1,
    years: tuple = (1810, 2013),
    mode: str = "relative",
) -> DataFrame:
    """Construct a dataframe with ngram mean frequencies per year over a given time period.

    Args:
        ngrams: To be filled in.
        smooth: Smoothing factor for the graph visualisation.
        years: Tuple with start and end years for the time period of interest
        mode: Frequency measure.

    Returns:
        pandas dataframe with mean values for each year

    :meta private:
    """
    ngc = {}
    # check if relative frequency or absolute frequency is in question
    if mode.startswith("rel") or mode == "y":
        arg = "y"
    else:
        arg = "f"
    for x in ngrams:
        # check if x is a non empty ngram - empty ngrams are coded as empty lists
        # if x is non emtpy it accepts keys - look at alternative isinstance(x, dict)?
        if x != []:
            ngc[x["key"]] = {
                z["x"]: z[arg]
                for z in x["values"]
                if int(z["x"]) <= int(years[1]) and int(z["x"]) >= int(years[0])
            }

    return pd.DataFrame(ngc).rolling(window=smooth, win_type="triang").mean()
