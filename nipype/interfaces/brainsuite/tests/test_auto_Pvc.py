# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..brainsuite import Pvc


def test_Pvc_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputMRIFile=dict(
            argstr='-i %s',
            extensions=None,
            mandatory=True,
        ),
        inputMaskFile=dict(
            argstr='-m %s',
            extensions=None,
        ),
        outputLabelFile=dict(
            argstr='-o %s',
            extensions=None,
            genfile=True,
        ),
        outputTissueFractionFile=dict(
            argstr='-f %s',
            extensions=None,
            genfile=True,
        ),
        spatialPrior=dict(argstr='-l %f', ),
        threeClassFlag=dict(argstr='-3', ),
        timer=dict(argstr='--timer', ),
        verbosity=dict(argstr='-v %d', ),
    )
    inputs = Pvc.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Pvc_outputs():
    output_map = dict(
        outputLabelFile=dict(extensions=None, ),
        outputTissueFractionFile=dict(extensions=None, ),
    )
    outputs = Pvc.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
