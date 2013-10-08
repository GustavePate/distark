
from distark.commons.utils.uniq import Uniq


class TestUniq(object):

    def test_uniq(self):
        u = Uniq()
        cpt = 100
        pool = []
        while cpt > 0:
            pool.append(u.getid(u.CLIENT))
            cpt -= 1
        # del doublons
        spool = set(pool)
        assert len(pool) == len(spool)
