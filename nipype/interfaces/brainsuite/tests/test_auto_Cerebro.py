# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..brainsuite import Cerebro


def test_Cerebro_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        costFunction=dict(
            argstr='-c %d',
            usedefault=True,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputAtlasLabelFile=dict(
            argstr='--atlaslabels %s',
            extensions=None,
            mandatory=True,
        ),
        inputAtlasMRIFile=dict(
            argstr='--atlas %s',
            extensions=None,
            mandatory=True,
        ),
        inputBrainMaskFile=dict(
            argstr='-m %s',
            extensions=None,
        ),
        inputMRIFile=dict(
            argstr='-i %s',
            extensions=None,
            mandatory=True,
        ),
        keepTempFiles=dict(argstr='--keep', ),
        linearConvergence=dict(argstr='--linconv %f', ),
        outputAffineTransformFile=dict(
            argstr='--air %s',
            extensions=None,
            genfile=True,
        ),
        outputCerebrumMaskFile=dict(
            argstr='-o %s',
            extensions=None,
            genfile=True,
        ),
        outputLabelVolumeFile=dict(
            argstr='-l %s',
            extensions=None,
            genfile=True,
        ),
        outputWarpTransformFile=dict(
            argstr='--warp %s',
            extensions=None,
            genfile=True,
        ),
        tempDirectory=dict(argstr='--tempdir %s', ),
        tempDirectoryBase=dict(argstr='--tempdirbase %s', ),
        useCentroids=dict(argstr='--centroids', ),
        verbosity=dict(argstr='-v %d', ),
        warpConvergence=dict(argstr='--warpconv %f', ),
        warpLabel=dict(argstr='--warplevel %d', ),
    )
    inputs = Cerebro.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Cerebro_outputs():
    output_map = dict(
        outputAffineTransformFile=dict(extensions=None, ),
        outputCerebrumMaskFile=dict(extensions=None, ),
        outputLabelVolumeFile=dict(extensions=None, ),
        outputWarpTransformFile=dict(extensions=None, ),
    )
    outputs = Cerebro.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
