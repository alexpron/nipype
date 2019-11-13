# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..convert import Camino2Trackvis


def test_Camino2Trackvis_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        data_dims=dict(
            argstr='-d %s',
            mandatory=True,
            position=4,
            sep=',',
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='-i %s',
            extensions=None,
            mandatory=True,
            position=1,
        ),
        min_length=dict(
            argstr='-l %d',
            position=3,
            units='mm',
        ),
        nifti_file=dict(
            argstr='--nifti %s',
            extensions=None,
            position=7,
        ),
        out_file=dict(
            argstr='-o %s',
            extensions=None,
            genfile=True,
            position=2,
        ),
        voxel_dims=dict(
            argstr='-x %s',
            mandatory=True,
            position=5,
            sep=',',
        ),
        voxel_order=dict(
            argstr='--voxel-order %s',
            extensions=None,
            mandatory=True,
            position=6,
        ),
    )
    inputs = Camino2Trackvis.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Camino2Trackvis_outputs():
    output_map = dict(trackvis=dict(extensions=None, ), )
    outputs = Camino2Trackvis.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
