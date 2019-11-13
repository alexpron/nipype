# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import TVAdjustVoxSpTask


def test_TVAdjustVoxSpTask_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='-in %s',
            extensions=None,
            mandatory=True,
        ),
        origin=dict(
            argstr='-origin %g %g %g',
            xor=['target_file'],
        ),
        out_file=dict(
            argstr='-out %s',
            extensions=None,
            keep_extension=True,
            name_source='in_file',
            name_template='%s_avs',
        ),
        target_file=dict(
            argstr='-target %s',
            extensions=None,
            xor=['voxel_size', 'origin'],
        ),
        voxel_size=dict(
            argstr='-vsize %g %g %g',
            xor=['target_file'],
        ),
    )
    inputs = TVAdjustVoxSpTask.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_TVAdjustVoxSpTask_outputs():
    output_map = dict(out_file=dict(extensions=None, ), )
    outputs = TVAdjustVoxSpTask.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
