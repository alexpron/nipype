# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..brainsuite import Dewisp


def test_Dewisp_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputMaskFile=dict(
            argstr='-i %s',
            extensions=None,
            mandatory=True,
        ),
        maximumIterations=dict(argstr='-n %d', ),
        outputMaskFile=dict(
            argstr='-o %s',
            extensions=None,
            genfile=True,
        ),
        sizeThreshold=dict(argstr='-t %d', ),
        timer=dict(argstr='--timer', ),
        verbosity=dict(argstr='-v %d', ),
    )
    inputs = Dewisp.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Dewisp_outputs():
    output_map = dict(outputMaskFile=dict(extensions=None, ), )
    outputs = Dewisp.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
