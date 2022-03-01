import os
from voipms import VoipMs


class TestAccountsGet:
    client = VoipMs(os.environ["VOIPMS_USERNAME"],
                    os.environ["VOIPMS_PASSWORD"])

    def test_sub_accounts(self):
        result = self.client.accounts.get.sub_accounts()
        assert result["status"] == "success"
        assert "accounts" in result
        assert len(result["accounts"]) > 0
