# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..label_fusion import CalcTopNCC


def test_CalcTopNCC_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='-target %s',
            extensions=None,
            mandatory=True,
            position=1,
        ),
        in_templates=dict(
            argstr='%s',
            mandatory=True,
            position=3,
        ),
        mask_file=dict(
            argstr='-mask %s',
            extensions=None,
        ),
        num_templates=dict(
            argstr='-templates %s',
            mandatory=True,
            position=2,
        ),
        top_templates=dict(
            argstr='-n %s',
            mandatory=True,
            position=4,
        ),
    )
    inputs = CalcTopNCC.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_CalcTopNCC_outputs():
    output_map = dict(out_files=dict(), )
    outputs = CalcTopNCC.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
