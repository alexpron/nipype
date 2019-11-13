# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import LFCD


def test_LFCD_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        autoclip=dict(argstr='-autoclip', ),
        automask=dict(argstr='-automask', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='%s',
            copyfile=False,
            extensions=None,
            mandatory=True,
            position=-1,
        ),
        mask=dict(
            argstr='-mask %s',
            extensions=None,
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        out_file=dict(
            argstr='-prefix %s',
            extensions=None,
            name_source=['in_file'],
            name_template='%s_afni',
        ),
        outputtype=dict(),
        polort=dict(argstr='-polort %d', ),
        thresh=dict(argstr='-thresh %f', ),
    )
    inputs = LFCD.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_LFCD_outputs():
    output_map = dict(out_file=dict(extensions=None, ), )
    outputs = LFCD.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
