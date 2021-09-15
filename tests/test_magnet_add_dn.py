from trim21_flexget_plugins.modify.magnet_add_dn import PluginMagnetAddDownloadName


def test_add_dn() -> None:
    assert PluginMagnetAddDownloadName.add_dn(
        "magnet:?xt=urn:btih:190F1ABAED7AE7252735A811149753AA83E34309",
        "URL Escaped Torrent Name",
    ) == (
        "magnet:?xt=urn:btih:190F1ABAED7AE7252735A811149753AA83E34309"
        "&dn=URL+Escaped+Torrent+Name"
    )


def test_non_magnet_keep_original() -> None:
    raw = "https://example.com/a.torrent"
    assert PluginMagnetAddDownloadName.add_dn(raw, "URL Escaped Torrent Name") == raw
