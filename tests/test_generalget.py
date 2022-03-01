import os
from voipms import VoipMs


class TestGeneralGet:
    client = VoipMs(os.environ["VOIPMS_USERNAME"],
                    os.environ["VOIPMS_PASSWORD"])

    def test_servers_info(self):
        result = self.client.general.get.servers_info()
        assert result["status"] == "success"
        assert "servers" in result
        assert len(result["servers"]) > 0
        assert "San Jose-2" in [s["server_shortname"]
                                for s in result["servers"]]
