# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import DegreeCentrality


def test_DegreeCentrality_inputs():
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
        oned_file=dict(argstr='-out1D %s', ),
        out_file=dict(
            argstr='-prefix %s',
            extensions=None,
            name_source=['in_file'],
            name_template='%s_afni',
        ),
        outputtype=dict(),
        polort=dict(argstr='-polort %d', ),
        sparsity=dict(argstr='-sparsity %f', ),
        thresh=dict(argstr='-thresh %f', ),
    )
    inputs = DegreeCentrality.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_DegreeCentrality_outputs():
    output_map = dict(
        oned_file=dict(extensions=None, ),
        out_file=dict(extensions=None, ),
    )
    outputs = DegreeCentrality.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
