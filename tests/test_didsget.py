import os
from voipms import VoipMs


class TestDidsGet:
    client = VoipMs(os.environ["VOIPMS_USERNAME"],
                    os.environ["VOIPMS_PASSWORD"])

    def test_dids_can(self):
        rate_center = self.client.dids.get.rate_centers_can("BC")[
            "ratecenters"][0]
        result = self.client.dids.get.dids_can("BC", rate_center["ratecenter"])
        assert result["status"] == "success"
        assert "dids" in result
        assert len(result["dids"]) > 0

    def test_dids_info(self):
        result = self.client.dids.get.dids_info()
        assert result["status"] == "success"
        assert "dids" in result
        assert len(result["dids"]) > 0

    def test_dids_usa(self):
        rate_center = self.client.dids.get.rate_centers_usa("CO")[
            "ratecenters"][0]
        result = self.client.dids.get.dids_usa("CO", rate_center["ratecenter"])
        assert result["status"] == "success"
        assert "dids" in result
        assert len(result["dids"]) > 0

    def test_provinces(self):
        result = self.client.dids.get.provinces()
        assert result["status"] == "success"
        assert "provinces" in result
        assert len(result["provinces"]) == 13
        assert "AB" in [p["province"] for p in result["provinces"]]

    def test_recordings(self):
        result = self.client.dids.get.recordings()
        assert result["status"] == "success"
        assert "recordings" in result
        assert len(result["recordings"]) > 0

    def test_sip_uris(self):
        result = self.client.dids.get.sip_uris()
        assert result["status"] == "success"
        assert "sipuris" in result
        assert len(result["sipuris"]) > 0
