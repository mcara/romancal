"""Roman tests for generating associatinos based on skycells"""

import os

import pytest

from romancal.associations import skycell_asn


@pytest.mark.bigdata
def test_skycell_asn_generation(rtdata):
    """Test for the generation of associations based on skycells"""

    # This test should generate seven json files
    args = [
        "r0000101001001001001_0002_wfi01_cal.asdf",
        "r0000101001001001001_0002_wfi10_cal.asdf",
        "-o",
        "r512",
    ]
    rtdata.get_data("WFI/image/r0000101001001001001_0002_wfi01_cal.asdf")
    rtdata.get_data("WFI/image/r0000101001001001001_0002_wfi10_cal.asdf")

    skycell_asn._cli(args)

    # skycell associations that should be generated
    output_files = [
        "r512_p_v01001001001_r274dp63x31y80_f158_asn.json",
        "r512_p_v01001001001_r274dp63x31y81_f158_asn.json",
        "r512_p_v01001001001_r274dp63x32y82_f158_asn.json",
        "r512_p_v01001001001_r274dp63x32y80_f158_asn.json",
        "r512_p_v01001001001_r274dp63x32y81_f158_asn.json",
        "r512_p_v01001001001_r274dp63x32y82_f158_asn.json",
    ]
    # Test that the json files exist
    for file in output_files:
        skycell_asn.logger.info(f"Check that the json file exists{file}")
        assert os.path.isfile(file)
