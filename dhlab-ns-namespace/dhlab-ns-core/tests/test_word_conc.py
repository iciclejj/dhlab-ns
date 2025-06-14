from dhlab_ns.text.conc_coll import WordConc

# testparams
dhlab_books = [
    100000000,
    100000001,
    100000002,
    100000003,
    100000004,
    100000005,
    100000006,
    100000007,
    100000008,
    100000009,
    100422432,
    100437934,
    100563959,
]
urn_books = [
    "URN:NBN:no-nb_digibok_2008091004038",
    "URN:NBN:no-nb_digibok_2021030248529",
    "URN:NBN:no-nb_digibok_2020100607613",
]


class TestWordConc:
    def test_word_conc(self):
        c = WordConc(urn=urn_books, dhlabid=dhlab_books, words=["han", "hun"])
        assert c is not None
        assert len(c) > 0
        assert c.frame.shape[0] > 0

    def test_empty(self):
        c = WordConc()
        assert c is not None
        assert len(c) == 0
        assert c.frame.shape[0] == 0
