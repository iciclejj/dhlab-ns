from dhlab_ns.api.dhlab_api import wildcard_search
from dhlab_ns.text.dhlab_object import DhlabObj


class WildcardWordSearch(DhlabObj):
    """
    Find a class of words matching a wildcard string
    """

    def __init__(self, word, factor=2, freq_limit=10, limit=50):
        """
        Args:
            word: word from a mixture of * and characters
            factor: the additional length of words to be returned
            freq_limit: the frequency of returned words lower limit
            limit: number of words returned
        """
        self.words = wildcard_search(
            word, factor=factor, freq_limit=freq_limit, limit=limit
        )
        super().__init__(self.words)
