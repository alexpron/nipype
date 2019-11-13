# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..model import FEATModel


def test_FEATModel_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ev_files=dict(
            argstr='%s',
            copyfile=False,
            mandatory=True,
            position=1,
        ),
        fsf_file=dict(
            argstr='%s',
            copyfile=False,
            extensions=None,
            mandatory=True,
            position=0,
        ),
        output_type=dict(),
    )
    inputs = FEATModel.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_FEATModel_outputs():
    output_map = dict(
        con_file=dict(extensions=None, ),
        design_cov=dict(extensions=None, ),
        design_file=dict(extensions=None, ),
        design_image=dict(extensions=None, ),
        fcon_file=dict(extensions=None, ),
    )
    outputs = FEATModel.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
