# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..developer import MedicAlgorithmImageCalculator


def test_MedicAlgorithmImageCalculator_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inOperation=dict(argstr='--inOperation %s', ),
        inVolume=dict(
            argstr='--inVolume %s',
            extensions=None,
        ),
        inVolume2=dict(
            argstr='--inVolume2 %s',
            extensions=None,
        ),
        null=dict(argstr='--null %s', ),
        outResult=dict(
            argstr='--outResult %s',
            hash_files=False,
        ),
        xDefaultMem=dict(argstr='-xDefaultMem %d', ),
        xMaxProcess=dict(
            argstr='-xMaxProcess %d',
            usedefault=True,
        ),
        xPrefExt=dict(argstr='--xPrefExt %s', ),
    )
    inputs = MedicAlgorithmImageCalculator.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_MedicAlgorithmImageCalculator_outputs():
    output_map = dict(outResult=dict(extensions=None, ), )
    outputs = MedicAlgorithmImageCalculator.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
