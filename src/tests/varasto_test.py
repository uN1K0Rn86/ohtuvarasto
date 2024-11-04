import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_tilavuus(self):
        self.neg_tilavuus = Varasto(-2)
        self.assertAlmostEqual(self.neg_tilavuus.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        self.neg_varasto = Varasto(10, -2)
        self.assertAlmostEqual(self.neg_varasto.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivinen_lisays(self):
        saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-4)
        self.assertAlmostEqual(saldo, self.varasto.saldo)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_liikaa(self):
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ota_negatiivinen_maara(self):
        saldo = self.varasto.saldo
        self.varasto.ota_varastosta(-4)
        self.assertAlmostEqual(saldo, self.varasto.saldo)

    def test_ota_kaikki(self):
        self.varasto.lisaa_varastoon(8)
        kaikki = self.varasto.ota_varastosta(15)
        self.assertAlmostEqual(kaikki, 8)

    def test_string_method(self):
        varasto = str(self.varasto)
        self.assertEqual(varasto, "saldo = 0, vielä tilaa 10")