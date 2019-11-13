# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..convert import AnalyzeHeader


def test_AnalyzeHeader_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        centre=dict(
            argstr='-centre %s',
            units='mm',
        ),
        data_dims=dict(
            argstr='-datadims %s',
            units='voxels',
        ),
        datatype=dict(
            argstr='-datatype %s',
            mandatory=True,
        ),
        description=dict(argstr='-description %s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        greylevels=dict(
            argstr='-gl %s',
            units='NA',
        ),
        in_file=dict(
            argstr='< %s',
            extensions=None,
            mandatory=True,
            position=1,
        ),
        initfromheader=dict(
            argstr='-initfromheader %s',
            extensions=None,
            position=3,
        ),
        intelbyteorder=dict(argstr='-intelbyteorder', ),
        networkbyteorder=dict(argstr='-networkbyteorder', ),
        nimages=dict(
            argstr='-nimages %d',
            units='NA',
        ),
        offset=dict(
            argstr='-offset %d',
            units='NA',
        ),
        out_file=dict(
            argstr='> %s',
            extensions=None,
            genfile=True,
            position=-1,
        ),
        picoseed=dict(
            argstr='-picoseed %s',
            units='mm',
        ),
        printbigendian=dict(
            argstr='-printbigendian %s',
            extensions=None,
            position=3,
        ),
        printimagedims=dict(
            argstr='-printimagedims %s',
            extensions=None,
            position=3,
        ),
        printintelbyteorder=dict(
            argstr='-printintelbyteorder %s',
            extensions=None,
            position=3,
        ),
        printprogargs=dict(
            argstr='-printprogargs %s',
            extensions=None,
            position=3,
        ),
        readheader=dict(
            argstr='-readheader %s',
            extensions=None,
            position=3,
        ),
        scaleinter=dict(
            argstr='-scaleinter %d',
            units='NA',
        ),
        scaleslope=dict(
            argstr='-scaleslope %d',
            units='NA',
        ),
        scheme_file=dict(
            argstr='%s',
            extensions=None,
            position=2,
        ),
        voxel_dims=dict(
            argstr='-voxeldims %s',
            units='mm',
        ),
    )
    inputs = AnalyzeHeader.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_AnalyzeHeader_outputs():
    output_map = dict(header=dict(extensions=None, ), )
    outputs = AnalyzeHeader.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
