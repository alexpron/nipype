# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..core import SEMLikeCommandLine


def test_SEMLikeCommandLine_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
    )
    inputs = SEMLikeCommandLine.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
